import time
import random
import paho.mqtt.client as mqtt


mqtt_broker = "mqtt3.thingspeak.com"
mqtt_port = 1883
client_id = "FhMQAwUWFw0jHBQ5JwsrCyA"
username = "FhMQAwUWFw0jHBQ5JwsrCyA"
password = "EWGM9SE16uBl3bAFj8GzbOyk"
channel_id = "2888587"


topic = f"channels/{channel_id}/publish"

client = mqtt.Client(client_id=client_id, protocol=mqtt.MQTTv311)
client.username_pw_set(username, password)
client.connect(mqtt_broker, mqtt_port)

print("🚀 Publishing sensor data to ThingSpeak...")

time.sleep(5)

while True:
    temperature = round(random.uniform(-50, 50), 2)
    humidity = round(random.uniform(0, 100), 2)
    co2 = random.randint(300, 2000)

    # Creating MQTT payload: field1 = temp, field2 = humidity, field3 = CO2
    payload = f"field1={temperature}&field2={humidity}&field3={co2}"

    result = client.publish(topic, payload)
    status = result[0]

    if status == 0:
        print(f"✅ Sent: {payload}")
        
        with open("sensor_log.txt", "a") as file:
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"{timestamp},{temperature},{humidity},{co2}\n")
    else:
        print("❌ Failed to send message")

    time.sleep(15)  # ThingSpeak allows updates for every 15 secs
