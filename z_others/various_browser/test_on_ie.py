from selenium import webdriver


class TestIE:
    def test_ie_launch(self):
        driver = webdriver.Ie(executable_path="../../drivers/IEDriverServer.exe")
        driver.get("https://courses.letskodeit.com")
        driver.quit()


test_ie = TestIE()
test_ie.test_ie_launch()
