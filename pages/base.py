from abc import abstractmethod, ABC, abstractproperty

from selenium.webdriver.support.wait import WebDriverWait

from tests import BASE_URL


class BasePage(ABC):
    @property
    @abstractmethod
    def PAGE_URI(self):
        return ""

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 3)
        self.long_wait = WebDriverWait(browser, 15)

    def get_title(self) -> str:
        return self.browser.find_element_by_css_selector(".head h1").text

    def go_to_page(self):
        self.browser.get(BASE_URL + "/symfony/web/index.php" + self.PAGE_URI)

    @abstractmethod
    def wait_for_page(self):
        pass