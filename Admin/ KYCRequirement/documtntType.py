from selenium.webdriver.common.action_chains import ActionChains

from CashBaba.Admin.common.EnbironmentSetup import logIn


class KycRequierment(logIn):



    def testKycRequierment(self):
        driver=self.driver
        wallet_category_but=driver.find_element_by_xpath("//span[normalize-space()='KYC Requirement']").click()
        driver.implicitly_wait(10)
        print("Click kyc requirement")





    # def testAllUser(self):
    #     driver = self.driver
    #     all_user_but = driver.find_element_by_xpath("//a[normalize-space()='All User']").click()
    #     driver.implicitly_wait(10)
    #     print("success2")
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
