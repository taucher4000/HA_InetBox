**[🇩🇪 Deutsche Version der Beschreibung](README_DE.md)**

---

# Home Assistant Add-on: Truma InetBox Emulator

This Home Assistant add-on emulates a **Truma InetBox** to control a **Truma Combi Heater** via a UART LIN adapter.  
It is based on the [inetbox.py](https://github.com/danielfett/inetbox.py) implementation by [@danielfett](https://github.com/danielfett), and integrates seamlessly into Home Assistant through MQTT Auto Discovery.  

With this add-on, you can control your Truma heating system directly from Home Assistant, without needing the original Truma InetBox hardware.

---

## ✨ Features

- Emulates a Truma InetBox over UART (LIN bus adapter required).  
- Full integration with **Home Assistant** via **MQTT Auto Discovery**.  
- Automatic device and entity publishing to your MQTT broker.  
- Local control – no cloud or external services required.  
- Built as a **Home Assistant Add-on** for easy deployment.

---

## 🛠 Requirements

- **Home Assistant** (any installation that supports add-ons).  
- **MQTT Broker** (e.g., [Mosquitto](https://github.com/home-assistant/addons/tree/master/mosquitto)).  
- **UART LIN adapter** connected to your Truma Combi Heater.  
- **Raspberry Pi** (the add-on is currently tested and confirmed working only on Raspberry Pi).  
- Basic familiarity with configuring Home Assistant and MQTT.  

---

## 🚀 Installation

1. In **Home Assistant**, go to **Settings → Add-ons → Add-on Store**  
2. Click the **⋮ (three dots)** menu in the top right and choose **Repositories**  
3. Add the repository URL: `https://github.com/taucher4000/HA_InetBox`
4. Return to the Add-on Store, locate **InetBox**, and install it  
5. After installation, click **Start** to launch the add-on  
6. *(Optional)* Check the **Logs** tab to verify successful startup

---

## 🔧 Configuration

The add-on can be configured via the **Configuration** tab in the Add-on settings.  
Below is a list of all available options and their meaning.

| Option | Type | Default | Description |
|--------|------|----------|-------------|
| `MQTTBroker` | `string` | `core-mosquitto` | Hostname or service name of your MQTT broker. Use `core-mosquitto` if using the Home Assistant MQTT add-on. |
| `MQTTUser` | `string` *(optional)* | `""` | MQTT username if your broker requires authentication. Leave empty if not needed. |
| `MQTTPassword` | `password` *(optional)* | `""` | MQTT password for the given user. |
| `SerialDevice` | `string` | `/dev/serial0` | Path to the serial device connected to your InetBox. Adjust if using a different port. |
| `DefaultTargetTempRoom` | `integer` | `22` | Default room temperature target (°C) sent to the device if no specific value is set. |
| `DebugApp` | `boolean` | `false` | Enables debugging output for the main application logic. |
| `DebugLin` | `boolean` | `false` | Enables debug output for LIN (Local Interconnect Network) communication. |
| `DebugProtocol` | `boolean` | `false` | Enables detailed protocol debugging output. |
| `SetTime` | `boolean` | `true` | If enabled, automatically sets the InetBox system time from Home Assistant at startup. |
| `Timezone` | `string` | `Europe/Berlin` | Time zone override if SetTime is enabled
| `Language` | `list` | `de` |  language used for the entity names and values. Possible Options: de (german), en (english). |

---

## 🔧 Enabling UART on Raspberry Pi

To use the UART interface with your Raspberry Pi and the LIN adapter, you must first enable UART support:  

1. Install the **HassOS SSH port 22222 Configurator** add-on from [adamoutler/HassOSConfigurator](https://github.com/adamoutler/HassOSConfigurator).  
2. In your Home Assistant profile settings, enable **Advanced User mode** (otherwise the add-on will not be visible).  
3. Copy your `id_rsa.pub` key into the configurator settings.  
4. Run the configurator, then uninstall it after execution and reboot your system.  
5. Connect to your Raspberry Pi using SSH on port 22222, for example:  
   `ssh root@<your-home-assistant-ip> -p 22222`  
6. Mount the boot partition with:  
   `mount /dev/mmcblk0p1 /mnt`  
7. Edit the file `/mnt/config.txt` and add the line:  
   `enable_uart=1`  
8. Reboot the Raspberry Pi to apply the changes.  

---

## ⚠️ Disclaimer

This add-on is provided **as-is** and is used entirely **at your own risk**.  
I am not responsible for any damage to your hardware, software, vehicle, or heating system that may result from using this software.  

Please ensure you fully understand the implications of connecting to your Truma heating system before use.  
