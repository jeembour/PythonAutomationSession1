import unittest

from selenium import webdriver


class LogInTest(unittest.TestCase):
    def login(self):
        browser = webdriver.Chrome(executable_path="browser/chromedriver.exe")
        browser.get("https:")


if __name__ == '__main__':
    unittest.main()
