from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get('https://id.investing.com/news/stock-market-news')
time.sleep(3)
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="PromoteSignUpPopUp"]/div[2]/i'))).click()
bungkus = driver.find_element_by_xpath('//*[@id="leftColumn"]/div[4]')
jumlah = bungkus.find_elements_by_tag_name('article')
print(len(jumlah))
for j in range(3):
    for i in range(1,len(jumlah)+1):
        artikel1 = driver.find_element_by_xpath('//*[@id="leftColumn"]/div[4]/article['+str(i)+']')
        judul = driver.find_element_by_xpath('//*[@id="leftColumn"]/div[4]/article['+str(i)+']/div[1]/a').text
        if("js-article-item articleItem   " == artikel1.get_attribute('class')):
            print(judul + " Bisa di scrape")
        else :
            print(judul + " Tidak Bisa di scrape")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="PromoteSignUpPopUp"]/div[2]/i'))).click()
    driver.find_element_by_xpath('//*[@id="paginationWrap"]/div[3]/a').click()
    time.sleep(3)


# while (len(artikel) < target):
   
#     window = driver.find_element_by_xpath('/html')
#     driver.execute_script("return arguments[0].scrollIntoView(true);", window)
#     isi = driver.find_element_by_class_name('largeTitle')
#     artikel = isi.find_elements_by_tag_name('article')
#     driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", window)
#     print(len(artikel))
#     time.sleep(1)

#     driver.find_element_by_xpath('//*[@id="paginationWrap"]/div[3]/a').click()

# driver.execute_script("return arguments[0].scrollIntoView(true);", window)
# for i in range(1,target+1):
#     link = '//*[@id="leftColumn"]/div[4]/article['+str(i)+']/div[1]/a'
#     a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
#         (By.XPATH, link))).get_attribute('href')
#     # print(str(i) + '. '+a)
#     driver.execute_script("window.open('');") #openNewTab
#     driver.switch_to.window(driver.window_handles[1]) #moveToNewTab
#     driver.get(a)
#     artikel = driver.find_element_by_class_name('tmpt-desk-kon')
#     isi = artikel.find_elements_by_tag_name('p')
#     judul = driver.find_element_by_class_name('detail-desk')
#     berita = ''
#     for n in range(1, len(isi)):
#         berita = berita + isi[n].text
#     item = {
#         'judul' : judul.text,
#         'link' : driver.current_url,
#         'isi' : berita
#     }
#     list.append(item)
#     print(str(i)+'. ' +judul.text)
#     driver.close()
#     driver.switch_to.window(driver.window_handles[0])
#     print('selesai')
# df = pd.DataFrame(list)
# print(df)
# df.to_csv('dataset_kontan.csv', encoding='utf-8')
# driver.quit() 