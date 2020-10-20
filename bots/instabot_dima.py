from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from random import randrange


class InstaLikeBot():
    def login(self):

        path = os.getcwd()
        browser_options = Options()
        browser_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 '
                                     '(KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
        driver = webdriver.Firefox(options=browser_options, executable_path=path + '/geckodriver')
        wait = WebDriverWait(driver, 10)
        driver.get(url='https://www.instagram.com/')
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")))
        username = driver.find_element_by_xpath('/html/body/div[1]/section/main/article'
                                     '/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        time.sleep(5)
        username.send_keys('rumagpie')
        password = driver.find_element_by_xpath('/html/body/div[1]/section/main/article'
                                                '/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        time.sleep(5)
        password.send_keys('456988wdv')
        log_in = driver.find_element_by_xpath('/html/body/div[1]/section/main/article'
                                              '/div[2]/div[1]/div/form/div/div[3]/button')
        log_in.click()
        time.sleep(10)
        save_data = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        save_data.click()

        driver.implicitly_wait(15)

        popup = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        ActionChains(driver).move_to_element(popup).click(popup)



bot = InstaLikeBot()
bot.login()