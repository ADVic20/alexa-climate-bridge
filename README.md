Alexa Climate Bridge

Bridge between Home Assistant and Amazon Alexa for advanced climate control.

Alexa Climate Bridge allows Home Assistant to control climate devices exposed through Amazon Alexa by providing a simple MQTT bridge and bidirectional synchronization.

It is designed for devices that are fully supported in the Alexa ecosystem but have limited or no native integration with Home Assistant.

Features
🌡️ Control Alexa climate devices from Home Assistant.
🔄 Bidirectional synchronization.
⚡ Real-time state updates.
🏠 MQTT Auto Discovery for Home Assistant.
❄️ Supports HVAC modes.
🌬️ Supports fan speed.
🎯 Supports target temperature.
🔌 Lightweight and easy to install.
🐧 Optimized for Linux and Proxmox.
Supported Features
Power On / Off
HVAC Mode
Target Temperature
Current Temperature
Fan Mode
Preset Modes (when supported)
Swing Mode (optional)
Requirements
Home Assistant
Amazon Alexa
MQTT Broker (Mosquitto recommended)
Linux (Debian/Ubuntu/Proxmox)
Installation

Clone the repository:

git clone https://github.com/<username>/AlexaClimateBridge.git
cd AlexaClimateBridge

Run the installer:

chmod +x install.sh
sudo ./install.sh
MQTT Topics

Example:

alexa_climate/living_room/state
alexa_climate/living_room/command
alexa_climate/living_room/availability
Home Assistant

The bridge supports MQTT Discovery.

After installation, Home Assistant automatically creates the climate entity.

Example:

climate.living_room_ac

No manual YAML configuration is required.

Configuration

Example:

DEVICE_NAME=Living Room AC

MQTT_HOST=192.168.1.10
MQTT_PORT=1883
MQTT_USER=mqtt
MQTT_PASSWORD=password

ALEXA_DEVICE=Living Room AC
Example Automations

Turn on the air conditioner when the temperature exceeds 28°C.

trigger:
  - platform: numeric_state
    entity_id: sensor.living_room_temperature
    above: 28

action:
  - service: climate.turn_on
    target:
      entity_id: climate.living_room_ac
Architecture
Amazon Alexa
       │
       ▼
Alexa Climate Bridge
       │
       ▼
     MQTT
       │
       ▼
Home Assistant
Roadmap
Support multiple climate devices.
Automatic device discovery.
Preset modes.
Swing mode.
Fan speed presets.
Better logging.
Docker support.
Home Assistant Add-on.
License

MIT License

Contributing

Pull Requests are welcome.

For major changes, please open an issue first.

Credits

Created by ADVic20
