import unittest

from selenium import webdriver

"""
class CalcSecondsTestCase(unittest.TestCase):
    def test_zeros_and_minutes(self):
        minutes = 8
        hours = 3
        expected_seconds = (minutes*60)+(hours*3600)
        actual_seconds = self.get_seconds(minutes, hours)
        self.assertEqual(expected_seconds, actual_seconds)  # add assertion here

    def get_seconds(self, minutes, hours):
        return  (minutes*60)+(hours*60*60)
"""
class Login (unittest.TestCase):
    def test_valid_login(self):
        browser = webdriver.Chrome(executable_path="browser/chromedriver.exe")

 #       self.assertEqual(True, False)
if __name__ == '__main__':
    unittest.main()
