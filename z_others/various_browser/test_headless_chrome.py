from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe", chrome_options=options)
driver.get("https://www.duckduckgo.com")
print(driver.title)
driver.quit()
