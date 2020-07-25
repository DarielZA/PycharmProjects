#This import give us a test output when the script is executed
import unittest
from selenium import webdriver

class SearchText(unittest.TestCase):
    def setUp(self):
        #Create a new chrome session...
        self.driver = webdriver.Chrome(executable_path='../Selenium_Python/Driver/chromedriver.exe')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        #Navigate to the home page...
        self.driver.get("http://www.google.com")

    def test_search_by_text(self):
        #Get the text search box...
        self.search_field = self.driver.find_element_by_name("q")

        #Enter search keyword and submit...
        self.search_field.send_keys("Selenium WebDriver Interview Questions")
        self.search_field.submit()

        #Get the list of elements which are displayed after the search
        #currently on result page using "find_elements_by_class_name" method...

        lists = self.driver.find_elements_by_class_name("r")
        no=len(lists)
        self.assertEqual(14, len(lists))


    def tearDown(self):
        #Close the browser window...
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

