# iot-mqtt-simulation

# IoT Environment Station – MQTT + ThingSpeak

This project simulates a virtual environment sensor station using Python and MQTT to send data to ThingSpeak.

## Features
- Simulates random data for Temperature, Humidity, and CO₂
- Sends real-time updates to ThingSpeak via MQTT
- Logs all data locally for offline access
- Script to filter last 5 hours of data for any sensor

## Technologies Used
- Python 3
- paho-mqtt
- ThingSpeak MQTT Broker

## Files
- `mqtt_thingspeak_publisher.py` – Main simulator script
- `last_5_hour_data.py` – Script to view last 5 hours of data / Replace it According to the requirement 
- `sensor_log.txt` – Data log file

## How to Run
1. Install dependencies:
2. Replace MQTT credentials in `mqtt_thingspeak_publisher.py`
3. Run the script:
4. Watch the live graphs on your ThingSpeak channel.

## Author
Daivik Gangappa – Syracuse University
