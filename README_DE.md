**[🇬🇧  english version of this description](README.md)**

----

# Home Assistant Add-on: Truma InetBox Emulator

Dieses Home-Assistant-Add-on emuliert eine **Truma InetBox**, um eine **Truma Combi Heizung** über einen UART-LIN-Adapter zu steuern.  
Es basiert auf der Implementierung [inetbox.py](https://github.com/danielfett/inetbox.py) von [@danielfett](https://github.com/danielfett) und integriert sich nahtlos in Home Assistant über **MQTT Auto Discovery**.

Mit diesem Add-on kannst du dein Truma-Heizsystem direkt aus Home Assistant steuern – **ohne die originale Truma InetBox-Hardware** zu benötigen.

---

## ✨ Funktionen

- Emuliert eine Truma InetBox über UART (LIN-Bus-Adapter erforderlich)  
- Vollständige Integration in **Home Assistant** über **MQTT Auto Discovery**  
- Automatische Veröffentlichung von Geräten und Entitäten an deinen MQTT-Broker  
- Lokale Steuerung – keine Cloud oder externen Dienste erforderlich  
- Als **Home-Assistant-Add-on** umgesetzt für eine einfache Installation

---

## 🛠 Voraussetzungen

- **Home Assistant** (jede Installation mit Add-on-Unterstützung)  
- **MQTT-Broker** (z. B. [Mosquitto](https://github.com/home-assistant/addons/tree/master/mosquitto))  
- **UART-LIN-Adapter**, verbunden mit deiner Truma Combi Heizung  
- **Raspberry Pi** (das Add-on wurde bisher nur auf dem Raspberry Pi getestet und bestätigt)  
- Grundkenntnisse in der Konfiguration von Home Assistant und MQTT

---

## 🚀 Installation

1. Öffne in **Home Assistant**: **Einstellungen → Add-ons → Add-on-Store**  
2. Klicke oben rechts auf das **⋮ (Drei-Punkte-Menü)** und wähle **Repositories**  
3. Füge folgende Repository-URL hinzu:  
   `https://github.com/taucher4000/HA_InetBox`  
4. Kehre zum Add-on-Store zurück, suche **InetBox** und installiere es  
5. Klicke nach der Installation auf **Start**, um das Add-on zu starten  
6. *(Optional)* Prüfe den **Logs**-Tab, um einen erfolgreichen Start zu bestätigen

---

## 🔧 Konfiguration

Die Konfiguration erfolgt über den **Konfiguration**-Tab in den Add-on-Einstellungen.  
Nachfolgend findest du alle verfügbaren Optionen und ihre Bedeutung:

| Option | Typ | Standard | Beschreibung |
|------|-----|----------|--------------|
| `MQTTBroker` | `string` | `core-mosquitto` | Hostname oder Servicename deines MQTT-Brokers. Verwende `core-mosquitto`, wenn du das Home-Assistant-MQTT-Add-on nutzt. |
| `MQTTUser` | `string` *(optional)* | `""` | MQTT-Benutzername, falls dein Broker eine Authentifizierung benötigt. Leer lassen, wenn nicht erforderlich. |
| `MQTTPassword` | `password` *(optional)* | `""` | MQTT-Passwort für den angegebenen Benutzer. |
| `SerialDevice` | `string` | `/dev/serial0` | Pfad zum seriellen Gerät, das mit deiner InetBox verbunden ist. Anpassen, falls ein anderer Port verwendet wird. |
| `DefaultTargetTempRoom` | `integer` | `22` | Standard-Zieltemperatur für den Raum (°C), die gesendet wird, wenn kein anderer Wert gesetzt ist. |
| `DebugApp` | `boolean` | `false` | Aktiviert Debug-Ausgaben für die Hauptanwendungslogik. |
| `DebugLin` | `boolean` | `false` | Aktiviert Debug-Ausgaben für die LIN-Kommunikation (Local Interconnect Network). |
| `DebugProtocol` | `boolean` | `false` | Aktiviert detaillierte Debug-Ausgaben des Protokolls. |
| `SetTime` | `boolean` | `true` | Wenn aktiviert, wird die Systemzeit der InetBox beim Start automatisch von Home Assistant gesetzt. |
| `Timezone` | `string` | `Europe/Berlin` | Zeitzonen-Override, wenn `SetTime` aktiviert ist |
| `Language` | `list` | `de` |  Sprache, die für die Namen und Werte der Entitäten verwendet wird. Mögliche Optionen: de (Deutsch), en (Englisch). |
| `Optimistic` | `boolean` | `false` | Aktiviere den MQTT Optimistic Mode. Wenn aktiviert, werden Befehle direkt als angenommen betrachtet, auch wenn keine Bestätigung vom Gerät empfangen wurde.

---

## 🔧 UART auf dem Raspberry Pi aktivieren

Um die UART-Schnittstelle mit deinem Raspberry Pi und dem LIN-Adapter zu nutzen, muss UART zuerst aktiviert werden:

1. Installiere das Add-on **HassOS SSH port 22222 Configurator** aus  
   [adamoutler/HassOSConfigurator](https://github.com/adamoutler/HassOSConfigurator)  
2. Aktiviere in deinem Home-Assistant-Profil den **Erweiterten Benutzermodus**  
   (ansonsten ist das Add-on nicht sichtbar)  
3. Kopiere deinen `id_rsa.pub`-Schlüssel in die Einstellungen des Configurators  
4. Führe den Configurator aus, deinstalliere ihn anschließend und starte das System neu  
5. Verbinde dich per SSH auf Port 22222 mit deinem Raspberry Pi, z. B.:  
   `ssh root@<deine-home-assistant-ip> -p 22222`  
6. Binde die Boot-Partition ein mit:  
   `mount /dev/mmcblk0p1 /mnt`  
7. Bearbeite die Datei `/mnt/config.txt` und füge folgende Zeile hinzu:  
   `enable_uart=1`  
8. Starte den Raspberry Pi neu, um die Änderungen zu übernehmen

---

## ⚠️ Haftungsausschluss

Dieses Add-on wird **ohne Gewähr** bereitgestellt und die Nutzung erfolgt **auf eigenes Risiko**.  
Ich übernehme keine Verantwortung für Schäden an Hardware, Software, Fahrzeug oder Heizsystem, die durch die Verwendung dieser Software entstehen könnten.

Bitte stelle sicher, dass du die Auswirkungen der Verbindung mit deinem Truma-Heizsystem vollständig verstehst, bevor du dieses Add-on verwendest.
