import sys
import unittest
from unittest.mock import MagicMock

# ✅ MOCK GUI-dependent modules to avoid DISPLAY errors in CI
sys.modules['pynput'] = MagicMock()
sys.modules['pynput.keyboard'] = MagicMock()
sys.modules['pyautogui'] = MagicMock()
sys.modules['PIL.ImageGrab'] = MagicMock()

# ✅ Now safely import your main logic
from src import main

class TestKeyPress(unittest.TestCase):
    def test_key_1_pressed(self):
        mock_key = MagicMock()
        mock_key.char = '1'
        mock_key.vk = None  # top-row '1'

        # Patch GUI-related functions
        main.copy_image_to_clipboard = MagicMock()
        main.ImageGrab.grab = MagicMock(return_value=MagicMock())

        # Ensure screenshot variable is clear
        main.last_screenshot = '1.gif'

        # Call the function
        main.on_key_press(mock_key)

        self.assertIsNotNone(main.last_screenshot)
        print("✅ test_key_1_pressed passed.")

    def test_invalid_key(self):
        mock_key = MagicMock()
        mock_key.char = 'x'
        mock_key.vk = None

        main.last_screenshot = None
        main.on_key_press(mock_key)

        self.assertIsNone(main.last_screenshot)
        print("✅ test_invalid_key passed.")

if __name__ == '__main__':
    unittest.main()
