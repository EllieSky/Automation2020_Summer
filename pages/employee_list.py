
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base import BasePage
from tests import BASE_URL


class EmployeeList(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.PAGE_URI = "/pim/addEmployee"

    def enter_employee_name(self, first, last, middle=None):
        WebDriverWait(self.browser, 3).until(
            EC.presence_of_element_located((By.ID, "firstName"))).send_keys(first)
        # Enter employee name
        self.browser.find_element_by_id("lastName").send_keys(last)
        if middle:
            self.browser.find_element_by_id("middleName").send_keys(middle)

        emp_id = self.browser.find_element_by_id("employeeId").get_attribute("value")
        return emp_id

    def click_login_details_button(self):
        self.browser.find_element_by_id("chkLogin").click()

    def password_field(self,password='password'):
        self.browser.find_element_by_id("user_password").send_keys(password)

    def confirm_password_field(self,password='password'):
        self.browser.find_element_by_id("re_password").send_keys(password)

    def button_save_click(self):
        page_url = self.browser.current_url
        self.browser.find_element_by_id("btnSave").click()
        WebDriverWait(self.browser, 3).until(EC.url_changes(page_url))

    def button_logout_click(self):
        self.browser.find_element_by_id("welcome").click()
        WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Logout"))).click()