"""Configuration settings and environment loading."""
import os
import logging
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


def load_env(env_file: str = ".env") -> None:
    """
    Load environment variables from a .env file.
    
    Args:
        env_file: Path to the .env file (default is '.env')
    """
    if not os.path.exists(env_file):
        logger.debug("Environment file %s not found.", env_file)
        return
        
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()
            except ValueError:
                logger.warning("Invalid line in %s: %s", env_file, line)


@dataclass
class MQTTSettings:
    """MQTT connection settings."""
    broker: str = os.getenv("MQTT_BROKER", "test.mosquitto.org")
    port: int = int(os.getenv("MQTT_PORT", "1883"))
    topic: str = os.getenv("MQTT_TOPIC", "nielit/rpi/sensor")
    username: Optional[str] = os.getenv("MQTT_USERNAME")
    password: Optional[str] = os.getenv("MQTT_PASSWORD")


@dataclass
class FlaskSettings:
    """Flask web server settings."""
    host: str = os.getenv("FLASK_HOST", "0.0.0.0")
    port: int = int(os.getenv("FLASK_PORT", "5000"))
    debug: bool = os.getenv("FLASK_DEBUG", "True").lower() in ("true", "1", "yes")
