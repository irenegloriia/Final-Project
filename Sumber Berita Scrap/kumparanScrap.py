from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)
   
driver.get('https://kumparan.com/topic/saham')
target = 100
list = []
ibu = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/div[2]/div[1]/div/div[1]')
artikel = ibu.find_elements_by_xpath("//div[@data-qa-id='news-item']")
window = driver.find_element_by_xpath('/html')
while (len(artikel) < target):
    ibu = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/div[2]/div[1]/div/div[1]')
    artikel = ibu.find_elements_by_xpath("//div[@data-qa-id='news-item']")
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", window)
    # print(len(artikel))
    time.sleep(1)

for i in range(1,100,2):
    penulis = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div['+str(i)+']/div/div/div[1]/a/div/div/div/div[2]/div/div[1]/span/div/span').text
    if (penulis!="Mohammad Teguh"):
        link = '//*[@id="content"]/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div['+str(i)+']/div/div/div[1]/a'
        a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, link))).get_attribute('href')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(a)
        bungkus = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div[2]/div[2]/div[3]/div/div[3]')
        jumlah = bungkus.find_elements_by_xpath("//span[@class='Textweb__StyledText-sc-1fa9e8r-0 laLMaB']")
        judul = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/h1').text

        for i in range(len(jumlah)):
            print(judul)
            print(jumlah[i].text)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    else:
        print("ADA TEGUH SKIP")
    print('selesai ')
    print(' ')

item = {
        'judul' : judul.text,
        'link' : driver.current_url,
        'isi' : berita
driver.quit()
