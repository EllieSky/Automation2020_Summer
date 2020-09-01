import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class NewUser(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(
            executable_path='/Users/ellie/Selenium/Automation2020_Summer/browsers/chromedriver')
        self.browser.get('http://hrm-online.portnov.com/')

    def tearDown(self) -> None:
        self.browser.quit()

    def test_create_user(self):
        browser = self.browser
        wait = WebDriverWait(browser, 3)

        # Login
        self.login()
        # self.login("ellie")
        # self.login("bob", "abc123")
        # self.login(password="abc123")

        # Go To Add Employee Page
        browser.find_element_by_id("btnAdd").click()

        emp_id = self.enter_employee_name(last="Jones", middle="Kim", first="Emily")

        # create employee credentials
        browser.find_element_by_id("chkLogin").click()

        wait.until(expected_conditions.visibility_of_element_located((By.ID, "user_name"))).send_keys(f"EJ{emp_id}")

        browser.find_element_by_id("user_password").send_keys('password')
        browser.find_element_by_id("re_password").send_keys('password')

        page_url = browser.current_url

        # Save
        browser.find_element_by_id("btnSave").click()

        wait.until(expected_conditions.url_changes(page_url))

        # logout
        browser.find_element_by_id("welcome").click()

        # #welcome-menu li:nth-child(2)>a
        # //div[@id="welcome-menu"]//li[2]/a

        wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Logout"))).click()
        # browser.find_element_by_link_text("Logout").click()

        # Login
        browser.find_element_by_id("txtUsername").send_keys(f'ej{emp_id}')
        browser.find_element_by_id("txtPassword").send_keys('password')

        browser.find_element_by_id("btnLogin").click()

        actual_message = browser.find_element_by_id("welcome").text
        self.assertTrue("Welcome Emily", actual_message)

        # you can write your own "assert" using fail command
        # if "Welcome Emi985407834508934509ly" != actual_message:
        #     self.fail("Very bad... the welcome message does nto match")
        #
        # try:
        #     browser.find_element_by_id("blah").click()
        # except NoSuchElementException:
        #     self.fail("Opps, I did it again")

        self.func_name("james", height=129, size='small', married=True, pet='dog')

    def enter_employee_name(self, first, last, middle=None):
        WebDriverWait(self.browser, 3).until(expected_conditions.presence_of_element_located((By.ID, "firstName"))).send_keys(first)
        # Enter employee name
        self.browser.find_element_by_id("lastName").send_keys(last)
        if middle:
            self.browser.find_element_by_id("middleName").send_keys(middle)

        emp_id = self.browser.find_element_by_id("employeeId").get_attribute("value")
        return emp_id

    def login(self, username='admin', password='password'):
        browser = self.browser
        browser.find_element_by_id("txtUsername").send_keys(username)
        browser.find_element_by_id("txtPassword").send_keys(password)
        browser.find_element_by_id("btnLogin").click()
        WebDriverWait(browser, 3).until(expected_conditions.presence_of_element_located(
            [By.CSS_SELECTOR, "#empsearch_employee_name_empName.inputFormatHint"]))


    def func_name(self, name, dob=None, **kwargs):
        example_dict = {
            'key': 'value',
            'age': 12,
            'speed': 36.5
        }

        # this is what would happen to the passed in params
        # kwargs = {'height':129, 'size':'small', 'married':True, 'pet':'dog'}

        for item in kwargs.keys():
            print(kwargs.get(item))

        if 'height' in kwargs.keys():
            print(f"your height is {kwargs.get('height')}")

if __name__ == '__main__':
    unittest.main()
