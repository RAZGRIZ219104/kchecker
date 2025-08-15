#!/usr/bin/env python3
"""
Alternative keyboard listener using the 'keyboard' library
This library also uses Windows API on Windows for low-level hooks
"""

import sys

try:
    import keyboard
except ImportError:
    print("The 'keyboard' library is not installed.")
    print("Install it with: pip install keyboard")
    sys.exit(1)

def on_key_event(event):
    """Handle keyboard events"""
    if event.event_type == keyboard.KEY_DOWN:
        print(f"Key pressed: {event.name} (scan_code: {event.scan_code})")
        
        # Exit on ESC
        if event.name == 'esc':
            print("ESC pressed. Exiting...")
            return False
    elif event.event_type == keyboard.KEY_UP:
        print(f"Key released: {event.name} (scan_code: {event.scan_code})")

def main():
    """Main function using keyboard library"""
    print("Keyboard Library - Low-level keyboard listener")
    print("This uses Windows API on Windows, evdev on Linux")
    print("Press ESC to exit")
    print("-" * 50)
    
    try:
        # Hook all keyboard events
        keyboard.hook(on_key_event)
        
        # Keep the program running
        keyboard.wait('esc')
        
    except Exception as e:
        print(f"Error: {e}")
        if "root" in str(e).lower() or "permission" in str(e).lower():
            print("On Linux, you may need to run with sudo for low-level access")
    
    print("Keyboard listener stopped.")

if __name__ == "__main__":
    main()
