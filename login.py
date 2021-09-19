import time
import unittest

import requests as requests

from selenium import webdriver


class LogInTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path='browser/chromedriver.exe')
        self.browser.get('http://hrm-online.portnov.com/symfony/web/index.php/auth/login')

    def tearDown(self) -> None:
        self.browser.quit()

    def test_valid_login(self):
  #      user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"
 #       header =  {'user-agent': user_agent}
        browser = self.browser
        browser.find_element_by_xpath('//*[@id="txtUsername"]').send_keys('admin')
        browser.find_element_by_id('txtPassword').send_keys('password')
        browser.find_element_by_css_selector('#btnLogin').click()
        time.sleep(3)
        url = browser.current_url
        welcome_message = browser.find_element_by_xpath('//*[@id="welcome"]').text
        self.assertTrue(url.endswith('viewEmployeeList'))
        self.assertEqual('Welcome Admin', welcome_message)

if __name__ == '__main__':
    unittest.main()
