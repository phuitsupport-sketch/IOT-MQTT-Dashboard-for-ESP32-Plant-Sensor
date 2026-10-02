<div align="center"><a href="#"><img src="assets/images/logo.png" width="400" ></a><br><br>
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" target="_blank" /></div>
<br><br>


Scoplant - The IoT MQTT Django dashboard for ESP32 (TTGO T-Higrow) is a project that provides a web-based dashboard for monitoring and controlling environmental conditions using an ESP32-based sensor device. The project utilizes the MQTT protocol for seamless communication between the sensor device and the dashboard, allowing real-time updates on the status of the environment being monitored.
<br>
<div align="center"><a href="#"><img src="assets/images/v4.PNG"  width="1600"></a><br></div>

The TTGO T-Higrow device is equipped with sensors that measure various environmental parameters such as temperature, humidity, and light intensity. These measurements are transmitted to the MQTT broker, which then forwards the data to the Django backend for processing. The Django backend is responsible for storing and processing the data, as well as handling user authentication and authorization.
<br>
<div align="center"><a href="#"><img src="assets/images/v2.PNG"  width="1600"></a><br></div>

The web-based dashboard is designed using Django's templating system and is optimized for desktop and mobile devices. The dashboard displays the data in an intuitive and user-friendly manner, allowing users to monitor the environmental conditions at a glance. The dashboard also features controls that allow users to adjust the settings of the sensor device, such as the frequency of data transmission and the threshold values for triggering alerts.
<br>
<div align="center"><a href="#"><img src="assets/images/v3.PNG"  width="1600"></a><br></div>

Overall, this project has the potential to be a valuable tool for anyone who needs to remotely monitor and control their IoT devices. By creating a system that connects an MQTT device to a dashboard, users can receive real-time insights into the performance of their devices and take action when necessary.
<br>
<div align="center"><a href="#"><img src="assets/images/v1.png"  width="1600"></a><br><br></div>


## MQTT Protocol
<div align="center"><br><br>
<img src="assets/images/v6.PNG" target="_blank"width="600" /></div>


This project aims to create a system that connects an MQTT device to a dashboard, enabling users to remotely monitor and control their IoT devices. MQTT is a lightweight messaging protocol that is commonly used for transmitting telemetry data from IoT devices to other devices or servers. A dashboard, on the other hand, is a visual interface that provides real-time insights into data and allows for remote monitoring and control of devices.

To achieve this, the project will involve several components, including an MQTT broker, a web server, and a user interface that displays the data in a user-friendly format. The MQTT device will send telemetry data to the broker, which will then forward it to the web server. The web server will process the data and display it on the dashboard in real-time.



### Hardware

<div align="center"><br><br>
<img src="assets/images/v5.PNG" target="_blank"width="600" /></div>

The TTGO-T-HIGrow project is an open-source hardware and software solution for monitoring environmental conditions using an ESP32-based sensor device. The project provides a comprehensive set of resources for users to design and build their own TTGO-T-HIGrow sensor devices, including schematics, PCB layouts, and firmware code.

The project is based on open-source principles, and all resources and designs are freely available to the community. The project encourages collaboration and knowledge sharing, and welcomes contributions from users of all levels of experience.


### Resource
[TTGO-T-HIGrow]( https://github.com/pesor/TTGO-T-HIGrow)





## How to Run

This Django project is designed to be easy to set up and run. Here are the steps you need to follow to get started:

### Prerequisites
Before you can run this Django project, you need to have the following software installed:

SQLite is included with Python; no separate database server is required.

Python 3.9 or later

### Installation

To install this Django project, follow these steps:

1- Clone the project repository to your local machine using the command:
```sh
git clone https://github.com/alialaei110/IOT-MQTT-Dashboard-for-ESP32-Plant-Sensor.git
```
2- Navigate to the project directory using the command:
```sh
cd IOT-MQTT-Dashboard-for-ESP32-Plant-Sensor
```
3- Create a virtual environment and activate it using the following commands:
```sh
python -m venv env
source env/Scripts/activate
```
4- Install the project dependencies using the command:
```sh
pip install -r requirements.txt
```



### Running the Project

for the first time, before running server run commands:

```sh
python manage.py makemigrations
```
```sh
python manage.py migrate
```

Once you have installed and configured the Django project, you can run it using the following command:

```sh
python manage.py runserver
```

This command will start the Django development server, and you should be able to access the project by navigating to ```http://127.0.0.1:8000/``` in your web browser.

That's it! You should now have this Django project up and running on your local machine.


### Create user for the first time

create a superuser by writing the following command:
```sh
python manage.py createsuperuser
```
We then write the following credentials step by step. We can fill these credentials according to our preferences:

```sh
Username: admin
Email address: admin@gmail.com
Password: ********
Password (again): ********
```
Note: After filling a row, press “Enter” to fill the other information.

Now the superuser will be created if we have entered all fields correctly.


## Free deployment (Render)

The project uses Django's built-in SQLite database, stored in `db.sqlite3`; MongoDB Atlas is not required. The repository includes a Render Blueprint for a free web service. Before deploying:

1. Push this project to a GitHub repository that you own (the current `origin` points to the upstream project and may not allow pushes).
2. In Render, create a **Blueprint** from your GitHub repository. The Blueprint generates `DJANGO_SECRET_KEY` and configures the `*.onrender.com` host automatically.
3. Wait for the first deployment to finish. Render will create migrations, collect static files, run migrations and serve the app at its generated `https://...onrender.com` address. Create an administrator with `python manage.py createsuperuser` using Render Shell if available.

**Important:** Render's free web service has an ephemeral filesystem. The site can run with SQLite, but its database file (users, devices and logs) may be lost when the service restarts or is redeployed. Use a host with persistent storage, or a persistent external database, before entering data you need to keep. Render free services may also sleep when idle. The MQTT code connects to the public Eclipse test broker, which is not suitable for production and may not provide reliable telemetry.


## License
[MIT License](LICENSE)

Free Software!
