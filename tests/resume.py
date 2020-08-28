import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from parameterized import parameterized


class Resume(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get("http://hrm-online.portnov.com/")

    def tearDown(self) -> None:
        self.browser.quit()

    @parameterized.expand([
        ("admin", "password", "Bob Boss", "Resume is attached", "No resume attached", "txtUsername", "txtPassword", "btnLogin", "empsearch_supervisor_name",
         "searchBtn", "//td[text()='QA Lead']/ancestor::tr//a", "tblAttachments")
    ])
    def test_is_resume_file_uploaded(self, username, password, supervisor_name, resume_is_attached_message, resume_is_not_attached_message,
                                     username_input, password_input, login_button, supervisor_name_input, search_button, employee_id, resume):
        browser = self.browser

        browser.find_element_by_id(username_input).send_keys(username)
        browser.find_element_by_id(password_input).send_keys(password)

        browser.find_element_by_id(login_button).click()

        browser.find_element_by_id(supervisor_name_input).send_keys(supervisor_name)

        browser.find_element_by_id(search_button).click()

        browser.find_element_by_xpath(employee_id).click()
        # //td[text()='QA Lead']/..//a[text()='774863']

        try:
            browser.find_element_by_id(resume).is_displayed()
            print(resume_is_attached_message)
        except NoSuchElementException:
            print(resume_is_not_attached_message)
        return True

    # // table[ @ id = 'btnTable']
    # // table[contains( @ id, "btn")]
    # // label[contains(text(), "Or")]
    # // label[text() = "Oranges"] /../..// input
    # // label[text() = "Oranges"] / ancestor::tr // input
    # // label[text() = "Oranges"] / following::input


if __name__ == '__main__':
    unittest.main()
