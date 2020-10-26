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

    def __init__(self, login, password):
        self.login = login
        self.password = password

        path = os.getcwd()
        browser_options = Options()
        browser_options.add_argument('--disable-notifications')
        browser_options.add_argument(
            '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 '
            '(KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')

        self.driver = webdriver.Firefox(options=browser_options, executable_path=path + '/geckodriver')
        self.driver.mobile
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(url='https://www.instagram.com/')

    def log_in(self):

        if self.login == None or self.login == '':
            print('Введите корректный логин')
            exit()
        if self.password == None or self.password == '':
            print('Введите корректный пароль')
            exit()


        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")))
        username = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article'
                                     '/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        time.sleep(5)

        for l in self.login:
            username.send_keys(l)
            time.sleep(0.5)

        password = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article'
                                                '/div[2]/div[1]/div/form/div/div[2]/div/label/input')
        time.sleep(5)

        for p in self.password:
            password.send_keys(p)
            time.sleep(0.5)

        log_in = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article'
                                              '/div[2]/div[1]/div/form/div/div[3]/button')
        log_in.click()
        time.sleep(10)
        save_data = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        save_data.click()

        time.sleep(10)

        ActionChains(self.driver).key_down(Keys.TAB).key_down(Keys.TAB).key_down(Keys.ENTER).perform()

    def like_by_tags(self):

        profile = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div'
                                                       '/div[2]/div[1]/div/div/a')
        profile.click()

        search = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        ActionChains(self.driver).move_to_element(search).double_click().perform()
        ActionChains(self.driver).send_keys('море').perform()


bot = InstaLikeBot(login='rumagpie', password='456988wdv')
bot.log_in()
bot.like_by_tags()