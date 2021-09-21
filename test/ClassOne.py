import unittest

from CashBaba.test.ClassBase import BaseClass


# class ClassOne(BaseClass):
class ClassOne(BaseClass):
    def testFunc(self):
        print("hello")
        self.driver.get("https://www.w3schools.com/html/default.asp")
        self.driver.implicitly_wait(2)
        self.driver.close()

if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)