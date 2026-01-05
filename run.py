#!/inetbox/bin/python3
# -*- coding: utf-8 -*-
import json
import yaml
import sys
from pathlib import Path
from inetbox import truma_service
import random


CONFIG_FILE = Path("/etc/miqro.yml")
OPTIONS_FILE = Path("/data/options.json")
HEATER_DISCOVERY_DIR = Path("/src/mqtt_auto_discovery_objs/heater/")
AIRCON_DISCOVERY_DIR = Path("/src/mqtt_auto_discovery_objs/aircon/")
MIQRO_CONFIG = {
    "broker": {
        "host": "core-mosquitto",
        "port": 1883,
        "keepalive": 60
    },
    "auth": {
        "username": "",
        "password": ""
    },
    "log_level": "INFO",
    "services": {
        "truma": {
            "serial_device": "/dev/serial0",
            "default_target_temp_room": 22,
        }
    }
}

def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_yaml(data: dict, path: Path) -> None:
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False)


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

ha_options = load_json(OPTIONS_FILE)

MIQRO_CONFIG["broker"]["host"] = ha_options["MQTTBroker"]
MIQRO_CONFIG["auth"]["username"] = ha_options["MQTTUser"]
MIQRO_CONFIG["auth"]["password"] = ha_options["MQTTPassword"]
MIQRO_CONFIG["services"]["truma"]["default_target_temp_room"] = ha_options["DefaultTargetTempRoom"]
MIQRO_CONFIG["services"]["truma"]["serial_device"] = ha_options["SerialDevice"]
MIQRO_CONFIG["services"]["truma"]["debug_app"] = ha_options["DebugApp"]
MIQRO_CONFIG["services"]["truma"]["debug_lin"] = ha_options["DebugLin"]
MIQRO_CONFIG["services"]["truma"]["debug_protocol"] = ha_options["DebugProtocol"]
MIQRO_CONFIG["services"]["truma"]["set_time"] = ha_options["SetTime"]
MIQRO_CONFIG["services"]["truma"]["timezone_override"] = ha_options["Timezone"]
MIQRO_CONFIG["services"]["truma"]["language"] = ha_options["Language"]

save_yaml(MIQRO_CONFIG, CONFIG_FILE)

if __name__ == '__main__':
    sys.exit(truma_service.run())
