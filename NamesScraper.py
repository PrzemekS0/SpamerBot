from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
import csv

links = open('linkigłówne.txt', 'r+')
plik = links.read().split('\n')
imiona = open('imiona.txt', 'w+')

for url in plik:
    driver = webdriver.Chrome()
    driver.get(url)
    WebDriverWait(url, 5)
    akceptacja = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
    akceptacja.click()
    time.sleep(4)
    try:
        imie = driver.find_element(By.XPATH, "//div[@class='QGPIr']//span")
        imie2 = imie.get_attribute('innerHTML')
        print(imie2)
        imiona.write(imie2)
        imiona.write('\n')

    # print(tablicaimion)
    # driver.close()
    except:
        imiona.write("-------")
        imiona.write('\n')
