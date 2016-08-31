from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string

driver = webdriver.Firefox()
driver.get('https://www.watch2gether.com')
driver.find_element_by_css_selector('.ui.primary.button').click()


time.sleep(3)

watch = driver.current_url

driver.get("https://facebook.com")
time.sleep(2)

#login to facebook
driver.find_element_by_id('email').send_keys('notmyemail@hotmail.com')
driver.find_element_by_id('pass').send_keys('veryeasytoguesspassword')
driver.find_element_by_id('loginbutton').click()

time.sleep(3)

driver.find_element_by_class_name("class_of_friend").click()

time.sleep(3)

driver.find_element_by_css_selector('css_selector_of_friend').send_keys(str(watch) , Keys.ENTER )


driver.get(watch)