# 📊 Test Results Template

## **Test 1**
- **Mosquitto Setting**: `max_queued_messages 100000`
- **QoS**: 0
- **Messages Sent**: 10,000
- **Messages Received**: 10,000
- **Total Time**: 0.76 sec
- **Speed**: **13,132 messages/sec**
- **Observations**: [e.g., No message loss, CPU usage ~30%]



# Raw output:
/opt/homebrew/etc/mosquitto/mosquitto.conf
max_queued_messages 100000

## NUM_MESSAGES = 50000
  mqtt_sim git:(main) ✗ py test_mqtt_speed.py

🚀 Starting MQTT Speed Test...

📡 Subscribed to topic: sensor/accelerometer

📊 Sent: 50000, Received: 43150
⏱️ Total Time: 6.0592 sec
⚡ Max Publish Rate: 7121.40 messages/sec
Traceback (most recent call last):
  File "/Users/azakaria/Code/mqtt_sim/test_mqtt_speed.py", line 71, in <module>
    run_mqtt_speed_test()
    └ <function run_mqtt_speed_test at 0x102ec82c0>
  File "/Users/azakaria/Code/mqtt_sim/test_mqtt_speed.py", line 66, in run_mqtt_speed_test
    assert received_count == NUM_MESSAGES, f"❌ Test Failed: Expected {NUM_MESSAGES}, got {received_count}"
           │                 │                                          │                   └ 43150
           │                 │                                          └ 50000
           │                 └ 50000
           └ 43150
AssertionError: ❌ Test Failed: Expected 50000, got 43150

## NUM_MESSAGES = 100,000
➜  mqtt_sim git:(main) ✗ py test_mqtt_speed.py

🚀 Starting MQTT Speed Test...

📡 Subscribed to topic: sensor/accelerometer

📊 Sent: 100000, Received: 76840
⏱️ Total Time: 7.0516 sec
⚡ Max Publish Rate: 10896.83 messages/sec
Traceback (most recent call last):
  File "/Users/azakaria/Code/mqtt_sim/test_mqtt_speed.py", line 71, in <module>
    run_mqtt_speed_test()
    └ <function run_mqtt_speed_test at 0x10515c2c0>
  File "/Users/azakaria/Code/mqtt_sim/test_mqtt_speed.py", line 66, in run_mqtt_speed_test
    assert received_count == NUM_MESSAGES, f"❌ Test Failed: Expected {NUM_MESSAGES}, got {received_count}"
           │                 │                                          │                   └ 76840
           │                 │                                          └ 100000
           │                 └ 100000
           └ 76840
AssertionError: ❌ Test Failed: Expected 100000, got 76840
➜  mqtt_sim git:(main) ✗ 

### Intpretation
🔴 What This Tells Us
Message loss increases with volume

At 50,000 messages, you lost 13.7%.
At 100,000 messages, you lost 23.2%.
Conclusion: The system struggles as message volume increases.
Publishing speed increases, but losses grow

The publish rate improved from 7,121 msg/sec → 10,896 msg/sec.
However, message loss increased, meaning the broker or subscriber is overwhelmed.


/opt/homebrew/etc/mosquitto/mosquitto.conf
max_queued_messages 100000

## NUM_MESSAGES = 50000 
➜  mqtt_sim git:(main) ✗ py test_mqtt_speed.py                         

🚀 Starting MQTT Speed Test...

📡 Subscribed to topic: sensor/accelerometer

📊 Sent: 50000, Received: 50000
⏱️ Total Time: 6.0756 sec
⚡ Max Publish Rate: 8229.64 messages/sec
✅ Speed Test Completed Successfully!

## NUM_MESSAGES = 100000 
➜  mqtt_sim git:(main) ✗ py test_mqtt_speed.py 

🚀 Starting MQTT Speed Test...

📡 Subscribed to topic: sensor/accelerometer

📊 Sent: 100000, Received: 100000
⏱️ Total Time: 7.1307 sec
⚡ Max Publish Rate: 14023.80 messages/sec
✅ Speed Test Completed Successfully!


### Interpretation
Increasing the mqtt buffer size from 50k to 100k takes insures all messages are delivered.
/opt/homebrew/etc/mosquitto/mosquitto.conf
max_queued_messages 100000

It's unclear why the publish rate is higher with the higher messages value:
NUM_MESSAGES = 100000  
(not a problem)

So to be clear, with too small a buffer value either the broker is unable to publish the messages quickly enough or the subscriber is able to consume the messages quickly enough.