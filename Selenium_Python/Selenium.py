from selenium import webdriver

print("sample test case started")
driver = webdriver.Chrome(executable_path='../Selenium_Python/Driver/chromedriver.exe')
driver.maximize_window()
driver.get("https://www.google.com/")
driver.close()
print("sample test successfully completed")