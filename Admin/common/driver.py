import unittest

from selenium import webdriver


class MyDriver(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("C:\\Users\R051705030\PycharmProjects\seleniumPython\Driver\chromedriver.exe")


