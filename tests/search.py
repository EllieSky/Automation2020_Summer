import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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

        WebDriverWait(browser, 3).until(expected_conditions.presence_of_element_located(
            [By.CSS_SELECTOR, "#empsearch_employee_name_empName.inputFormatHint"]))

        WebDriverWait(browser, 3).until(
            expected_conditions.presence_of_element_located([By.ID, "empsearch_job_title"])).click()

        # WebDriverWait will "find" the webelement just like find_element_by_id
        # browser.find_element_by_id("empsearch_job_title").click()

        browser.find_element_by_xpath('//option[text()="QA Manager"]').click()

        time.sleep(1)
        browser.find_element_by_id("searchBtn").click()

        time.sleep(3)

        list_of_rows = browser.find_elements_by_xpath("//tbody/tr")

        for single_row in list_of_rows:
            actual_job_title = single_row.find_element_by_xpath(".//td[5]").text
            self.assertEqual("QA Manager", actual_job_title)

# OR (another method of looping)
        for j in range(1, len(list_of_rows)+1):
            actual_job_title = browser.find_element_by_xpath(f"//tbody/tr[{j}]/td[5]").text
            self.assertEqual("QA Manager", actual_job_title)

if __name__ == '__main__':
    unittest.main()
