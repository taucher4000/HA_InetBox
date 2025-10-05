#!/inetbox/bin/python3
# -*- coding: utf-8 -*-
import json
import yaml
import sys
import os
from pathlib import Path
from inetbox import truma_service
from paho.mqtt import client as mqtt_client
import random


CONFIG_FILE = Path("/etc/miqro.yml")
OPTIONS_FILE = Path("/data/options.json")
DISCOVERY_DIR = Path("/inetbox/mqtt_auto_discovery_objs/")


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_yaml(data: dict, path: Path) -> None:
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False)


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)



miqro_config = load_yaml(CONFIG_FILE)
ha_options = load_json(OPTIONS_FILE)

miqro_config["broker"]["host"] = ha_options["MQTTBroker"]
miqro_config["auth"]["username"] = ha_options["MQTTUser"]
miqro_config["auth"]["password"] = ha_options["MQTTPassword"]
miqro_config["services"]["truma"]["default_target_temp_room"] = ha_options["DefaultTargetTempRoom"]
miqro_config["services"]["truma"]["serial_device"] = ha_options["SerialDevice"]

save_yaml(miqro_config, CONFIG_FILE)

client = mqtt_client.Client(f'publish-{random.randint(0, 1000)}')
client.username_pw_set(ha_options["MQTTUser"], ha_options["MQTTPassword"])
client.connect(ha_options["MQTTBroker"])

for filepath in DISCOVERY_DIR.rglob("*.json"):
    device_class, topic_id = filepath.stem.split("-", 1)
    topic = f"homeassistant/{device_class}/truma_{topic_id}__1/config"

    with filepath.open("r", encoding="utf-8") as f:
        payload = json.load(f)

    payload["device"] = {
        "identifiers": ["truma_control"],
        "name": "Truma Control",
        "model": "Combi",
        "manufacturer": "Truma"
    }

    client.publish(topic, json.dumps(payload), retain=True)

client.disconnect()

if __name__ == '__main__':
    sys.exit(truma_service.run())
