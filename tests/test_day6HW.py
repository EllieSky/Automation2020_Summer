import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import *
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/Shelby/Downloads/chromedriver")


class test_day6HW(unittest.TestCase):

    def setUp(self) -> None:
        driver.get("http://hrm-online.portnov.com/symfony/web/index.php/auth/login")
        self.wait = WebDriverWait(driver, 10)
        self.first_name = None
        self.emp_id = None
        self.usr_name = None
        self.new_password = None

    def tearDown(self) -> None:
        driver.quit()

    def login(self, username='admin', password='password'):
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "txtUsername")))
        driver.find_element_by_id("txtUsername").send_keys(username)
        driver.find_element_by_id("txtPassword").send_keys(password)
        driver.find_element_by_id("btnLogin").click()


if __name__ == '__main__':
    unittest.main()
