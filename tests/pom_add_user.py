import unittest

from fixtures.base import BaseFixture
from pages.add_employee import AddEmployeePage
from pages.employee_information import EmployeeInformation


class NewUser(BaseFixture):
    def setUp(self) -> None:
        super().setUp()
        self.employee_info_page = EmployeeInformation(self.browser)
        self.add_employee_page = AddEmployeePage(self.browser)

    def test_create_user(self):
        self.login_page.login()

        self.employee_info_page.goto_add_employee_page()

        emp_id = self.add_employee_page.enter_employee_name(last="Jones", middle="Kim", first="Emily")
        self.add_employee_page.enter_employee_credentials(f"EJ{emp_id}", 'password')

        self.login_page.logout()
        self.login_page.login(f'ej{emp_id}')

        self.login_page.get_welcome_message()
        self.assertTrue("Welcome Emily", self.login_page.get_welcome_message())

if __name__ == '__main__':
    unittest.main()
