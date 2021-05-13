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

#driver.get('https://www.cnbcindonesia.com/market/20210323144940-17-232242/heboh-tesla-ini-bocoran-target-harga-antm-inco-cs-dari-clsa') #link bisa
#driver.get('https://www.cnbcindonesia.com/market/20210318144742-19-231149/di-ghosting-tesla-dipinang-toyota-cs') #link masalah
driver.get('https://www.cnbcindonesia.com/market/20210322092639-17-231788/jangan-kaget-saham-emiten-emas-antm-mdka-cs-jeblok-terus')
time.sleep(5)
list = []
box = driver.find_element_by_xpath('/html/body/div[4]/div[2]/article')
nampung = driver.find_element_by_xpath(".//div[@class='detail_text']")
paragraf = nampung.find_elements_by_tag_name('p')
time = driver.find_element_by_xpath(".//div[@class='date']").text
link = driver.current_url

if (len(driver.find_elements_by_xpath("/html/body/div[4]/div[2]/article/div[3]/div/div/h2")) > 0 ): 
    title = driver.find_element_by_xpath("/html/body/div[4]/div[2]/article/div[3]/div/div/h1").text
else : 
    title = driver.find_element_by_xpath("/html/body/div[4]/div[2]/article/div[1]/div/div/h1").text

berita1 = ''
if (len(driver.find_elements_by_xpath("/html/body/div[4]/div[2]/article/div[7]/a/i")) > 0):
    for n in range(len(paragraf)):
        if not ("NEXT:" in paragraf[n].text[:5]):
            berita1 = berita1 + paragraf[n].text
    next = driver.find_element_by_xpath("/html/body/div[4]/div[2]/article/div[7]/a/i")
    driver.execute_script("arguments[0].scrollIntoView(true);", next )
    next.click()
    box = driver.find_element_by_xpath('/html/body/div[4]/div[2]/article')
    nampung = driver.find_element_by_xpath(".//div[@class='detail_text']")
    paragraf = nampung.find_elements_by_tag_name('p')

    for i in range(len(paragraf)):
        if not ("NEXT:" in paragraf[i].text[:5]):
            berita1 = berita1 + paragraf[i].text  

else :
    for i in range(len(paragraf)):
        if not ("NEXT:" in paragraf[i].text[:5]):
            berita1 = berita1 + paragraf[i].text  
print('Judul = ' +title)
print('Waktu = ' +time)
print(link)
berita1 = berita1.replace('Jakarta, CNBC Indonesia - ','')
berita1 = berita1.replace('TIM RISET CNBC INDONESIA','')
print(berita1)
driver.quit()