@classmethod
def tearDownClass(cls) -> None:
    cls.driver.close()
    cls.driver.quit()
