from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.base import BasePage


class AddEmployeePage(BasePage):
    @property
    def PAGE_URI(self):
        return "/pim/addEmployee"

    def wait_for_page(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, "firstName")))

    def enter_first_name(self, first):
        self.wait.until(
            expected_conditions.presence_of_element_located((By.ID, "firstName"))).send_keys(first)

    def enter_last_name(self, last):
        self.long_wait.until(
            expected_conditions.presence_of_element_located((By.ID, "lastName"))).send_keys(last)

    def enter_middle_name(self, middle):
        self.wait.until(
            expected_conditions.presence_of_element_located((By.ID, "middleName"))).send_keys(middle)

    def get_employee_id(self):
        return self.browser.find_element_by_id("employeeId").get_attribute("value")

    def enter_employee_name(self, first, last, middle=None):
        self.enter_first_name(first)
        self.enter_last_name(last)
        if middle:
            self.enter_middle_name(middle)

        return self.get_employee_id()

    def enter_employee_credentials(self, username, password, repeat_password=None):
        self.browser.find_element_by_id("chkLogin").click()

        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "user_name"))).send_keys(username)

        self.browser.find_element_by_id("user_password").send_keys(password)

        repassword = repeat_password if repeat_password else password

        self.browser.find_element_by_id("re_password").send_keys(repassword)

        page_url = self.browser.current_url

        # Save
        self.browser.find_element_by_id("btnSave").click()

        self.wait.until(expected_conditions.url_changes(page_url))
        return self.browser.current_url.split('/')[-1]