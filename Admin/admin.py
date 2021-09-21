import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome("C:\\Users\R051705030\PycharmProjects\seleniumPython\Driver\chromedriver.exe")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://192.168.101.23/admin/")
        self.assertIn("Cashbaba Admin Panel", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("Cashbaba Admin Panel")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()