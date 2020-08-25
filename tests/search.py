import time
import unittest

from selenium import webdriver


class Search(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path='/Users/ellie/Selenium/Automation2020_Summer/browsers/chromedriver')
        self.browser.get('http://hrm-online.portnov.com/')

    def tearDown(self) -> None:
        self.browser.quit()

    def test_search_by_job_title(self):
        browser = self.browser

        browser.find_element_by_id("txtUsername").send_keys('admin')
        browser.find_element_by_id("txtPassword").send_keys('password')

        browser.find_element_by_id("btnLogin").click()

        time.sleep(3)




if __name__ == '__main__':
    unittest.main()
