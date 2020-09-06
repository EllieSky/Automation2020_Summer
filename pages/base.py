from tests import BASE_URL


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.PAGE_URI = ""

    def get_title(self) -> str:
        return self.browser.find_element_by_css_selector(".head h1").text

    def go_to_page(self):
        self.browser.get(BASE_URL + "/symfony/web/index.php" + self.PAGE_URI)