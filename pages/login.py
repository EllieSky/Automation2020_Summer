from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.PAGE_URI = "/auth/login"

    def login(self, username='admin', password='password'):
        browser = self.browser
        browser.find_element_by_id("txtUsername").send_keys(username)
        browser.find_element_by_id("txtPassword").send_keys(password)
        browser.find_element_by_id("btnLogin").click()
       # WebDriverWait(browser, 3).until(expected_conditions.presence_of_element_located(
        #    [By.CSS_SELECTOR, "#empsearch_employee_name_empName.inputFormatHint"]))

    def click_social_media_icon(self, icon_name):
        social_icon = f"//a[contains(@href, '{icon_name}')]"
        self.browser.find_element_by_xpath(social_icon).click()

    def click_page_footer_link(self):
        footer = "#footer a"
        self.browser.find_element_by_css_selector(footer).click()

    def get_title(self) -> str:
        return self.browser.find_element_by_id("logInPanelHeading").text

