import unittest
from unittest.mock import patch
from delete_file import rm


class TestDeleteFile(unittest.TestCase):

    def test_deletion(self):
        with patch('os.remove'): # simulating this remove function in the os library
            output = rm('some_file.txt')
            self.assertEqual(output, 'some_file.txt has been deleted!')

if __name__ == '__main__':
    unittest.main()