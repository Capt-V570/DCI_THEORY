import unittest
import os
from unittest.mock import patch
from delete_file import rm


class TestDeleteFile(unittest.TestCase):
    def test_deletion(self):
        # with patch('db.remove'):
        with patch("os.remove"):  # simulating this remove function in the os library
            output = rm("some_file.txt")
            self.assertEqual(output, "some_file.txt has been deleted!")

    # without patch (mocking)
    def test_rm(self):
        open("some_file.txt", "a")
        rm("some_file.txt")
        self.assertFalse(os.path.isfile("some_file.txt"), "failed to remove file")


if __name__ == "__main__":
    unittest.main()
