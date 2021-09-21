from CashBaba.Admin.common.EnbironmentSetup import logIn


class user(logIn):

    def testUser(self):
        driver=self.driver
        user_but=driver.find_element_by_xpath("//span[normalize-space()='Users']").click()
        driver.implicitly_wait(10)
        print("success")


    # def testAllUser(self):
    #     driver = self.driver
    #     all_user_but = driver.find_element_by_xpath("//a[normalize-space()='All User']").click()
    #     driver.implicitly_wait(10)
    #     print("success2")
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
