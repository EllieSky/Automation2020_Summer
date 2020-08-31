import unittest
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class AddNewEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get("http://hrm-online.portnov.com/")

    def tearDown(self) -> None:
        self.browser.quit()

    def test_add_new_employee_functionality(self):
        browser = self.browser
        explicit_wait = WebDriverWait(browser, 3)

        browser.find_element_by_id("txtUsername").send_keys("admin")
        browser.find_element_by_id("txtPassword").send_keys("password")
        browser.find_element_by_id("btnLogin").click()

        # 1) On the PIM tab click the ADD button.
        explicit_wait.until(expected_conditions.presence_of_element_located([By.XPATH, "//input[@id='empsearch_employee_name_empName'][@class='ac_input inputFormatHint']"]))
        browser.find_element_by_id("menu_pim_addEmployee").click()

        # 2) Enter First name
        first_name = "max"
        first_name_input = browser.find_element_by_id("firstName")
        explicit_wait.until(expected_conditions.visibility_of(first_name_input))
        first_name_input.send_keys(first_name)
        first_name_input_value = first_name_input.get_attribute("value")

        # 2) Last name
        last_name = "seli"
        last_name_input = browser.find_element_by_id("lastName")
        last_name_input.send_keys(last_name)
        last_name_input_value = last_name_input.get_attribute("value")

        # 2) save the employee id into a variable
        employee_id = browser.find_element_by_id("employeeId").get_attribute("value")

        # 3) click the 'Create Login Details' checkbox.
        browser.find_element_by_id("chkLogin").click()

        user_name_input = browser.find_element_by_id("user_name")
        password_input = browser.find_element_by_id("user_password")

        # 4) Wait for the 'User Name' and 'Password' fields to appear
        explicit_wait.until(expected_conditions.visibility_of(user_name_input))
        explicit_wait.until(expected_conditions.visibility_of(password_input))

        # 5) Fill in the 'User Name' field with a unique value
        user_name_input.send_keys(first_name_input_value + last_name_input_value + employee_id)

        # 6) Fill in the 'Password' and the 'Confirm Password' fields
        password = "maxpassword"
        password_input.send_keys(password)
        browser.find_element_by_id("re_password").send_keys(password)

        # 7) Click save
        browser.find_element_by_id("btnSave").click()

        # 7) wait for the Personal Details page to load
        explicit_wait.until(expected_conditions.url_to_be("http://hrm-online.portnov.com/symfony/web/index.php/pim/viewPersonalDetails/empNumber/" + employee_id))
        current_url = browser.current_url
        self.assertTrue(current_url.endswith(employee_id))

        # Logout.  (Click on Welcome Admin, wait for the user menu to appear, click logout)
        browser.find_element_by_id("welcome").click()

        logout = browser.find_element_by_xpath("//a[text()='Logout']")
        explicit_wait.until(expected_conditions.visibility_of(logout))
        logout.click()

        # Login using the username and password from steps 5 and 6 above
        browser.find_element_by_id("txtUsername").send_keys(first_name_input_value + last_name_input_value + employee_id)
        browser.find_element_by_id("txtPassword").send_keys(password)
        browser.find_element_by_id("btnLogin").click()

        # Check that correct Welcome message is displayed
        welcome_message = browser.find_element_by_xpath("//a[text()='Welcome " + first_name + "']")
        explicit_wait.until(expected_conditions.visibility_of(welcome_message))
        self.assertTrue(welcome_message.is_displayed())


if __name__ == '__main__':
    unittest.main()
