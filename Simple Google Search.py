from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Taking chromedriver.exe to launch chrome as the bot browser.
PATH = "D:\DELL\Documents\Course\Python\Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Take in "https://google.com" as the search bar
driver.get("https://google.com")

#Searching the search elements in google.com
search = driver.find_element_by_name('q')

#Inputs in the search bar
search.send_keys("YAY IT CLICKS ")

#Enters the RETURN key in the keyboard
search.send_keys(Keys.RETURN)
