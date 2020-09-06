import time
import unittest
from selenium.webdriver.support.select import Select

from selenium.common.exceptions import NoSuchElementException



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome("../browsers/chromedriver")
        self.browser.get('http://hrm-online.portnov.com/')


    def tearDown(self) -> None:
        self.browser.quit()


    def test_homework3(self):
        browser = self.browser
        wait = WebDriverWait(browser, 3)


        wait.until(expected_conditions.presence_of_element_located([By.ID, "txtUsername"])).send_keys("admin")

        # browser.find_element_by_id("txtUsername").send_keys("admin")
        wait.until(expected_conditions.presence_of_element_located([By.ID, "txtPassword"])).send_keys("password")
        # browser.find_element_by_id("txtPassword").send_keys("password")
        # browser.find_element_by_id("btnLogin").click()
        wait.until(expected_conditions.presence_of_element_located([By.ID, "btnLogin"])).click()
        wait.until(expected_conditions.presence_of_element_located([By.XPATH, "//input[@id = 'empsearch_employee_name_empName'][@class = 'ac_input inputFormatHint']"]))
        wait.until(expected_conditions.presence_of_element_located([By.XPATH, "//select[@id = 'empsearch_job_title']"])).click()
        wait.until(expected_conditions.presence_of_element_located([By.XPATH, "//option[text() = 'QA Manager']"])).click()
        browser.find_element_by_xpath("//input[@id = 'searchBtn']").click()
        wait.until(expected_conditions.element_located_to_be_selected((By.XPATH, "//option[text()='QA Manager']")))
        list_of_rows = browser.find_elements_by_xpath("//*[@id='resultTable']/tbody/tr[*]")
        # print(len(list_of_rows))

        for each_row in list_of_rows:
            actual_value = each_row.find_element_by_xpath(".//td[5]").text
            self.assertEqual("QA Manager", actual_value)


if __name__ == '__main__':
    unittest.main()
