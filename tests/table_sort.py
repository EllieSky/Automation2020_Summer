import unittest

from selenium import webdriver

from pages.employee_information import EmployeeInformation
from pages.login import LoginPage
from tests import CHROME_DRIVER


class TableSort(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.login_page = LoginPage(self.browser)
        self.login_page.go_to_page()
        # self.browser.get('http://hrm-online.portnov.com/')
        # new comment

    def tearDown(self) -> None:
        # this closes the browser session, not just the window
        self.browser.quit()  # some more changes

    def test_sort_by_first_middle_name(self):
        self.login_page.login()

        emp_info_page = EmployeeInformation(self.browser)
        emp_info_page.sort_table_by_first_middle_name()

        row_count = emp_info_page.get_table_row_count()

        previous_name = ""
        for row_number in range(row_count):
            name = emp_info_page.get_first_middle_name_from_row(row_number + 1).lower()
            self.assertLessEqual(previous_name, name)
            print(previous_name, " is less of equal to ", name)
            previous_name = name

    def test_sort_by_job_title(self):
        pass


if __name__ == '__main__':
    unittest.main()
