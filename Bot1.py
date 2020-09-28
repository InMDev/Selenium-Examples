from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "D:\DELL\Documents\Course\Python\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")

search = driver.find_element_by_name('q')
search.send_keys("YAY IT CLICKS ")
search.send_keys(Keys.RETURN)
