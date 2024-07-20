# ML-Based Fog-Cloud Agricultural Irrigation System
This repository contains the implementation of a smart agricultural irrigation system that leverages machine learning, fog computing, and cloud services. The system aims to optimize water usage for irrigation based on real-time sensor data and dynamically trained machine learning models. It includes Arduino code, Raspberry Pi fog scripts, a Jupyter notebook for ML model training, an MIT App Inventor app .aia file, and a project report.

##Repository Structure
Arduino Code/: Contains the Arduino code for reading sensor data and controlling the water pump.
Fog Script/: Contains Python scripts for the Raspberry Pi, acting as a fog device.
Neural Network Training/: Includes Jupyter notebooks for training the machine learning models.
Android App/: Contains the MIT App Inventor project file (.aia) for the Android app.
Project Report: A report detailing the system design and implementation.

##Features
Automatic Mode: Predicts irrigation needs using real-time sensor data and dynamically trained machine learning models.
Manual Mode: Allows remote control of the irrigation system via a mobile app.
Real-Time Data: Collects and processes sensor data (humidity, temperature, soil moisture) in real-time.
Cloud Integration: Uses Firebase for storing sensor data and trained models.
Fog Computing: Utilizes a Raspberry Pi for data preprocessing and local decision-making.
User-Friendly Interface: Provides an Android app for switching modes and monitoring sensor data.

##Getting Started

###Prerequisites
Arduino Uno
Raspberry Pi (Or any fog device)
Sensors (humidity, temperature, soil moisture)
Water pump
MIT App Inventor for Android app development
Firebase account

##Installation

###Clone the repository
git clone https://github.com/yourusername/ml-fog-cloud-irrigation.git

###Arduino Setup
Connect sensors and water pump to the Arduino.
Upload the Arduino code from the Arduino Code/ directory to the Arduino board.

###Raspberry Pi Setup
Install necessary Python libraries.
Run the Raspberry Pi code from the Fog Script/ directory.

###Firebase Setup
Create a Firebase project and configure the Realtime Database.
Update Firebase credentials in the Raspberry Pi code.

###Android App Setup
Import the Android App/ project file into MIT App Inventor.
Update Firebase configuration in the app.
Build and run the app on your Android device.

##Usage
Manual Mode: Use the Android app to manually control the water pump and monitor sensor data.
Automatic Mode: The system automatically controls irrigation based on ML model predictions.

##Documentation
Refer to the Project Report that includes system design, implementation details, and results.

##Contributing
Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.
