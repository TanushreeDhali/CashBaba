from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\R051705030\\PycharmProjects\\seleniumPython\\Driver\\chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("https://san.cashbaba.com.bd/admin/login")
#Test case1
driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("01144080183")
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("Rcis123$..")
driver.find_element_by_xpath("//button[normalize-space()='SIGN IN']").click()
#Test case2

time.sleep(5)
driver.quit()
