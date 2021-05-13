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

driver.get('https://stockbit.com/#/stream')

All = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div[2]/a[1]/span').click()
# time.sleep(5)
target = 20
targetSaham = 'antm'
# list = []
timeline = driver.find_element_by_xpath('//*[@id="stimeline"]')
stream = timeline.find_elements_by_xpath(".//div[contains(@class, 'stream-box')]")
window = driver.find_elements_by_xpath('/html')                             

time.sleep(5)                          
if (len(driver.find_elements_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div[1]/div/div/div[4]/div[5]/div/a[3]")) > 0 ): 
    driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div[1]/div/div/div[4]/div[5]/div/a[3]").click()
else :
    print('skip')

box = driver.find_element_by_xpath(".//div[contains(@class, 'stream-username')]")

#Conversation Right
time.sleep(5) 
convWindow = driver.find_element_by_xpath('//*[@id="conversation-child"]')

conv = convWindow.find_elements_by_xpath(".//div[contains(@class, 'stream-username')]")
print('jumlah komen', len(conv))
time.sleep(5)

boxDate = driver.find_element_by_xpath(".//div[contains(@class, 'stream-date')]")
date1 = boxDate.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[5]/div[4]/div[2]/div[3]/div[1]/div[4]/div[2]/a").text
box = driver.find_element_by_xpath(".//div[contains(@class, 'stream-username')]")
textComment = box.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[5]/div[4]/div[2]/div[3]/div[1]/div[4]/div[3]").text
username = box.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[5]/div[4]/div[2]/div[3]/div/div[4]/div[1]/a[1]/b").text  
print(date1)
print(username)
print(textComment)

# for i in range(1,target):
#     textBox = driver.find_element_by_xpath(".//div[contains(@class, 'stream-col-right')]")
#     teksPosting = textBox.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div["+str(i)+"]/div[4]/div[3]").text
#     dateTime = textBox.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div["+str(i)+"]/div[4]/div[2]/a").text
#     print(dateTime)
#     print(teksPosting)
#     print('=======================================================')
#     item = {
#         'DateTime' : dateTime,
#         'News' : teksPosting
#     }
#     list.append(item)
#     print(str(i)+'.' +dateTime)
#     print('selesai')
# df = pd.DataFrame(list)
# print(df)
# df.to_csv('UNVRTrendingBuzz.csv', encoding='utf-8')
# driver.quit()