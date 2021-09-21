import unittest

from selenium import webdriver

from CashBaba.test.ClassBase import BaseClass
import time

from CashBaba.test.ClassOne import ClassOne


class Abc():
  url = 'https://www.example.com'

  def drivercreate(self):
    print("Hello abc")
    driver = webdriver.Chrome("C:\\Users\R051705030\PycharmProjects\seleniumPython\Driver\chromedriver.exe")
    return driver

  # def urlget(driver):
  #   driver.get('https://www.example.com')
  #
  # driver = drivercreate("")
  # urlget(driver)