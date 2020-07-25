from selenium import webdriver
# To print the reports of the test cases in html format (Suite)
# But this is not longer need because unittest has that feature embedded now...
import HtmlTestRunner
import unittest


class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path='../Selenium_Python/Driver/chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_search(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Yu-gi-oh! top ten best cards of all time")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Selenium_Python/Reports'))
