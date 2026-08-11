import json
import logging
import os
from typing import Callable, Dict, Any, Optional
import paho.mqtt.client as mqtt

logger = logging.getLogger(__name__)

class MQTTPublisher:
    """
    A simple MQTT publisher for sending sensor data.
    """
    
    def __init__(self, broker: Optional[str] = None, port: Optional[int] = None, topic: Optional[str] = None):
        """
        Initialize the MQTT publisher.
        Defaults are loaded from environment variables if not provided.
        """
        self.broker = broker or os.getenv('MQTT_BROKER', 'localhost')
        self.port = port or int(os.getenv('MQTT_PORT', '1883'))
        self.topic = topic or os.getenv('MQTT_TOPIC', 'nielit/sensors')
        
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        logger.info(f"Initialized MQTT Publisher (Broker: {self.broker}:{self.port}, Topic: {self.topic})")
        
    def connect(self) -> None:
        """Connect to the MQTT broker."""
        logger.info(f"Connecting to MQTT broker {self.broker}:{self.port}")
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()
        
    def disconnect(self) -> None:
        """Disconnect from the MQTT broker."""
        logger.info("Disconnecting from MQTT broker")
        self.client.loop_stop()
        self.client.disconnect()
        
    def publish(self, payload: Dict[str, Any]) -> None:
        """
        Publish a JSON payload to the topic.
        
        Args:
            payload (Dict[str, Any]): Dictionary of data to publish.
        """
        msg = json.dumps(payload)
        logger.debug(f"Publishing to {self.topic}: {msg}")
        self.client.publish(self.topic, msg)
        
    def __enter__(self):
        self.connect()
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()


class MQTTSubscriber:
    """
    A simple MQTT subscriber for receiving commands or data.
    """
    
    def __init__(self, broker: Optional[str] = None, port: Optional[int] = None, 
                 topic: Optional[str] = None, on_message_callback: Optional[Callable] = None):
        """
        Initialize the MQTT subscriber.
        """
        self.broker = broker or os.getenv('MQTT_BROKER', 'localhost')
        self.port = port or int(os.getenv('MQTT_PORT', '1883'))
        self.topic = topic or os.getenv('MQTT_TOPIC', 'nielit/#')
        self.callback = on_message_callback
        
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        
        logger.info(f"Initialized MQTT Subscriber (Broker: {self.broker}:{self.port}, Topic: {self.topic})")
        
    def _on_connect(self, client, userdata, flags, reason_code, properties):
        logger.info(f"Connected to MQTT broker with result code {reason_code}")
        client.subscribe(self.topic)
        
    def _on_message(self, client, userdata, msg):
        payload = msg.payload.decode('utf-8')
        logger.debug(f"Received message on {msg.topic}: {payload}")
        if self.callback:
            self.callback(msg.topic, payload)
            
    def connect(self) -> None:
        """Connect to the MQTT broker."""
        logger.info(f"Connecting to MQTT broker {self.broker}:{self.port}")
        self.client.connect(self.broker, self.port, 60)
        
    def disconnect(self) -> None:
        """Disconnect from the MQTT broker."""
        logger.info("Disconnecting from MQTT broker")
        self.client.disconnect()
        
    def start(self) -> None:
        """Start the background network loop."""
        self.client.loop_start()
        
    def stop(self) -> None:
        """Stop the background network loop."""
        self.client.loop_stop()
        
    def __enter__(self):
        self.connect()
        self.start()
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.stop()
        self.disconnect()
