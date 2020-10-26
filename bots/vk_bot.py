from selenium import webdriver
import os
import time

path = os.getcwd()
vk_options = webdriver.FirefoxOptions()
vk_browser = webdriver.Firefox(executable_path=path + '/geckodriver')
main_page_vk = vk_browser.get('https://vk.com/')
time.sleep(10)
login_el = vk_browser.find_element_by_id('index_email')
pass_el = vk_browser.find_element_by_id('index_pass')
button_login = vk_browser.find_element_by_id('index_login_button')
login = ''
for letter in login:
    login_el.send_keys(l)
    time.sleep(2)
time.sleep(13)
password = ''
for letter in password:
    pass_el.send_keys(letter)
    time.sleep(2)
time.sleep(5)
button_login.click()
groups = vk_browser.get('https://vk.com/groups?tab=admin')



