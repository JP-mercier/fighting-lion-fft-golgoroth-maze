# Fighting Lion FFT - Golgoroth's Maze Auto-Aim

An automated aiming script for Destiny 2's Fighting Lion exotic grenade launcher using Fast Fourier Transform (FFT) image correlation for precise targeting in Golgoroth's Maze encounters.

## ⚠️ Requirements

- **1440p Monitor (2560x1440)** - Script is calibrated for this resolution
- Windows 10/11
- Python 3.7+
- Destiny 2 running in windowed or borderless windowed mode

## 🎯 Features

- **FFT-based Image Correlation**: Uses Fast Fourier Transform for precise crosshair tracking
- **Real-time Aim Correction**: Automatically adjusts mouse position based on visual feedback
- **Golgoroth's Maze Optimized**: Specifically designed for the maze encounter mechanics
- **Hotkey Controls**: Press 'h' to start/stop the script
- **Firewall Integration**: Blocks Destiny 2 networking ports for solo play

## 🎥 Demo Video

[![Fighting Lion FFT Auto-Aim Demo](https://img.youtube.com/vi/Vx1zXPyDAZ0/0.jpg)](https://www.youtube.com/watch?v=Vx1zXPyDAZ0)

*Click the thumbnail above to watch the demo video*

## 📋 Installation

1. Install required Python packages:
```bash
pip install numpy pillow keyboard scipy pywin32 pyautogui
```

2. Clone this repository:
```bash
git clone https://github.com/yourusername/fighting-lion-fft-golgoroth-maze.git
cd fighting-lion-fft-golgoroth-maze
```

3. Run the script:
```bash
python fighting_lion_auto.py
```

## 🎮 Usage

1. Launch Destiny 2 and navigate to Golgoroth's Maze encounter
2. Position your character at the designated spot
3. Run the script and press 'h' to start
4. The script will automatically:
   - Take a reference screenshot
   - Continuously shoot and adjust aim
   - Use FFT correlation to track crosshair position
   - Apply micro-adjustments for optimal accuracy

## 🔧 Configuration

The script includes several configurable parameters:

- **Screen Area**: Currently set for 200x200 pixel region around center
- **Timing**: 3.7-second wait between shots
- **Coordinates**: Adjustable for different screen positions

## ⚠️ Disclaimer

This script is for educational purposes only. Use at your own risk and ensure compliance with Destiny 2's Terms of Service and your local laws regarding automation software.

## 🛠️ Technical Details

The script uses:
- **scipy.signal.fftconvolve** for Fast Fourier Transform correlation
- **PIL ImageGrab** for screen capture
- **win32api** for mouse control
- **numpy** for image processing

## 📝 License

This project is open source. Please use responsibly and in accordance with game terms of service.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the script's accuracy and functionality.
