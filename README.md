# dev-toolkit-60

A Python autoclicker built for developers and QA engineers who need reliable mouse automation during testing and repetitive workflows. It delivers precise timing control with minimal overhead and built-in safeguards.

## Features

- Millisecond-accurate click intervals with optional human-like jitter
- Support for left, right, and middle mouse buttons in single or double-click mode
- Global hotkeys for start, stop, and emergency halt without leaving the target window
- Automatic session logging with click count, duration, and average rate

## Installation

```bash
git clone https://github.com/Developer/dev-toolkit-60.git
cd dev-toolkit-60
pip install -r requirements.txt
```

## Usage

Run from the command line with your desired parameters:

```bash
python autoclicker.py --clicks 800 --interval 0.08 --button left
```

Press the configured hotkey (default F7) to begin. Press F8 at any time to stop immediately.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)