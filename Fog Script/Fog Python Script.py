import serial
import time
import firebase_admin
from firebase_admin import credentials, db
import pandas as pd
import tensorflow as tf
import joblib

cred = credentials.Certificate("ml-iot-irrigation.json") #Load your Firebase Database Credentials JSON
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ml-iot-irrigation-default-rtdb.firebaseio.com/' #Specify your database URL
})



model = tf.keras.models.load_model("irrigation_model.keras")
scaler = joblib.load("scaler.pkl")

ref = db.reference('/')

while True:
    try:
        ser = serial.Serial('COM6', 9600)
        print("Serial connected")
        if ser.readline().strip() == b"Ready":
                print("Arduino ready")
                break
    except serial.SerialException:
        print("Serial not connected. Retrying...")
        time.sleep(1)

def control_pump(status):
    ser.write(status.encode())


def predict_irrigation(humidity, temperature, moisture):
    sensor_data = pd.DataFrame([[moisture,temperature,humidity]], columns=['Moisture', 'Temperature', 'Humidity'])
    new_data_scaled = scaler.transform(sensor_data)
    prediction = model.predict(new_data_scaled,verbose=0)
    return prediction[0][0] > 0.5

def check_condition(condition):
    if(condition=="true"):
        return True
    else:
        return False

def give_condition(condition):
    if(condition):
        return "true"
    else:
        return "false"
        

while True:
    arduino_data = ser.readline().decode().strip()
    if arduino_data:
        data = arduino_data.split(',')
        humidity = float(data[1][2:])
        temperature = float(data[0][2:])
        moisture = float(data[2][2:])

        if(temperature<0 or humidity<0 or moisture<0):
            print("Sensor value error")
            continue
        print("Arduino Data-> Temperature:",temperature," Humidity:",humidity," Moisture:",moisture)
        
        ref.update({
            'Humidity': humidity,
            'Temperature': temperature,
            'Moisture': moisture
        })

        system_mode = check_condition(ref.child('System_mode').get())
        if system_mode:
            irrigation_needed = predict_irrigation(humidity, temperature, moisture)
            """if moisture<50:
                irrigation_needed=True
            print(irrigation_needed)"""
            ref.update({'Pump_status': give_condition(irrigation_needed)})
            if irrigation_needed:
                print("Pump Started")
                control_pump('1')
                time.sleep(1)
                ref.update({'Pump_status': "false"})
            else:
                control_pump('0')

        pump_status = check_condition(ref.child('Pump_status').get())
        if not(system_mode):
            if pump_status:
                control_pump('1')
                print("Pump Started")
                time.sleep(1)
                ref.update({'Pump_status': "false"})
            else:
                control_pump('0')

    time.sleep(0.5)
