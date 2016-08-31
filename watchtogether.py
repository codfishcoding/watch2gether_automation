from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import string

driver = webdriver.Firefox()
driver.get('https://www.watch2gether.com') #going to site
driver.find_element_by_css_selector('.ui.primary.button').click()


time.sleep(3) #lets the browser load just as a precaution

watch = driver.current_url

driver.get("https://facebook.com")
time.sleep(2) #sleeps because sometimes will not load fast enough

#login to facebook
driver.find_element_by_id('email').send_keys('notmyemail@hotmail.com')
driver.find_element_by_id('pass').send_keys('veryeasytoguesspassword')
driver.find_element_by_id('loginbutton').click()

time.sleep(3)

#this gets the class name to click on the message box on
#the right hand side of facebook
driver.find_element_by_class_name("class_of_friend").click()

time.sleep(3)

#this sends the keys into the message box once it has been created
driver.find_element_by_css_selector('css_selector_of_friend').send_keys(str(watch) , Keys.ENTER )

#go back to watch2gether
driver.get(watch)
