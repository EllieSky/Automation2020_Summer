import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.employee_information import EmployeeInformation
from pages.login import LoginPage
from pages.employee_list import EmployeeList
from tests import CHROME_DRIVER


class AddUser(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.login_page = LoginPage(self.browser)
        self.login_page.go_to_page()
        self.add_user = EmployeeList(self.browser)
        self.add_user.go_to_page()



    def tearDown(self) -> None:
        # this closes the browser session, not just the window
        self.browser.quit()  # some more changes

    def test_add_new_user(self):
        # login
        self.login_page.login()
        browser = self.browser
        wait = WebDriverWait(browser, 3)
        # login

        # Go To Add Employee Page
        self.add_user.add_button().click()
        #browser.find_element_by_id("btnAdd").click()

        emp_id = self.add_user.enter_employee_name(last="Jones", middle="Kim", first="Emily")
        # create employee credentials
        #browser.find_element_by_id("chkLogin").click()
        self.add_user.login_details_button().click()
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "user_name"))).send_keys(f"EJ{emp_id}")

        #browser.find_element_by_id("user_password").send_keys('password')
        self.add_user.password_field()
        #browser.find_element_by_id("re_password").send_keys('password')
        self.add_user.confirm_password_field()
        page_url = browser.current_url

        # Save

        self.add_user.button_save_click()
        #browser.find_element_by_id("btnSave").click()

        #wait.until(expected_conditions.url_changes(page_url))

        # logout
        self.add_user.button_logout_click()
        #browser.find_element_by_id("welcome").click()

        # #welcome-menu li:nth-child(2)>a
        # //div[@id="welcome-menu"]//li[2]/a

        #wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Logout"))).click()
        # browser.find_element_by_id("btnLogin").click()
        self.login_page.login(username=f'ej{emp_id}', password='password')
        actual_message = self.add_user.welcome_button().text
        #actual_message = browser.find_element_by_id("welcome").text
        self.assertTrue("Welcome Emily", actual_message)







if __name__ == '__main__':
    unittest.main()
