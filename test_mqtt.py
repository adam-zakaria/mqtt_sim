import paho.mqtt.client as mqtt
import json, time

BROKER = "localhost"
TOPIC = "sensor/data"
NUM_MESSAGES = 10
received_messages = []

def on_message(client, userdata, msg):
  decoded_msg = msg.payload.decode()
  print(f"✅ Received: {decoded_msg}")
  received_messages.append(decoded_msg)

def run_mqtt_test():
  print("\n🚀 Starting MQTT Test...\n")

  # Start Subscriber
  client = mqtt.Client()
  client.on_message = on_message
  client.connect(BROKER, 1883, 60)
  client.subscribe(TOPIC)
  client.loop_start()
  print("📡 Subscribed to topic:", TOPIC)

  # Publish Messages
  pub_client = mqtt.Client()
  pub_client.connect(BROKER, 1883, 60)
  for i in range(NUM_MESSAGES):
    payload = json.dumps({"id": i, "value": i * 10})
    pub_client.publish(TOPIC, payload)
    print(f"📤 Test {i+1}: Published {payload}")
    time.sleep(0.5)
  pub_client.disconnect()

  # Wait for messages to arrive
  time.sleep(5)
  client.loop_stop()
  client.disconnect()

  print(f"\n📊 Messages Received: {len(received_messages)} / {NUM_MESSAGES}\n")
  
  # ✅ Validate message count
  assert len(received_messages) == NUM_MESSAGES, f"❌ Test Failed: Expected {NUM_MESSAGES}, got {len(received_messages)}"
  
  print("✅ ALL TESTS PASSED SUCCESSFULLY!\n")

if __name__ == "__main__":
  run_mqtt_test()
