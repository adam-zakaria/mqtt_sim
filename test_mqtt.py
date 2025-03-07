import paho.mqtt.client as mqtt
import json, time

BROKER = "localhost"
TOPIC = "sensor/data"
NUM_MESSAGES = 10
received_messages = []

def on_message(client, userdata, msg):
  received_messages.append(msg.payload.decode())

def run_mqtt_test():
  print("\n🚀 Starting MQTT Test...\n")

  # Start Subscriber
  client = mqtt.Client(callback_api_version=2)  # Suppresses deprecation warning
  client.on_message = on_message
  client.connect(BROKER, 1883, 60)
  client.subscribe(TOPIC)
  client.loop_start()
  print("📡 Subscribed to topic:", TOPIC)

  # Start Publisher
  pub_client = mqtt.Client(callback_api_version=2)  # Suppresses deprecation warning
  pub_client.connect(BROKER, 1883, 60)
  for i in range(NUM_MESSAGES):
    payload = json.dumps({"id": i, "value": i * 10})
    pub_client.publish(TOPIC, payload)
    print(f"📤 Published: {payload}")
    time.sleep(0.5)
  pub_client.disconnect()

  # Wait for messages to arrive
  print('Sleeping for 1 second, to give messages to arrive')
  time.sleep(1)
  client.loop_stop()
  client.disconnect()

  # Print summary
  print(f"\n📊 Total Messages Received: {len(received_messages)} / {NUM_MESSAGES}")

  # Single assert for the entire test
  assert len(received_messages) == NUM_MESSAGES, f"❌ Test Failed: Expected {NUM_MESSAGES}, got {len(received_messages)}"

  print("✅ len(received_messages) == NUM_MESSAGES")

if __name__ == "__main__":
  run_mqtt_test()
