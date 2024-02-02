from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import csv
import random

# arkusz z którego będziemy wyciagać informacje do wiadomości
df = pd.read_excel("ZImionami.xlsx", sheet_name="Arkusz1")
Imiona = df['Imiona']  # zmienna przechowywująca listę imion z bazy
Names_ig = df['Nazwa']  # zmienna przechowywująca listę nazw użytkownika z bazy
# print(Imiona)
# print(Names_ig)

logins = 'przemekkowalski5'  # login do konta
passwords = 'przemekkowalski55'  # hasło do konta
# between_messages = 1450 # odstęp między wysyłanymi wiadomościami
between_messages = 10
browser = webdriver.Chrome()  # wybór przeglądarki naszego webdrivera

browser.get('https://instagram.com')  # url, na który ma bot wejść na początku
browser.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
time.sleep(random.randrange(1, 2))  # przerwa pomiędzy wykonywaniem czynności
input_username = browser.find_element_by_name('username')
time.sleep(random.randrange(1, 2))
input_password = browser.find_element_by_name('password')
input_username.send_keys(logins)  # wpisywanie loginu
time.sleep(random.randrange(1, 2))
input_password.send_keys(passwords)  # wpisywanie hasła
time.sleep(random.randrange(2, 3))
input_password.send_keys(Keys.ENTER)
time.sleep(3)
browser.find_element_by_xpath(
    '/html/body/div[5]/div/div/div/div[3]/button[2]').click()
time.sleep(5)
browser.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
time.sleep(random.randrange(3))
browser.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()

licznik = 0
while licznik < 1305:
    time.sleep(random.randrange(1, 2))
    browser.find_element_by_xpath(
        '/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(Names_ig[licznik])
    time.sleep(random.randrange(3, 4))
    browser.find_element_by_xpath(
        '/html/body/div[6]/div/div/div[2]/div[2]').find_element_by_tag_name('button').click()
    time.sleep(random.randrange(3, 4))
    browser.find_element_by_xpath(
        '/html/body/div[6]/div/div/div[1]/div/div[3]/div/button/div').click()
    time.sleep(random.randrange(3, 4))
    text_area = browser.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    text_area.send_keys(
        'Cześć ' + Imiona[licznik]+'! Tutaj Przemek, chciałbym przedstawić Ci ofertę która opiewa o 3 miliony złotych. Chcesz się dowiedzieć więcej? Odpisz. Pozdrawiam!')
    time.sleep(random.randrange(3, 4))
    text_area.send_keys(Keys.ENTER)
    browser.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()
    licznik += 1
    time.sleep(between_messages)
