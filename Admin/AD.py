import unittest

from CashBaba.Admin.common.EnbironmentSetup import EnvSetup


class LogIN(EnvSetup):
    def setUp(self):

        self.driver.get("https://192.168.101.23/admin/")
        self.driver.set_page_load_timeout(20)

        exp_title="Cashbaba Admin Panel"

        try:
            if self.driver.title==exp_title:
                print("Cashbaba Admin open successfully")
        except Exception as e:
            print(e+"Cashbaba Admin open Failed")

if __name__ == '__main__':
    unittest.main()


