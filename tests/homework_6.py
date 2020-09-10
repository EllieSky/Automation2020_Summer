import unittest
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


# Using the python methods and examples discussed and created in class, complete the following test case:

class Homework6(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.get('http://hrm-online.portnov.com/')

    def tearDown(self) -> None:
        self.browser.quit()

    def login(self, username="admin", password="password"):
        browser = self.browser
        browser.find_element_by_id("txtUsername").send_keys(username)
        browser.find_element_by_id("txtPassword").send_keys(password)
        browser.find_element_by_id("btnLogin").click()
        WebDriverWait(browser, 3).until(expected_conditions.presence_of_element_located(
            [By.CSS_SELECTOR, "#empsearch_employee_name_empName.inputFormatHint"]))

    # 1)Login
    def test_sort_by_first_name_abc(self):
        browser = self.browser
        wait = WebDriverWait(browser, 3)
        self.login()
        # 2) Go to PIM tab
        # 3) Click on the "First (& Middle) Name" table header  -> this should result in the employees to be rearranged in alpha order by first name
        # 4) Verify that the names now appear in alpha order.
        sort_button = browser.find_element_by_xpath("//a[contains(text(),'First (& Middle) Name')]")
        button_abc = sort_button.click()
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "ASC")))
        #empsearch_employee_name_empName.inputFormatHint
        # result_button= browser.find_element_by_xpath("//a[@class='ASC']")
        # self.assertTrue(result_button.get_attribute("ASC"))
        column_of_first_name = list()
        column_of_first_name = browser.find_elements_by_xpath("//.//td[3]")
        previous_name = ""
        for single_name in column_of_first_name:
            # print(browser.find_element_by_xpath("//.//td[3]").text)
            #print(single_name.text)
            list1= list(single_name)
            print(len(column_of_first_name))
            #self.assertLessEqual(previous_name, single_name)


        # button_desc = browser.find_element_by_xpath("//a[contains(text(),'First (& Middle) Name')]").click()


    def test_sort_by_first_name_desc1(self):
        browser = self.browser
        wait = WebDriverWait(browser, 3)
        action = ActionChains(browser)
        self.login()
        sort_button = browser.find_element_by_xpath("//a[contains(text(),'First (& Middle) Name')]")
        button_desc = action.double_click(on_element=sort_button)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "DESC")))

    def test_sort_by_first_name_desc(self):
        browser = self.browser
        wait = WebDriverWait(browser, 3)
        action = ActionChains(browser)
        self.login()
        sort_button = browser.find_element_by_xpath("//a[contains(text(),'First (& Middle) Name')]").click()
        button_desc = browser.find_element_by_xpath("//a[@class='ASC']").click()
        # button_desc = action.double_click(on_element=sort_button)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "DESC")))
        # actual_result = browser.find_element_by_xpath("//a[@class='DESC']")
        column_of_first_name = list()
        column_of_first_name = browser.find_elements_by_xpath("//.//td[3]")

        for single_name in column_of_first_name:
            list_fn= (single_name.text)
            b = list_fn
            print(b[0:5])

            #list_adc = b[0]
            #self.assertGreaterEqual(list_adc,b)



# (For now do this only for the first page)
# Note: it is possible to have 2 or more of the same name, so names won't always be <, sometimes they may be ==.
# Hint: You will need to add a wait after step #3, to allow time for the sort to complete.
# Hint: To check that all first names are in alpha order, you will need to use a different assert than assertEqual(). Try using assertTrue or assertGreaterEqual / assertLessEqual.
# Hint: There is a way to compare 2 names without using index, or enumerate. Can you think of a way?


if __name__ == '__main__':
    unittest.main()
