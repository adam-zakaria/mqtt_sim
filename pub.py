import paho.mqtt.client as mqtt
import json, time

BROKER = "localhost"
TOPIC = "sensor/data"
NUM_MESSAGES = 10
INTERVAL = 1

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

for i in range(NUM_MESSAGES):
  payload = json.dumps({"id": i, "value": round(100 * (i / NUM_MESSAGES), 2)})
  client.publish(TOPIC, payload)
  print(f"Published: {payload}")
  time.sleep(INTERVAL)

client.disconnect()
