# Introduction
This project protoypes MQTT messages simulation and a production CI / CD pipeline using GitHub Actions actions.

It installs a Mosqito MQTT broker, publishes messages on a topic, and subscribes to messages  on the topic. Then, it tests the messages are sent.

# Install (MacOS)
## Python Packages
pip install -r requirements.txt

## MQTT Broker
brew install mosquitto
brew services start mosquitto

# Run
pytest -s test_mqtt.py

# Notes
Since pytest automatically discovers test functions, test_mqtt.py doesn’t have a main() function. If you're running it directly with python test_mqtt.py, it won't execute anything because pytest is designed to discover and run functions prefixed with test_.

The code can be changed to be used without pytest by putting the asserts directly in main.

# More notes
Okay...so what to do..Simulate the messages..do The CI?CD