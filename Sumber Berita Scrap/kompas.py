from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

myprofile = webdriver.FirefoxProfile('/Users/irenegloriia/Library/Application Support/Firefox/Profiles/egc4m9xh.stockbitScrap')
PATH = "/opt/homebrew/Cellar/geckodriver/0.29.0/bin/geckodriver"
driver = webdriver.Firefox(firefox_profile=myprofile ,executable_path=PATH)

# driver.get('https://money.kompas.com/read/2021/03/23/210000926/bantu-penanggulangan-covid-19-taspen-sumbang-dua-ambulans-ke-polri-dan-bkn')
# driver.get('https://money.kompas.com/read/2021/03/15/192657126/antm-raih-laba-rp-141-triliun-di-tahun-2020')
driver.get('https://money.kompas.com/read/2021/03/22/124329526/rupiah-dan-ihsg-terperosok-asing-lepas-bbca-asii-dan-smgr?page=all#page2')
time.sleep(5)
list = []
berita = ''

if (len(driver.find_elements_by_xpath("/html/body/div[1]/div[3]/div[3]/div[1]/div[4]/div[2]/div[7]/div/div[3]")) > 0):
    showAll = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[1]/div[4]/div[2]/div[7]/div/div[3]')
    driver.execute_script("arguments[0].scrollIntoView(true);", showAll )
    showAll.click()
    time.sleep(10)
box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[1]/div[4]/div[2]/div[2]/div[1]')
paragraf = box.find_elements_by_tag_name('p')
title = driver.find_element_by_xpath("//h1[@class='read__title']").text
time = driver.find_element_by_xpath("//div[@class='read__time']").text
link = driver.current_url
for n in range(len(paragraf)):
    if not ("Baca jug" in paragraf[n].text[:9]):
        berita = berita + paragraf[n].text + ''
print('Judul = ' +title)
print('Waktu = ' +time)
print(link)
print('Isi = ' +berita)

driver.quit()