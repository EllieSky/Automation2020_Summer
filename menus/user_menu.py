from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UserMenu(object):
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 3)
        self.long_wait = WebDriverWait(browser, 15)

    def get_welcome_message(self):
        return self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "welcome"))).text
        # return self.wait.until(expected_conditions.presence_of_element_located((By.ID, "welcome"))).text

    def select_change_password(self):
        self.browser.find_element_by_id("welcome").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Change Password"))).click()


    def logout(self):
        self.browser.find_element_by_id("welcome").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Logout"))).click()


