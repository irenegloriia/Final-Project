from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import re

myprofile = webdriver.FirefoxProfile('/Users/irenegloriia/Library/Application Support/Firefox/Profiles/egc4m9xh.stockbitScrap')
PATH = "/opt/homebrew/Cellar/geckodriver/0.29.0/bin/geckodriver"
driver = webdriver.Firefox(firefox_profile=myprofile ,executable_path=PATH)

driver.get('https://www.indopremier.com/ipotnews/newsDetail.php?jdl=Rebound__Harga_Emas_Antam_Bertambah_Rp9_Ribu_Gram&news_id=131375&group_news=IPOTNEWS&taging_subtype=PG002&name=&search=y_general&q=,&halaman=1')
time.sleep(5)
list = []
berita = ''
box = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/section/div/div[1]/div[1]/div/div/dl')
paragraf = box.find_elements_by_xpath('/html/body/div[2]/div[2]/section/section/div/div[1]/div[1]/div/div/dl/article')
title = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/section/div/div[1]/div[1]/div/div/dl/dt').text
time = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/section/div/div[1]/div[1]/div/div/dl/div/small').text
link = driver.current_url

print('Judul = ' +title)
print('Waktu = ' +time)
print(link)
for n in range(len(paragraf)):
    berita = berita + paragraf[n].text + ' '
    item = {
            'Judul' : title,
            'Waktu' : time,
            'News' : berita
        }
    list.append(item)
for match in re.finditer('Sumber', berita):
    sumber = match.start()
berita = berita[:sumber]
# df = pd.DataFrame(list)
print(berita)
# df.to_csv('ipot', encoding='utf-8')
driver.quit()
