import unittest

from selenium.webdriver.support import expected_conditions

from fixtures.base import BaseFixture
from pages.add_employee import AddEmployeePage


class GoToMenu(BaseFixture):
    def setUp(self) -> None:
        super().setUp()
        self.login_page.login()

    def test_select_qualification_skills(self):
        add_emp_page = AddEmployeePage(self.browser)
        url = self.browser.current_url
        add_emp_page.main_menu.select_admin_qualification_skills()
        self.wait.until(expected_conditions.url_changes(url))
        self.assertEqual('Skills', self.browser.find_element_by_css_selector('#recordsListDiv h1').text)
        self.user_menu.logout()


if __name__ == '__main__':
    unittest.main()
