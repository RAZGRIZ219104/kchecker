#!/usr/bin/env python3
"""
Windows API Level Keyboard Event Listener
This version uses ctypes to directly call Windows API functions for low-level keyboard hooks
"""

import sys
import ctypes
from ctypes import wintypes
import ctypes.wintypes

# Windows API constants
WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_SYSKEYDOWN = 0x0104
WM_SYSKEYUP = 0x0105

# Windows API function signatures
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

# Define the KBDLLHOOKSTRUCT structure
class KBDLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("vkCode", wintypes.DWORD),      # Virtual key code
        ("scanCode", wintypes.DWORD),    # Hardware scan code
        ("flags", wintypes.DWORD),       # Event flags
        ("time", wintypes.DWORD),        # Timestamp
        ("dwExtraInfo", ctypes.POINTER(wintypes.ULONG))  # Extra info
    ]

# Hook procedure type
HOOKPROC = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)

# Virtual key code to name mapping (partial)
VK_CODES = {
    0x08: 'BACKSPACE', 0x09: 'TAB', 0x0D: 'ENTER', 0x10: 'SHIFT',
    0x11: 'CTRL', 0x12: 'ALT', 0x1B: 'ESC', 0x20: 'SPACE',
    0x21: 'PAGE_UP', 0x22: 'PAGE_DOWN', 0x23: 'END', 0x24: 'HOME',
    0x25: 'LEFT', 0x26: 'UP', 0x27: 'RIGHT', 0x28: 'DOWN',
    0x2E: 'DELETE', 0x5B: 'LEFT_WIN', 0x5C: 'RIGHT_WIN',
    # A-Z keys (0x41-0x5A)
    **{i: chr(i) for i in range(0x41, 0x5B)},
    # 0-9 keys (0x30-0x39)
    **{i: chr(i) for i in range(0x30, 0x3A)},
    # F1-F12 keys
    **{0x70 + i: f'F{i+1}' for i in range(12)},
}

class WindowsKeyboardListener:
    def __init__(self):
        self.hook_id = None
        
    def low_level_keyboard_proc(self, nCode, wParam, lParam):
        """Low-level keyboard hook procedure"""
        if nCode >= 0:
            # Get keyboard data
            kb_struct = ctypes.cast(lParam, ctypes.POINTER(KBDLLHOOKSTRUCT)).contents
            
            # Determine event type
            if wParam == WM_KEYDOWN:
                event_type = "KEY_DOWN"
            elif wParam == WM_KEYUP:
                event_type = "KEY_UP"
            elif wParam == WM_SYSKEYDOWN:
                event_type = "SYS_KEY_DOWN"
            elif wParam == WM_SYSKEYUP:
                event_type = "SYS_KEY_UP"
            else:
                event_type = f"UNKNOWN({wParam})"
            
            # Get key information
            vk_code = kb_struct.vkCode
            scan_code = kb_struct.scanCode
            flags = kb_struct.flags
            
            # Get key name
            key_name = VK_CODES.get(vk_code, f"VK_{vk_code:02X}")
            
            # Print detailed information
            print(f"{event_type}: {key_name} (VK:{vk_code:02X}, SC:{scan_code:02X}, Flags:{flags:02X})")
            
            # Exit on ESC key press
            if vk_code == 0x1B and wParam == WM_KEYDOWN:
                print("ESC pressed. Exiting...")
                user32.PostQuitMessage(0)
                return 1
        
        # Call next hook
        return user32.CallNextHookExW(self.hook_id, nCode, wParam, lParam)
    
    def install_hook(self):
        """Install the low-level keyboard hook"""
        # Create hook procedure
        self.hook_proc = HOOKPROC(self.low_level_keyboard_proc)
        
        # Install hook
        self.hook_id = user32.SetWindowsHookExW(
            WH_KEYBOARD_LL,
            self.hook_proc,
            kernel32.GetModuleHandleW(None),
            0
        )
        
        if not self.hook_id:
            raise Exception("Failed to install keyboard hook")
        
        print("Windows API keyboard hook installed successfully!")
        return self.hook_id
    
    def uninstall_hook(self):
        """Uninstall the keyboard hook"""
        if self.hook_id:
            user32.UnhookWindowsHookEx(self.hook_id)
            self.hook_id = None
    
    def start_listening(self):
        """Start the message loop"""
        try:
            # Install hook
            self.install_hook()
            
            print("Listening for keyboard events at Windows API level...")
            print("Press ESC to exit")
            print("-" * 70)
            
            # Message loop
            msg = wintypes.MSG()
            while True:
                bRet = user32.GetMessageW(ctypes.byref(msg), None, 0, 0)
                if bRet == 0 or bRet == -1:  # WM_QUIT or error
                    break
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageW(ctypes.byref(msg))
                
        except KeyboardInterrupt:
            print("\nInterrupted by user")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.uninstall_hook()
            print("Keyboard hook uninstalled")

def main():
    """Main function - only works on Windows"""
    if sys.platform != "win32":
        print("This Windows API version only works on Windows!")
        print("Use the regular pynput version (main.py) on other platforms.")
        return
    
    print("Windows API Level Keyboard Listener")
    print("This version provides low-level access to keyboard events")
    
    listener = WindowsKeyboardListener()
    listener.start_listening()

if __name__ == "__main__":
    main()
