# Introduction
This project protoypes MQTT messages simulation and a production CI / CD pipeline using GitHub actions.

It installs a Mosqito MQTT broker, publishes messages on a topic, and subscribes to messages  on the topic. Then, it tests the messages are sent.

Github actions file: `.github/workflows/mqtt-test.yml`

# Install (MacOS)
## Python Packages
`pip install -r requirements.txt`

## MQTT Broker
```
brew install mosquitto
brew services start mosquitto
```

# Run
`python test_mqtt.py`