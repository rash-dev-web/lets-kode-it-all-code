from selenium import webdriver


class TestFirefox:
    def test_firefox_launch(self):
        driver = webdriver.Firefox(executable_path="../../drivers/geckodriver.exe")
        driver.get("https://courses.letskodeit.com")
        driver.quit()


test_firefox = TestFirefox()
test_firefox.test_firefox_launch()
