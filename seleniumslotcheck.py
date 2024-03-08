import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

import time

def check():
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/p").text
        print (elem)
        if "No appointments are available at the moment but slots will be posted in the coming days." == elem:
            print ("Slot yok")
            time.sleep(3)
        # Telegram veya mail kodu buraya
        else:
            print ("Telegram mesa att")
            exit()
    except:
        print ("yine bakmakta fayda var telegra mesaj at")
        exit()
        # Telegram veya mail kodu buraya
def backandforw():
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[1]/button/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[1]/button/span").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div/div[4]/button").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/div[2]/button").click()

driver = uc.Chrome()
driver.get("https://consulat.gouv.fr/ambassade-de-france-en-irlande/rendez-vous?name=Visas")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div/div/div/div[2]/div[2]/div/button").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div/div/div/div[2]/div[2]/div/ul/li[1]").click()
time.sleep(10)
print("captcha please")
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div/div[4]/button").click()
time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/div[1]/div/label").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div/div[2]/button").click()
while 1:
    check()
    backandforw()
