import unittest
import time

from selenium import webdriver

class logIn(unittest.TestCase):
    def testFunc(self):
        self.driver=webdriver.Chrome("C:\\Users\R051705030\PycharmProjects\seleniumPython\Driver\chromedriver.exe")
        driver=self.driver
        driver.maximize_window()
        driver.get("https://192.168.101.23/admin/")
        print("Url Open successfully")
        driver.implicitly_wait(10)
        exp_title="Cashbaba Admin Panel"
        dtl_but = driver.find_element_by_id("details-button").click()
        proceed_but = driver.find_element_by_id("proceed-link").click()
        driver.implicitly_wait(10)
        # Open a new window
        driver.execute_script("window.open('');")
        # Switch to the new window
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://192.168.101.31:9001/swagger/index.html")
        dtl2_but = driver.find_element_by_id("details-button").click()
        proceed2_but  = driver.find_element_by_id("proceed-link").click()
        time.sleep(2)

        # Switch to the new window
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://192.168.101.23/admin/")

        ele_user = driver.find_element_by_xpath("//input[@placeholder='Username']")
        ele_user.send_keys("01144080183")
        print(ele_user.is_enabled())
        print(ele_user.is_displayed())

        ele_pass = driver.find_element_by_xpath("//input[@placeholder='Password']")
        ele_pass.send_keys("Rcis123$..")
        print(ele_pass.is_enabled())
        print(ele_pass.is_displayed())
        time.sleep(2)
        ele_log_but = driver.find_element_by_xpath("//button[normalize-space()='SIGN IN']").click()
        time.sleep(2)
        print("Admin Login success")



if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)