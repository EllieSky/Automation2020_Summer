from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base import BasePage
from pages.add_employee import AddEmployeePage


class EmployeeInformation(BasePage):

    @property
    def PAGE_URI(self):
        return "/pim/viewEmployeeList"

    def sort_table_by_first_middle_name(self) -> None:
        self.browser.find_element_by_xpath("//th/a[text()='First (& Middle) Name']").click()
        self.wait.until(EC.url_contains("sortField=firstMiddleName"))

    def get_first_middle_name_from_row(self, row_number) -> str:
        return self.browser.find_element_by_xpath(f"//tbody/tr[{row_number}]/td[3]").text

    def get_table_row_count(self):
        return len(self.browser.find_elements_by_xpath("//tbody/tr"))

    def goto_add_employee_page(self):
        self.browser.find_element_by_id("btnAdd").click()
        self.wait.until(EC.url_contains(AddEmployeePage.PAGE_URI))
        # OR
        self.wait.until(EC.presence_of_element_located((By.ID, 'lastName')))

