from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.base import BasePage
from pages.employee_information import EmployeeInformation
from tests import BASE_URL, URL_SLUG


class LoginPage(BasePage):
    @property
    def PAGE_URI(self):
        return "/auth/login"

    def login(self, username='admin', password='password'):
        browser = self.browser
        browser.find_element_by_id("txtUsername").send_keys(username)
        browser.find_element_by_id("txtPassword").send_keys(password)
        browser.find_element_by_id("btnLogin").click()

        # self.wait.until(expected_conditions.url_changes(f"{BASE_URL}{URL_SLUG}{self.PAGE_URI}"))
        # if browser.current_url.find(EmployeeInformation.PAGE_URI) >= 0:
        #     self.wait.until(expected_conditions.presence_of_element_located(
        #         [By.CSS_SELECTOR, "#empsearch_employee_name_empName.inputFormatHint"]))

    def click_social_media_icon(self, icon_name):
        social_icon = f"//a[contains(@href, '{icon_name}')]"
        self.browser.find_element_by_xpath(social_icon).click()

    def click_page_footer_link(self):
        footer = "#footer a"
        self.browser.find_element_by_css_selector(footer).click()

    def get_title(self) -> str:
        return self.browser.find_element_by_id("logInPanelHeading").text

    def logout(self):
        self.browser.find_element_by_id("welcome").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Logout"))).click()

    def get_welcome_message(self):
        return self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "welcome"))).text
        # return self.wait.until(expected_conditions.presence_of_element_located((By.ID, "welcome"))).text

    def wait_for_page(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, "frmLogin")))