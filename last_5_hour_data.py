from datetime import datetime, timedelta

cutoff = datetime.now() - timedelta(hours=5)
sensor = "co2"  #Change Accordingly 

with open("sensor_log.txt", "r") as file:
    for line in file:
        timestamp_str, temp, hum, co2 = line.strip().split(",")
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        if timestamp >= cutoff:
            value = {"temperature": temp, "humidity": hum, "co2": co2}[sensor]
            print(f"{timestamp} - {sensor.capitalize()}: {value}")
