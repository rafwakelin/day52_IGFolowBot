import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from config import IG_EMAIL, IG_PASSWORD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


CHROME_DRIVER_PATH = "/Users/rafaelqueiroz/Desktop/chromedriver"
SIMILAR_ACCOUNT = "amazing_python3"
IG_URL = "https://www.instagram.com/accounts/login/"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(IG_URL)
        time.sleep(5)

        ig_login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        ig_login.send_keys(IG_EMAIL)
        ig_psw = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        ig_psw.send_keys(IG_PASSWORD, Keys.ENTER)
        time.sleep(10)

        try:
            self.driver.find_element(By.CSS_SELECTOR, '._ac8f button').click()
            time.sleep(10)
            try:
                self.driver.find_element(By.CSS_SELECTOR, '._a9--._a9_1').click()
                time.sleep(10)
            except NoSuchElementException:
                pass
        except NoSuchElementException:
            pass

    def find_followers(self):
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(10)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "div._aacl._aaco._aacw._aad6._aade")
        for button in all_buttons:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();", button)
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "div._aacl._aaco._aacw._aad6._aade")))
                button.click()
                time.sleep(random.uniform(1, 5))
            except ElementClickInterceptedException:
                pass


ig_bot = InstaFollower()
ig_bot.login()
ig_bot.find_followers()
ig_bot.follow()
