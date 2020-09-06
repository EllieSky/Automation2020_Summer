import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AmazonBestSellerExample(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()
        self.browser.get('https://www.amazon.com/')

    def tearDown(self) -> None:
        self.browser.quit()

    def test_find_headphones(self):
        search_keyword = 'tablet'

        browser = self.browser
        wait = WebDriverWait(browser, 5)
        browser.find_element_by_id("twotabsearchtextbox").send_keys(search_keyword + Keys.ENTER)
        # # OR
        # browser.find_element_by_id("twotabsearchtextbox").send_keys("headphones")
        # browser.find_element_by_name("site-search").submit()
        # # OR
        # browser.find_element_by_id("twotabsearchtextbox").send_keys("headphones")
        # browser.find_element_by_css_selector("input.nav-input[value='Go']").click()

        best_sellers_list = browser.find_elements_by_css_selector(
            "span.a-badge-label[data-a-badge-color='sx-orange'] span.a-badge-text[data-a-badge-color='sx-cloud']")

            # '//span[@class="a-badge-label"][@data-a-badge-color="sx-orange"]//span[@class="a-badge-text"][@data-a-badge-color="sx-cloud"]'

        for best_seller_banner in best_sellers_list:
            # little cheat
            best_seller_banner.find_element_by_xpath(
                "./ancestor::div[@class='a-section a-spacing-medium']/div[2]//a"
            ).send_keys(Keys.COMMAND + Keys.ENTER)

        wait.until(expected_conditions.number_of_windows_to_be(len(best_sellers_list) + 1))

        handles = browser.window_handles
        for j in range(1, len(handles)):
            browser.switch_to.window(handles[j])

            wait.until(expected_conditions.presence_of_element_located((By.ID, "add-to-cart-button"))).click()
            # browser.find_element_by_id("add-to-cart-button")

            # a_list = browser.find_elements_by_id('a-popover-1')
            # if a_list and a_list[0].is_displayed():
            #     browser.find_element_by_css_selector('#a-popover-1 .a-button-close').click()

            if browser.find_elements_by_id('a-popover-1') and browser.find_element_by_id('a-popover-1').is_displayed():
                browser.find_element_by_css_selector('#a-popover-1 .a-button-close').click()
        pass



if __name__ == '__main__':
    unittest.main()
