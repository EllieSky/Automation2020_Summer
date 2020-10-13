import unittest

from selenium.webdriver.common.by import By

from fixtures.base import BaseFixture

class JSInjectionDemo(BaseFixture):
    footer = (By.ID, 'footer')

    def test_something(self):
        self.browser.set_window_size(500,500)
        self.browser.execute_script('window.scrollTo(35, 100)')
        # loc = self.browser.find_element_by_id('footer').location
        loc = self.browser.find_element(*self.footer).location
        self.browser.execute_script('window.scrollTo(arguments[0], arguments[1])', loc['x'], loc['y'])
        self.browser.find_element_by_id('divLogo').location_once_scrolled_into_view
        scroll_width = self.browser.execute_script("return document.querySelector('#divLogo').scrollWidth;")
        pass
if __name__ == '__main__':
    unittest.main()
