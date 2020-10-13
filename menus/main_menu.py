from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class MainMenu():
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 3)
        self.long_wait = WebDriverWait(browser, 15)

    def select_admin_qualification_skills(self):
        action = ActionChains(self.browser)

        action.move_to_element(self.browser.find_element_by_id('menu_admin_viewAdminModule'))
        action.move_to_element(self.browser.find_element_by_id('menu_admin_UserManagement'))
        action.move_to_element(self.browser.find_element_by_id('menu_admin_Qualifications'))
        action.click(self.browser.find_element_by_id('menu_admin_viewSkills'))

        # same result as above
        # action.move_to_element(self.browser.find_element_by_id('menu_admin_viewAdminModule'))
        # action.move_to_element(self.browser.find_element_by_id('menu_admin_UserManagement'))
        # action.move_to_element(self.browser.find_element_by_id('menu_admin_Qualifications'))
        # action.move_to_element(self.browser.find_element_by_id('menu_admin_viewSkills')).click()

        action.perform()