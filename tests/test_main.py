import unittest
from unittest.mock import MagicMock
from src import main
class TestKeyPress(unittest.TestCase):
    def test_key_1_pressed(self):
        # Mock a key with char '1'
        mock_key = MagicMock()
        mock_key.char = '1'
        mock_key.vk = None  # top-row '1'

        last_screenshot = "1.gif"  # reset
        main.copy_image_to_clipboard = MagicMock()  # avoid clipboard use
        main.ImageGrab.grab = MagicMock(return_value=MagicMock())  # mock screenshot

        main.on_key_press(mock_key)

        self.assertIsNotNone(last_screenshot)
        print("✅ test_key_1_pressed passed.")

    def test_invalid_key(self):
        # Mock a key with char 'x'
        mock_key = MagicMock()
        mock_key.char = 'x'
        mock_key.vk = None

        last_screenshot = None
        main.on_key_press(mock_key)

        self.assertIsNone(last_screenshot)
        print("✅ test_invalid_key passed.")


if __name__ == '__main__':
    unittest.main()
