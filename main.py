#!/usr/bin/env python3
"""
Keyboard Checker - Listens for keyboard presses and outputs them to terminal

This script uses pynput which provides cross-platform keyboard monitoring.
On Windows, pynput uses Windows API (SetWindowsHookEx) for low-level keyboard hooks.
On Linux, it uses X11 or evdev.

For more direct Windows API access, see:
- windows_api_version.py (direct ctypes Windows API calls)
- keyboard_lib_version.py (keyboard library alternative)
"""

from pynput import keyboard
import sys

def on_press(key):
    """Callback function called when a key is pressed"""
    try:
        if hasattr(key, 'char') and key.char is not None:
            # Regular character key
            print(f"Key pressed: '{key.char}'")
        else:
            # Special key (like space, enter, shift, etc.)
            key_name = str(key).replace('Key.', '')
            print(f"Special key pressed: {key_name}")
    except AttributeError:
        # Handle any edge cases
        print(f"Key pressed: {key}")

def on_release(key):
    """Callback function called when a key is released"""
    # Exit on ESC key
    if key == keyboard.Key.esc:
        print("\nESC pressed. Exiting...")
        return False

def main():
    """Main function to start the keyboard listener"""
    print("Keyboard Checker Started!")
    print("Press any key to see output. Press ESC to exit.")
    print("-" * 50)
    
    try:
        # Start the keyboard listener
        with keyboard.Listener(
            on_press=on_press,
            on_release=on_release
        ) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user (Ctrl+C)")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print("Keyboard listener stopped.")

if __name__ == "__main__":
    main()
