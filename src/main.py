# pip install pyautogui pynput pillow pywin32

import pyautogui
import threading
import time
from pynput import keyboard
from PIL import ImageGrab
import os
import io
import platform

if platform.system() == "Windows":
    import win32clipboard

def copy_image_to_clipboard(img):
    output = io.BytesIO()
    img.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()
    print("✅ Screenshot copied to clipboard.")

def on_key_press(key):
    try:
        if (hasattr(key,'char')) and key.char=='1' or (hasattr(key,'vk') and key.vk==97):
            print(f"Press Key 1. Key {key} pressed. Capturing screen...")
            screenshot = ImageGrab.grab()
            screenshot.show()  # Optional: open image preview
            copy_image_to_clipboard(screenshot)

            # OPTIONAL: Simulate Ctrl+V (paste) - can be dangerous
            # pyautogui.hotkey('ctrl', 'v')
        else:
            print(f" Incorrect Key {key} pressed. Please Press '1' or '2' only.")
    except Exception as e:
        print(f"❌ Error handling key: {key} → {e}")

    return False  # Stop listener after one press

def run_bot():
    print("🔹 Bot running...")
    print("🔹 Press '1' (top row) or Numpad 1 to capture and copy screenshot..")
    print("🔹 Press '2' (top row) or Numpad 2 to delete last screenshot.")
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    run_bot()
