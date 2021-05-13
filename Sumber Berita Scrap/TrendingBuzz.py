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

driver.get('https://stockbit.com/#/TrendingBuzz')
# time.sleep(5)
target = 300
targetSaham = 'UNVR'
list = []
timeline = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div')
stream = timeline.find_elements_by_xpath(".//div[contains(@class, 'stream-box')]")
print(len(stream))
window = driver.find_elements_by_xpath('/html')
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[3]/div[1]/div[4]/span').click()
sahamSearch = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[3]/div[3]/form/input')
sahamSearch.send_keys(targetSaham, Keys.ENTER)


while len(stream) < target:
    window = driver.find_elements_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div')
    timeline = driver.find_element_by_xpath('//*[@id="stimeline"]')
    stream = timeline.find_elements_by_xpath(".//div[contains(@class, 'stream-box')]")
    print(len(stream))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)", window)
    # driver.execute_script("arguments[0].scrollIntoView();", window)
    time.sleep(1)
print('selesai')

for i in range(1,target):
    textBox = driver.find_element_by_xpath(".//div[contains(@class, 'stream-col-right')]")
    teksPosting = textBox.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div[tr"+s(i)+"]/div[4]/div[3]").text
    dateTime = textBox.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div["+str(i)+"]/div[4]/div[2]/a").text
    print(dateTime)
    print(teksPosting)
    print('=======================================================')
    item = {
        'DateTime' : dateTime,
        'News' : teksPosting
    }
    list.append(item)
    print(str(i)+'.' +dateTime)
    print('selesai')
df = pd.DataFrame(list)
print(df)
df.to_csv('UNVRTrendingBuzz.csv', encoding='utf-8')
driver.quit()
#Icon Comment
                                                   
# streamBoxComment = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div[1]/div[4]/div[5]/div[2]/a[3]')
# streamCount = streamBoxComment.find_element_by_xpath(".//span[contains(@class, 'stream-count1')]").text
# print(int(streamCount))
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div[1]/div[4]/div[5]/div[2]/a[3]').click()

# #Conversation Comment
# timelineConversation= driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[5]/div[4]/div[2]/div[3]')
# boxConversation = timelineConversation.find_elements_by_xpath(".//div[contains(@class, 'stream-box')]")
# print(len(boxConversation))
