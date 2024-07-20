# ML-Based Fog-Cloud Agricultural Irrigation System
This repository contains the implementation of a smart agricultural irrigation system that leverages machine learning, fog computing, and cloud services. The system aims to optimize water usage for irrigation based on real-time sensor data and dynamically trained machine learning models. It includes Arduino code, Raspberry Pi fog scripts, a Jupyter notebook for ML model training, an MIT App Inventor app .aia file, and a project report.

## Repository Structure
```Arduino Code/```: Contains the Arduino code for reading sensor data and controlling the water pump.<br />
```Fog Script/```: Contains Python scripts for the Raspberry Pi, acting as a fog device.<br />
```Neural Network Training/```: Includes Jupyter notebooks for training the machine learning models.<br />
```Android App/```: Contains the MIT App Inventor project file (.aia) for the Android app.<br />
```Project Report```: A report detailing the system design and implementation.<br />

## Features
Automatic Mode: Predicts irrigation needs using real-time sensor data and dynamically trained machine learning models.<br />
Manual Mode: Allows remote control of the irrigation system via a mobile app.<br />
Real-Time Data: Collects and processes sensor data (humidity, temperature, soil moisture) in real-time.<br />
Cloud Integration: Uses Firebase for storing sensor data and trained models.<br />
Fog Computing: Utilizes a Raspberry Pi for data preprocessing and local decision-making.<br />
User-Friendly Interface: Provides an Android app for switching modes and monitoring sensor data.<br />

## Getting Started

### Prerequisites
Arduino Uno<br />
Raspberry Pi (Or any fog device)<br />
Sensors (humidity, temperature, soil moisture)<br />
Water pump<br />
MIT App Inventor for Android app development<br />
Firebase account<br />

## Installation

### Clone the repository<br />
```git clone https://github.com/duanepm/ML-Based-Fog-Cloud-Agricultural-Irrigation-System.git```

### Arduino Setup
Connect sensors and water pump to the Arduino.<br />
Upload the Arduino code from the Arduino Code/ directory to the Arduino board.<br />

### Raspberry Pi Setup
Install necessary Python libraries.<br />
Run the Raspberry Pi code from the Fog Script/ directory.<br />

### Firebase Setup
Create a Firebase project and configure the Realtime Database.<br />
Update Firebase credentials in the Raspberry Pi code.<br />

### Android App Setup
Import the Android App/ project file into MIT App Inventor.<br />
Update Firebase configuration in the app.<br />
Build and run the app on your Android device.<br />

## Usage
Manual Mode: Use the Android app to manually control the water pump and monitor sensor data.<br />
Automatic Mode: The system automatically controls irrigation based on ML model predictions.<br />

## Documentation
Refer to the Project Report that includes system design, implementation details, and results.<br />

## Contributing
Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome.
