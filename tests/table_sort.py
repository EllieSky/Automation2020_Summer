import unittest

from fixtures.base import BaseFixture
from pages.employee_information import EmployeeInformation


class TableSort(BaseFixture):

    def test_sort_by_first_middle_name(self):
        self.login_page.login()

        emp_info_page = EmployeeInformation(self.browser)
        emp_info_page.sort_table_by_first_middle_name()

        row_count = emp_info_page.get_table_row_count()

        previous_name = ""
        for row_number in range(row_count):
            name = emp_info_page.get_first_middle_name_from_row(row_number + 1).lower()
            self.assertLessEqual(previous_name, name)
            # print(previous_name, " is less of equal to ", name)
            previous_name = name


    def test_sort_by_job_title(self):
        pass


if __name__ == '__main__':
    unittest.main()
