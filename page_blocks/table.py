from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageTable:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 3)
        self.long_wait = WebDriverWait(browser, 15)

    def delete_row(self, row_num):
        table = self.browser.find_element_by_id("resultTable")
        table.find_element_by_xpath(f".//tr[{row_num}]//input").click()
        self.delete()

    def delete(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, "btnDelete"))).click()

    def get_value_from_row(self, row_num=5, column_name=4):
        name = self.browser.find_element_by_xpath(f"//tr[{row_num}]//td[{column_name}]").text()
        return name.title


        # //tr[1]//td[4]
        # get_value_from_row(3, "Last Name")
        # return the name


    def sort_by_column_header(self, header_name, order="ASC"):
        self.browser.find_element_by_xpath(
            f"//th/a[text()='{header_name.title()}']").click()
