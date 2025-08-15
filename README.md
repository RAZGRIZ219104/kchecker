# Keyboard Checker

A collection of Python scripts demonstrating different approaches to keyboard event monitoring, including Windows API level access.

## Files Overview

### 1. `main.py` - Cross-platform (Recommended)

- **Library**: `pynput`
- **Platform**: Windows, Linux, macOS
- **API Level**: Uses Windows API (`SetWindowsHookEx`) on Windows
- **Best for**: General use, cross-platform compatibility

### 2. `windows_api_version.py` - Direct Windows API

- **Library**: `ctypes` (direct Windows API calls)
- **Platform**: Windows only
- **API Level**: Direct low-level Windows API access
- **Best for**: Maximum control, detailed event information
- **Features**:
  - Virtual key codes
  - Hardware scan codes
  - Event flags and timestamps
  - System key events (Alt+Tab, etc.)

### 3. `keyboard_lib_version.py` - Alternative Library

- **Library**: `keyboard`
- **Platform**: Windows, Linux
- **API Level**: Windows API on Windows, evdev on Linux
- **Best for**: Simple API with low-level access

## Installation

### Quick Setup (Windows)

For Windows users, run the automated setup:

```cmd
setup_windows.bat
```

**Note: Run as Administrator for best results**

### Manual Installation (All Platforms)

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install all dependencies at once
pip install -r requirements.txt

# Or install individually:
pip install pynput
pip install keyboard  # For keyboard_lib_version.py
pip install pywin32   # For enhanced Windows support (optional)
```

### Windows-Specific Requirements

- **Python 3.7+** installed and in PATH
- **Administrator privileges** recommended for low-level hooks
- **Windows 10/11** (Windows 7+ should work but not tested)
- The `wversion.py` (Windows API version) uses only built-in libraries (`ctypes`)

## Usage

### Cross-platform version (Recommended)

```bash
python main.py
```

### Windows API version (Windows only)

```bash
python windows_api_version.py
```

### Keyboard library version

```bash
python keyboard_lib_version.py
```

## Windows API Details

On Windows, these scripts can access:

### Low-level Keyboard Hook (`WH_KEYBOARD_LL`)

- **Virtual Key Codes**: Hardware-independent key identifiers
- **Scan Codes**: Hardware-specific key codes
- **Event Types**:
  - `WM_KEYDOWN`: Regular key press
  - `WM_KEYUP`: Regular key release
  - `WM_SYSKEYDOWN`: System key press (Alt combinations)
  - `WM_SYSKEYUP`: System key release
- **Flags**: Additional event information
- **Timestamps**: Precise timing information

### Capabilities

- ✅ **Global hooks**: Capture keys from any application
- ✅ **System keys**: Alt+Tab, Windows key, etc.
- ✅ **Low-level access**: Hardware scan codes
- ✅ **Event filtering**: Can block or modify events
- ✅ **Detailed timing**: Precise timestamps

### Security Note

On Windows, low-level keyboard hooks require appropriate permissions and may be flagged by antivirus software as they can potentially be used for keylogging.

## Exit Instructions

- Press **ESC** to exit any of the scripts
- Or use **Ctrl+C** to interrupt

## Platform-Specific Notes

### Windows

- All three versions work
- May require administrator privileges for some system keys
- Antivirus software might flag the applications

### Linux

- `main.py` works with X11 or Wayland
- `keyboard_lib_version.py` may require sudo for low-level access
- `windows_api_version.py` will show an error message

### macOS

- `main.py` works but may require accessibility permissions
- Other versions are not compatible
