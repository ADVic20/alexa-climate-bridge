# ❄️ Alexa Climate Bridge

**Advanced climate bridge between Home Assistant and Amazon Alexa.**

Alexa Climate Bridge is a Home Assistant custom integration that allows advanced control of Alexa-compatible climate devices directly from Home Assistant.

It is designed for devices that work correctly inside the Amazon Alexa ecosystem but have limited or no native support in Home Assistant.

The integration creates a native Home Assistant climate entity, allowing control through dashboards, automations, scripts, and voice assistants.

---

# ✨ Features

🌡️ **Home Assistant Climate Entity**  
Creates a native climate device inside Home Assistant.

🔄 **Bidirectional Synchronization**  
Keeps climate states synchronized between Home Assistant and Alexa.

⚡ **Real-Time Updates**  
Fast updates when temperature, power, or modes change.

🏠 **Native Home Assistant Integration**  
No YAML configuration required.

❄️ **HVAC Modes Support**  
Supports available climate modes depending on the device.

🌬️ **Fan Speed Control**  
Control supported fan modes.

🎯 **Target Temperature Control**  
Set desired temperature directly from Home Assistant.

🔌 **Automation Ready**  
Works with:
- Automations
- Scripts
- Scenes
- Dashboards
- Voice assistants

---

# 🚀 Supported Features

| Feature | Support |
|---|---|
| Power ON/OFF | ✅ |
| Target Temperature | ✅ |
| Current Temperature | ✅ |
| HVAC Modes | ✅ |
| Fan Modes | ✅ |
| Preset Modes | ⚙️ Device dependent |
| Swing Mode | ⚙️ Optional |

---

# 📋 Requirements

Before installing:

- Home Assistant
- Amazon Alexa integration
- A supported Alexa climate device

Compatible with:

✅ Home Assistant OS  
✅ Home Assistant Container  
✅ Home Assistant Supervised  
✅ Home Assistant running in LXC  
✅ Home Assistant running in Virtual Machine  

---

# 📦 Installation

## Method 1 - Manual Installation

Download or clone the repository:

```bash
cd /config/custom_components

git clone https://github.com/ADVic20/AlexaClimateBridge.git

The final structure should look like:

custom_components
│
└── alexa_climate_bridge
    │
    ├── __init__.py
    ├── climate.py
    ├── config_flow.py
    ├── manifest.json
    └── ...

Restart Home Assistant:

Settings
 → System
 → Restart Home Assistant
Installation using VS Code / Code Server

If you use the Home Assistant VS Code add-on:

Open:

/config/custom_components/

Clone the repository:

git clone https://github.com/ADVic20/AlexaClimateBridge.git

or copy the integration folder manually.

Verify that the folder name matches the integration:

/config/custom_components/alexa_climate_bridge

Restart Home Assistant.

⚙️ Configuration

After installation:

Go to:

Settings
 → Devices & Services
 → Add Integration

Search for:

Alexa Climate Bridge

Follow the setup wizard.

No YAML configuration is required.

🏠 Home Assistant Entity

After setup, Home Assistant creates a climate entity:

Example:

climate.living_room_ac

The entity can be used in:

Lovelace dashboards
Automations
Scripts
Scenes

Example:

service: climate.set_temperature
target:
  entity_id: climate.living_room_ac
data:
  temperature: 23
🏗️ Architecture
Amazon Alexa
      │
      ▼
Alexa Climate Bridge
      │
      ▼
Home Assistant
      │
      ▼
Automations / Dashboard / Voice Control
🔄 Updating

To update the integration:

Open the integration folder:

cd /config/custom_components/alexa_climate_bridge

Download the latest changes:

git pull

Restart Home Assistant.

🛣️ Roadmap

Future improvements:

 Multiple climate devices
 Automatic device discovery
 Improved device compatibility
 More preset modes
 Advanced diagnostics
 Better error reporting
 HACS support
🤝 Contributing

Contributions are welcome.

If you find a bug or have an idea:

Open an issue
Describe the problem
Provide logs if possible

Pull requests are welcome.

📄 License

MIT License

👨‍💻 Credits

Created by ADVic20

⭐ If this project helps your Home Assistant setup, consider giving it a star.
