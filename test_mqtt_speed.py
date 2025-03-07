import paho.mqtt.client as mqtt
import json, time

BROKER = "localhost"
TOPIC = "sensor/accelerometer"
NUM_MESSAGES = 100000
received_messages = []
start_time = None

def on_message(client, userdata, msg):
  received_messages.append(msg.payload.decode())

def run_mqtt_speed_test():
  global start_time
  print("\n🚀 Starting MQTT Speed Test...\n")

  # Start Subscriber
  client = mqtt.Client(callback_api_version=2)
  client.on_message = on_message
  client.connect(BROKER, 1883, 60)
  client.subscribe(TOPIC)
  client.loop_start()
  print("📡 Subscribed to topic:", TOPIC)

  # Start Publisher
  pub_client = mqtt.Client(callback_api_version=2)
  pub_client.connect(BROKER, 1883, 60)
  
  start_time = time.time()  # Start timing
  for i in range(NUM_MESSAGES):
    payload = json.dumps({
      "uid": "jc-pilot001",
      "timestamp": time.time(),
      "x": 700 + (i % 10),
      "y": 690 + (i % 10),
      "z": 110 + (i % 10)
    })
    pub_client.publish(TOPIC, payload)
  
  pub_client.disconnect()

  # Wait for all messages to be received
  time.sleep(5)
  client.loop_stop()
  client.disconnect()

  # Compute results
  end_time = time.time()
  elapsed_time = end_time - start_time
  received_count = len(received_messages)
  rate = received_count / elapsed_time if elapsed_time > 0 else 0

  print(f"\n📊 Sent: {NUM_MESSAGES}, Received: {received_count}")
  print(f"⏱️ Total Time: {elapsed_time:.4f} sec")
  print(f"⚡ Max Publish Rate: {rate:.2f} messages/sec")

  # Save to file for reference
  with open("mqtt_speed_test_results.json", "w") as f:
    json.dump({
      "num_sent": NUM_MESSAGES,
      "num_received": received_count,
      "time_taken": elapsed_time,
      "publish_rate": rate
    }, f, indent=2)

  assert received_count == NUM_MESSAGES, f"❌ Test Failed: Expected {NUM_MESSAGES}, got {received_count}"

  print("✅ Speed Test Completed Successfully!\n")

if __name__ == "__main__":
  run_mqtt_speed_test()
