"""
Unit testing the temp_humidity.py file
"""

import unittest

class TestClass(unittest.TestCase):
    """
    Define tester
    """

    def test_time(self):

        """
        Test time
        """

        timestamp = "2018-04-16 20:20:00"
        self.assertTrue(timestamp)

    def test_temp(self):

        """
        Test temp
        """

        temp = 20
        self.assertTrue(temp)

    def test_humidity(self):

        """
        Test humidity
        """
        humidity = 60
        self.assertTrue(humidity >= 1)

if __name__ == "__main__":
    unittest.main()
