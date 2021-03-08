from selenium import webdriver


class TestChrome:
    def test_chrome_launch(self):
        driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")
        driver.get("https://courses.letskodeit.com")
        driver.quit()


test_chrome = TestChrome()
test_chrome.test_chrome_launch()
