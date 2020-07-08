import unittest
import tool3


class TestMyFunctions(unittest.TestCase):
    def test_create_ip_list(self):
        expected = ["192.168.1.1", "192.168.1.2"]
        self.assertEqual(tool3.create_ip_list("192.168.1.", 3), expected)
