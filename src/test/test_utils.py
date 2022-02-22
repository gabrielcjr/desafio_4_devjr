import unittest
from unittest import mock
import sys

sys.path.append("src")
from utils import utils


class TestUtils(unittest.TestCase):
    @mock.patch("os.system", return_value=0)
    def test_clear(self, mock_utils):
        print("test_clear")
        self.assertEqual(utils.clear(), 0)


if __name__ == "__main__":
    unittest.main()
