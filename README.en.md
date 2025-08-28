# War Thunder Voice Control 🎮🎤

[Русский](README.ru.md) | [Home](README.md)

Voice control system for War Thunder, written in Python. Control your game with natural voice commands for a more immersive and accessible experience.

## 🌟 Features

- **Voice commands**: Control various in-game actions with natural speech
- **Background noise calibration**: Automatically adapts to your environment for better recognition
- **Error handling**: Robust error handling for stable operation
- **Easy to use**: Simple commands in both Russian and English
- **Multilingual**: Russian and English languages supported
- **Custom actions**, including:
  - Rangefinder activation
  - Quick exit from game
  - Chat control
  - And much more!

## 🗂️ Project Structure

```
/ (root)
├── src/               # Source code
│   ├── main.py        # Main program file
│   └── utils/         # Utility modules
│       └── commands.py  # Command handlers
├── config/            # Configuration files
│   └── settings.json  # Key bindings
├── README.md          # Documentation
├── install.bat        # Installation script
└── start.bat          # Startup script
```

## 🛠️ Requirements

- Python 3.x
- SpeechRecognition library
- PyAudio
- keyboard library
- mouse library

## 📦 Installation

### Easy way (recommended):

1. Download and install [Python 3.x](https://www.python.org/downloads/)
2. Download this project ([download ZIP](https://github.com/frizzonje/WarthunderVoiceControl/archive/refs/heads/main.zip))
3. Unzip the archive
4. Run `install.bat`

### Setup and launch:

1. Open `config/settings.json` and set up key bindings to match your War Thunder controls
2. Start War Thunder
3. Run `start.bat`
4. Wait for background noise calibration (~2 seconds)
5. Start using voice commands!

⚠️ **Important**:
- Before first launch, check and edit `config/settings.json` so key bindings match your in-game settings!
- To change hotkeys, edit `config/settings.json`

### Advanced way (for developers):

```bash
# Clone the repository
git clone https://github.com/frizzonje/WarthunderVoiceControl.git

# Create and activate virtual environment
python -m venv myenv
myenv\Scripts\activate

# Install required packages
pip install SpeechRecognition pyaudio keyboard mouse

# Run the script
python main.py
```

## 🗣️ Available Commands

When started, the program will prompt you to select a language (Russian or English).
The system recognizes the following voice commands:

### 🎮 General commands
- "menu" - Open game menu
- "fire", "shoot", "attack" - Fire weapon
- "scope", "sniper mode" - Enable sniper mode
- "binoculars", "binocs" - Use binoculars
- "rage quit", "exit game" - Quick exit from game
- "exit program", "close program" - Close voice control program

### 🚗 Movement
- "forward", "move forward", "advance", "ahead" - Move forward
- "back", "backward", "reverse", "go back" - Move backward
- "left", "turn left", "go left" - Turn left
- "right", "turn right", "go right" - Turn right
- "straight", "center", "align" - Stop turning
- "stop", "halt", "hold" - Full stop
- "handbrake", "hand brake", "brake" - Use handbrake

### 🚜 Tank commands
- "smoke", "smoke screen", "deploy smoke" - Smoke screen
- "repair", "fix", "repair tank" - Repair
- "fire extinguisher", "extinguisher", "put out fire" - Fire extinguisher
- "artillery", "arty", "call artillery" - Call artillery
- "tow cable", "tow", "cable" - Tow cable
- "rangefinder", "range", "find range" - Rangefinder
- "thermal vision", "thermals" - Thermal vision
- "atgm", "guided missile" - Launch ATGM
- "shell one/two/three/four", "ammo one/two/three/four" - Select shell type

### ✈️ Aircraft commands
- "landing gear", "gear", "toggle gear" - Landing gear control
- "flaps", "toggle flaps" - Flaps control
- "air brake", "airbrake", "speed brake" - Air brake
- "radar lock", "lock radar", "radar target" - Radar target lock
- "missile lock", "lock missile", "target lock" - Missile target lock
- "launch missile", "fire missile", "missiles" - Launch missiles
- "weapon select", "select weapon", "change weapon" - Weapon selection
- "drop bombs", "bombs", "release bombs" - Drop bombs

### 🛩️ Drone commands
- "drone toggle", "drone launch/return" - Launch/return drone
- "drone lock", "drone target" - Lock target with drone
- "drone orbit", "drone circle" - Orbit mode
- "drone mark", "mark target" - Mark target with drone

## 📋 Development Plans

- 🚢 **Naval Support**: Adding voice commands for naval vessels control
- 🌐 **New Languages**: Expanding language support for more players worldwide
- 🎯 **Recognition Improvements**: Optimizing performance with different accents and recording conditions

## ⚠️ Note

- Make sure your microphone is properly configured and working
- The program needs appropriate permissions to control the keyboard

## 💻 For Developers
Command handling logic is in `src/utils/commands.py`. You can easily add new commands or modify existing ones.
