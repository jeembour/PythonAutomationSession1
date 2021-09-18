import unittest

import requests as requests
from selenium import webdriver


class LogInTest(unittest.TestCase):
    def test_valid_login(self):
  #      user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"
 #       header =  {'user-agent': user_agent}

        browser = webdriver.Chrome(executable_path='browser/chromedriver.exe')
        browser.get('http://hrm-online.portnov.com/symfony/web/index.php/auth/login')
        browser.find_element_by_xpath('//*[@id="txtUsername"]').send_keys('admin')

        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
