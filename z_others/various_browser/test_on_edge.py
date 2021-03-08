from selenium import webdriver


class TestEdge:
    def test_on_edge(self):
        driver = webdriver.Edge(executable_path="../../drivers/msedgedriver.exe")
        driver.get("https://courses.letskodeit.com")
        driver.quit()


test_edge = TestEdge()
test_edge.test_on_edge()
