from selenium import webdriver 
from selenium.webdriver.chrome.service import Service   # 4 importy dotyczące biblioteki selenium, które pozwolą nam na któtsze... 
from webdriver_manager.chrome import ChromeDriverManager #  ...zapisywanie komend
from selenium.webdriver.common.by import By

strony = [] # lista do której będziemy zapisywać linki do stron

# w range max 148 bo tyle jest stron
for i in range(148): 
    url = "https://ddob.com/ranking/instagram/page/"+str(i+250) # pętla, która tworzy linki do strony, z której zbieramy dane
    strony.append(url)

nazwy = open('nazwy.txt', 'a+') # plik tekstowy, w którym zapisywane będą nazwy kont 
obs = open('obs.txt', 'a+') # plik tekstowy, w którym zapisywana będzie liczba obserwujących konto danego influencera

for url in strony: # pętla, która pozwala na przeprowadzenie znajdujących w niej operacji dla każdej podstrony 

    driver = webdriver.Chrome() # ustawienie aby bot działał na przeglądarce Chrome
    driver.get(url) # Chrome otwiera url 

    kontener = [driver.find_elements(By.CLASS_NAME, 'listContainer')]   # opis w dokumentacji
    nicks = driver.find_elements(By.XPATH, "//div[@class='nickName']")  

    for element in driver.find_elements(By.XPATH, "//div[@class='nickName']"):
        element_contents = element.get_attribute('innerHTML')
        e = (((element_contents.replace(
            "</span>", "").replace("<span>", "").replace("\n", ""))))

        nazwy.write(e) # zapis nazwy konta do pliku
        nazwy.write('\n') # zapisa ENTERa, aby dane były przejrzyste

    liczby = driver.find_elements(By.XPATH, "//div[@class='stats']") 

    for element in driver.find_elements(By.XPATH, "//div[@class='stats']"):
        element_contents = element.get_attribute('innerHTML')
        e = (((element_contents.replace("</span>", "").replace("<span>",
             "").replace("&nbsp;", "").replace("\n", ""))))

        obs.write(e) # zapis ilczby obserwujących do pliku
        obs.write('\n') # zapis ENTERa



