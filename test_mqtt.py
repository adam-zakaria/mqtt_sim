"""
Since pytest automatically discovers test functions, test_mqtt.py doesn’t have a main() function. If you're running it directly with python test_mqtt.py, it won't execute anything because pytest is designed to discover and run functions prefixed with test_.

# Run
pytest -s test_mqtt.py
"""

import paho.mqtt.client as mqtt
import json, time

BROKER = "localhost"
TOPIC = "sensor/data"
NUM_MESSAGES = 10
received_messages = []

def on_message(client, userdata, msg):
  decoded_msg = msg.payload.decode()
  print(f"✅ Received: {decoded_msg}")  # Print each received message
  received_messages.append(decoded_msg)

def test_mqtt():
  print("🚀 Starting MQTT Test...")  # Debug print

  # Start Subscriber
  client = mqtt.Client()
  client.on_message = on_message
  client.connect(BROKER, 1883, 60)
  client.subscribe(TOPIC)
  client.loop_start()
  
  print("📡 Subscribed to topic:", TOPIC)  # Debug print

  # Publish Messages
  pub_client = mqtt.Client()
  pub_client.connect(BROKER, 1883, 60)
  for i in range(NUM_MESSAGES):
    payload = json.dumps({"id": i, "value": i * 10})
    pub_client.publish(TOPIC, payload)
    print(f"📤 Published: {payload}")  # Debug print
    time.sleep(0.5)
  pub_client.disconnect()

  # Wait for messages to arrive
  time.sleep(5)
  client.loop_stop()
  client.disconnect()

  print(f"📊 Messages Received: {len(received_messages)} / {NUM_MESSAGES}")
  assert len(received_messages) == NUM_MESSAGES, f"Expected {NUM_MESSAGES}, got {len(received_messages)}"
