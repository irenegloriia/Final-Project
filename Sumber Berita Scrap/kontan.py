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

driver.get('https://investasi.kontan.co.id/news/communication-cable-systems-ccsi-akan-rights-issue-efek-dilusi-maksimal-1453')

artikel = driver.find_element_by_class_name('tmpt-desk-kon')
isi = artikel.find_elements_by_tag_name('p')
title = driver.find_element_by_class_name('detail-desk').text
time = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div[2]').text
link = driver.current_url
berita = ''
for n in range(1, len(isi)):
    if(isi[n].text[:9] != "Baca Juga"):
        berita = berita + isi[n].text + ' '

berita = berita.replace('KONTAN.CO.ID -  JAKARTA.','')
print('Judul = ' +title)
print('Waktu = ' +time)
print(link)
print(berita)