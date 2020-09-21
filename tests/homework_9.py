import pytest
# before running this test should be installed  pyleniumio and VENV

@pytest.fixture
def login_page(py):
    py.visit("http://hrm-online.portnov.com/symfony/web/index.php/auth/login")
    py.webdriver.find_element_by_name("txtUsername").send_keys("admin")
    py.webdriver.find_element_by_name("txtPassword").send_keys("password")
    py.webdriver.find_element_by_name("Submit").click()


def get_value(py, row: int = 5, column: int = 4):
    name = py.getx(f"//tr[{row}]//td[{column}]").text()
    return name


def test_get_value_func(py, login_page):
    actual_name = get_value(py, row=6, column=4)

    assert actual_name=="Boss"
