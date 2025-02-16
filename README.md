# ML-Based Fog-Cloud Agricultural Irrigation System

This repository contains the implementation of a smart agricultural irrigation system that leverages machine learning, fog computing, and cloud services. The system optimizes water usage for irrigation based on real-time sensor data and dynamically trained machine learning models. The repository includes Arduino code, Raspberry Pi fog scripts, a Jupyter notebook for ML model training, an MIT App Inventor app (.aia file), and a project report.

---

## 📌 Table of Contents
- [Repository Structure](#repository-structure)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
    - [Arduino Setup](#arduino-setup)
    - [Raspberry Pi Setup](#raspberry-pi-setup)
    - [Firebase Setup](#firebase-setup)
    - [Android App Setup](#android-app-setup)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)

---

## 📂 Repository Structure
```
├── Arduino Code/         # Arduino code for sensor readings and pump control
├── Fog Script/           # Python scripts for Raspberry Pi (fog computing)
├── Neural Network Training/  # Jupyter notebooks for ML model training
├── Android App/          # MIT App Inventor project file (.aia)
├── Project Report        # Detailed system design and implementation report
```

---

## 🚀 Features
✅ **Automatic Mode**: Predicts irrigation needs using real-time sensor data and dynamically trained ML models.<br />
✅ **Manual Mode**: Allows remote control of the irrigation system via a mobile app.<br />
✅ **Real-Time Data**: Collects and processes sensor data (humidity, temperature, soil moisture).<br />
✅ **Cloud Integration**: Uses Firebase for storing sensor data and trained models.<br />
✅ **Fog Computing**: Employs a Raspberry Pi for local data preprocessing and decision-making.<br />
✅ **User-Friendly Interface**: Android app for seamless monitoring and control.<br />

---

## 🛠 Getting Started
### 📌 Prerequisites
- Arduino Uno
- Raspberry Pi (or any fog device)
- Sensors (humidity, temperature, soil moisture)
- Water pump
- MIT App Inventor for Android app development
- Firebase account

---

## 📥 Installation
### 🔹 Clone the repository
```bash
 git clone https://github.com/duanepm/ML-Based-Fog-Cloud-Agricultural-Irrigation-System.git
```

### 🔹 Arduino Setup
1. Connect sensors and the water pump to the Arduino.
2. Upload the Arduino code from the `Arduino Code/` directory to the board.

### 🔹 Raspberry Pi Setup
1. Install necessary Python libraries.
2. Run the Raspberry Pi scripts from the `Fog Script/` directory.

### 🔹 Firebase Setup
1. Create a Firebase project and configure the Realtime Database.
2. Update Firebase credentials in the Raspberry Pi scripts.

### 🔹 Android App Setup
1. Import the `Android App/` project file into MIT App Inventor.
2. Update Firebase configuration in the app.
3. Build and deploy the app on your Android device.

---

## 📌 Usage
📍 **Manual Mode**: Use the Android app to control the water pump and monitor sensor data.<br />
📍 **Automatic Mode**: The system autonomously manages irrigation based on ML model predictions.<br />

---

## 📖 Documentation
Refer to the `Project Report` for details on system design, implementation, and results.

---

## 🤝 Contributing
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request. Happy coding! 🚀
