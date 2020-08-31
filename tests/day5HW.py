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
driver.get("http://hrm-online.portnov.com/symfony/web/index.php/auth/login")

class Day5HW:

    def __init__(self):
        self.wait = WebDriverWait(driver, 10)
        self.first_name = None
        self.emp_id = None
        self.usr_name = None
        self.new_password = None

    def login(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID,"txtUsername")))
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("password")
        driver.find_element_by_id("btnLogin").click()

    def add_employee(self):
        driver.find_element_by_id("menu_pim_addEmployee").click()
        self.first_name = "Joe"
        driver.find_element_by_id("firstName").send_keys(self.first_name)
        driver.find_element_by_id("lastName").send_keys("Smith")
        emp_id = driver.find_element_by_id("employeeId").get_attribute("value")
        driver.find_element_by_id("chkLogin").click()
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID,"user_name")))
        driver.find_element_by_id("user_name")
        self.usr_name = (f"js{emp_id}")
        print(self.usr_name)
        driver.find_element_by_id("user_name").send_keys(self.usr_name)
        driver.find_element_by_id("user_password")
        self.new_password= "MyP@ssw0rd!"
        driver.find_element_by_id("user_password").send_keys(self.new_password)
        driver.find_element_by_id("re_password").send_keys(self.new_password)
        driver.find_element_by_id("btnSave").click()
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID,"btnSave")))
        driver.find_element_by_id("welcome").click()


    def logout(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//a[contains(@href,'logout')]")))
        driver.find_element_by_xpath("//a[contains(@href,'logout')]").click()



    def verify_add_emp(self):
        print(self.usr_name)
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "txtUsername")))
        driver.find_element_by_id("txtUsername").send_keys(self.usr_name)
        driver.find_element_by_id("txtPassword").send_keys(self.new_password)
        driver.find_element_by_id("btnLogin").click()
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID,"btnSave")))
        welcome_message = str(driver.find_element_by_id("welcome"))
        if "Joe" in welcome_message:
            print("Account created")
        else:
            print("Account not created")

    def close(self):
        driver.quit()


run = Day5HW()
run.login()
run.add_employee()
run.logout()
run.verify_add_emp()
run.close()















