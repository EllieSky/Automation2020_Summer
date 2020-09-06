import unittest

from selenium import webdriver


class FrameDemo(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(
            executable_path='/Users/ellie/Selenium/Automation2020_Summer/browsers/chromedriver')
        self.browser.get('https://skryabin.com/webdriver/html/sample.html')

    def tearDown(self) -> None:
        self.browser.quit()


    def test_frame_fields(self):
        browser = self.browser
        # outside a frame


        browser.switch_to.frame(browser.find_element_by_name('additionalInfo'))

        # inside a frame
        self.assertTrue(2 == len(browser.find_elements_by_tag_name('label')))

        displayed = browser.find_element_by_id('contactPersonName').is_displayed()
        self.assertTrue(displayed)
        browser.find_element_by_id("contactPersonName").send_keys("some text")
        # self.assertEqual("Contact Person Phone", browser.find_element_by_xpath("//*[@id='contactPersonPhone']/preceding::label[1]").text)

        browser.switch_to.default_content()

        # outside a frame
        displayed = browser.find_element_by_id('samplePageForm').is_displayed()
        self.assertTrue(displayed)


if __name__ == '__main__':
    unittest.main()
