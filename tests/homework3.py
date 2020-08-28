import time
import unittest

from selenium.common.exceptions import NoSuchElementException



from selenium import webdriver

class Login(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome("../browsers/chromedriver")
        self.browser.get('http://hrm-online.portnov.com/')

    def tearDown(self) -> None:
        self.browser.quit()


    def test_homework3(self):
        browser = self.browser

        browser.find_element_by_id("txtUsername").send_keys("admin")
        browser.find_element_by_id("txtPassword").send_keys("password")
        browser.find_element_by_id("btnLogin").click()
        time.sleep(3)
        browser.find_element_by_id("empsearch_supervisor_name").send_keys("Bob Boss")
        browser.find_element_by_id("searchBtn").click()
        browser.find_element_by_xpath("//*[@id='resultTable']/tbody/tr[2]/td[3]/a").click()

        try:
         browser.find_element_by_id("tblAttachments").is_displayed()
        except NoSuchElementException:
            print("No resume is attached")






if __name__ == '__main__':
    unittest.main()
