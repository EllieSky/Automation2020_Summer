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
unittest.TestLoader.sortTestMethodsUsing = None

driver = webdriver.Chrome(executable_path="/Users/Shelby/Downloads/chromedriver")


class test_day6HW(unittest.TestCase):

    def setUp(self):
        driver.get("http://hrm-online.portnov.com/symfony/web/index.php/auth/login")
        self.wait = WebDriverWait(driver, 10)




    def tearDown(self):
        driver.quit()



    def test_1login(self, username="admin", password="password"):
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, "txtUsername")))
        driver.find_element_by_id("txtUsername").send_keys(username)
        driver.find_element_by_id("txtPassword").send_keys(password)
        driver.find_element_by_id("btnLogin").click()
        url1 = driver.current_url



        self.wait.until(expected_conditions.url_to_be("http://hrm-online.portnov.com/symfony/web/index.php/pim/viewEmployeeList"))
        driver.find_element_by_xpath("//a[text()='First (& Middle) Name']").click()


        url2 = driver.current_url
        self.wait.until(expected_conditions.url_changes)
        self.assertNotEqual(url1,url2)
        name1 = driver.find_element_by_xpath("//a[text()='Admin'][1]").text
        name2 = driver.find_element_by_xpath("//a[text()='Amber']").text
        self.assertGreaterEqual(name2,name1)

if __name__ == '__main__':
    unittest.main()
