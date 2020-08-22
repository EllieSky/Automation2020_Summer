import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AmazonBestSellerExample(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(
            executable_path='/Users/ellie/Selenium/Automation2020_Summer/browsers/chromedriver')
        self.browser.get('https://www.amazon.com/')

    def tearDown(self) -> None:
        self.browser.quit()

    def test_find_headphones(self):
        browser = self.browser
        browser.find_element_by_id("twotabsearchtextbox").send_keys("headphones" + Keys.ENTER)
        # # OR
        # browser.find_element_by_id("twotabsearchtextbox").send_keys("headphones")
        # browser.find_element_by_name("site-search").submit()
        # # OR
        # browser.find_element_by_id("twotabsearchtextbox").send_keys("headphones")
        # browser.find_element_by_css_selector("input.nav-input[value='Go']").click()

        best_sellers_list = browser.find_elements_by_css_selector(
            "span.a-badge-label[data-a-badge-color='sx-orange'] span.a-badge-text[data-a-badge-color='sx-cloud']")

            # '//span[@class="a-badge-label"][@data-a-badge-color="sx-orange"]//span[@class="a-badge-text"][@data-a-badge-color="sx-cloud"]'

        # little cheat
        best_sellers_list[0].find_element_by_xpath("./ancestor::div[@class='a-section a-spacing-medium']/div[2]//a").send_keys(Keys.COMMAND + Keys.ENTER)

        pass



if __name__ == '__main__':
    unittest.main()
