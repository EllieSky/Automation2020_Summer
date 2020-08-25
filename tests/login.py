import time
import unittest

from selenium import webdriver
from parameterized import parameterized
import selenium


class Login(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path='/Users/ellie/Selenium/Automation2020_Summer/browsers/chromedriver')
        self.browser.get('http://hrm-online.portnov.com/')
        # new comment

    def tearDown(self) -> None:
        # this closes the browser session, not just the window
        self.browser.quit()  # some more changes

    @parameterized.expand([
        ("valid_credentials", "admin", "password", "viewEmployeeList", "Welcome Admin", True),
        ("bad_password", "admin", "PASSWORD", "validateCredentials", "Invalid credentials", False),
        ("empty_username", "", "password", "/auth/login", "Username cannot be empty", False),
        ("white_space_username_password", " ", " ", "validateCredentials", "Invalid credentials", False)
    ])
    def test_login(self, test_name, username, password, url_ending, expected_message, positive):
        browser = self.browser

        browser.find_element_by_id("txtUsername").send_keys(username)
        browser.find_element_by_id("txtPassword").send_keys(password)

        browser.find_element_by_id("btnLogin").click()

        time.sleep(3)

        url = browser.current_url

        if positive:
            actual_message = browser.find_element_by_id("welcome").text

        else:
            actual_message = browser.find_element_by_id("spanMessage").text

        self.assertTrue(url.endswith(url_ending),
                            "The page url '{0}' did not end with the expected value of '{1}'".format(url, url_ending))

        # self.assertTrue(url.endswith(url_ending),
        #                     f"The page url '{url}' did not end with the expected value of '{url_ending}'")

        self.assertEqual(expected_message, actual_message)

        # to count the number of inputs on the page:
        # len(browser.find_elements_by_tag_name("input"))

if __name__ == '__main__':
    unittest.main()

"//input/../../div"