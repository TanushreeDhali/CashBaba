import unittest

from selenium import webdriver

class BaseClass(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("C:\\Users\R051705030\PycharmProjects\seleniumPython\Driver\chromedriver.exe")
