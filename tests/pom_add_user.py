import unittest

from fixtures.base import BaseFixture
from pages.add_employee import AddEmployeePage
from pages.employee_information import EmployeeInformation, TableHeaders
from faker import Faker


class NewUser(BaseFixture):
    def setUp(self) -> None:
        super().setUp()
        self.employee_info_page = EmployeeInformation(self.browser)
        self.add_employee_page = AddEmployeePage(self.browser)

    def test_create_user(self):
        f = Faker()
        last = f.last_name()
        first = f.first_name_female()
        middle = f.first_name_male()
        initials = first[0] + last[0]


        self.login_page.login()

        self.employee_info_page.wait_for_page()

        self.employee_info_page.sort_by_column_header(TableHeaders.FIRST_MIDDLE_NAME)

        self.employee_info_page.goto_add_employee_page()

        emp_id = self.add_employee_page.enter_employee_name(last=last, middle=middle, first=first)
        self.add_employee_page.enter_employee_credentials(f"{initials}{emp_id}", 'password')



        self.login_page.logout()
        self.login_page.login(f'{initials}{emp_id}')

        self.login_page.get_welcome_message()
        self.assertTrue(f"Welcome {first}", self.login_page.get_welcome_message())

if __name__ == '__main__':
    unittest.main()





# mylist = [1,2,3, 'c', '2words', ('Bob', 'James')]
# mylist[1:4]
# [2, 3, 'c']
# mylist[1:4:-1]
# []
# mylist[4:1:-1]
# ['2words', 'c', 3]
# mylist[::-1]
# [('Bob', 'James'), '2words', 'c', 3, 2, 1]
# mylist[::-2]
# [('Bob', 'James'), 'c', 2]
# mylist[::2]
# [1, 3, '2words']
# mylist[::]
# [1, 2, 3, 'c', '2words', ('Bob', 'James')]
# anotherlist = mylist[::]
# another = mylist
# another[1] = 12