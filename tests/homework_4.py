import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Homework5(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.get('http://hrm-online.portnov.com/')

    def tearDown(self) -> None:
        self.browser.quit()

    def login(self):
        browser = self.browser

        browser.find_element_by_id("txtUsername").send_keys("username")
        browser.find_element_by_id("txtPassword").send_keys("password")
        browser.find_element_by_id("btnLogin").click()




# The goal of this homework is to practice using WebDriverWait.
# After login:
# 1) On the PIM tab click the ADD button.
    def test_add_employee(self):
        browser = self.browser
        wait = WebDriverWait(browser, 3)
        self.login()

        pim=browser.find_element_by_id("menu_pim_viewPimModule")
        wait.until(expected_conditions.presence_of_element_located(pim))
        pim.click()
        employee_list=browser.find_element_by_id("'menu_pim_viewEmployeeList")
        wait.until(expected_conditions.presence_of_element_located(employee_list))
        employee_list.click()
        browser.find_element_by_id("btnAdd").click()
# 2) Enter First, Last name and save the employee id into a variable,
# Hint: The ID is stored as a value attribute, NOT as text. So find_element().text will not work here, use .get_attribute() instead.
        first_name=browser.find_element_by_id("firstName").send_keys("Mark")
        last_name=browser.find_element_by_id("lastName").send_keys("Walberg")
        user_id=browser.find_element_by_id("employeeId").get_attribute("value")
# 3) While creating the employee, on the same screen where you enter their first and last name, click the 'Create Login Details' checkbox.
        browser.find_element_by_id("chkLogin").click()
        user_name= browser.find_element_by_id("user_name")
        password_field = browser.find_element_by_id("user_password")
        password="mw123456"
 # 4) Wait for the 'User Name' and 'Password' fields to appear
        wait.until(expected_conditions.visibility_of(user_name))
        wait.until(expected_conditions.visibility_of(password_field))
# 5) Fill in the 'User Name' field with a unique value. Usernames have to be different each time you run you script.
# Hint: Combine your employee's initials and employee id, to create a unique username.
# 6) Fill in the 'Password' and the 'Confirm Password' fields
        user_name.send_keys(user_name+user_id)
        password_field.send_keys(password)
        browser.find_element_by_id("re_password").send_keys(password)
# 7) Click save and wait for the Personal Details page to load
        browser.find_element_by_id("btnSave").click()


        self.assertEqual(True, True)




# Hint: there is an expected condition for that ;)
# Now perform the following steps:
# 1) Logout.  (Click on Welcome Admin, wait for the user menu to appear, click logout)
# 2) Login using the username and password from steps 5 and 6 above
# 3) Check that correct Welcome message is displayed
# It should contain 'Welcome <your employee's first name>'

if __name__ == '__main__':
    unittest.main()
