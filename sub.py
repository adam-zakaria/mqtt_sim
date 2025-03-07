import paho.mqtt.client as mqtt
import time

BROKER = "localhost"
TOPIC = "sensor/data"
received_messages = []

def on_message(client, userdata, msg):
  print(f"Received: {msg.payload.decode()}")
  received_messages.append(msg.payload.decode())

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)
client.loop_start()

time.sleep(12)  # Wait to receive messages
client.loop_stop()
client.disconnect()

assert len(received_messages) == 10, f"Expected 10 messages, got {len(received_messages)}"
print("✅ All messages received successfully.")
