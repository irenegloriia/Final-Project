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

driver.get('https://market.bisnis.com/read/20190926/189/1152553/rekomendasi-sinarmas-hold-aces-buy-on-weakness-bbca-cpin-smgr')
time.sleep(5)
time = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div[2]/div/span").text
title = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/h1").text
link = driver.current_url
box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div[5]/div/div[1]")
paragraf = box.find_elements_by_xpath("./child::*")
teksPosting = []
list = []
for a in paragraf:
    if (a.tag_name == "p" or a.tag_name == "table"):
        if not (a.text[:7]=="Sumber:" or a.text[7:]=="Editor :"):
            a = a.text.split("\n")
            a = " ".join(a)
            teksPosting.append(a)

teksPosting = " ".join(teksPosting)
item = {
    'News' : teksPosting
}
list.append(item)
# print(str(i)+'.' +dateTime)
print('selesai')

print(time)
print(title)
print(link)
print(teksPosting)

df = pd.DataFrame(list)
print(df)
df.to_csv('bisnis.csv', encoding='utf-8')
driver.quit()