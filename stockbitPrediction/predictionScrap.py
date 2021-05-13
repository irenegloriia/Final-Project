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

All = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div[2]/a[5]/span').click()
# time.sleep(5)
target = 20
targetSaham = 'antm'
# list = []
timeline = driver.find_element_by_xpath('//*[@id="stimeline"]')
stream = timeline.find_elements_by_xpath(".//div[contains(@class, 'stream-box')]")
print(len(stream))
window = driver.find_elements_by_xpath('/html')                             
driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div[4]/span[1]').click()
sahamSearch = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[4]/div[3]/form/input')
sahamSearch.send_keys(targetSaham, Keys.ENTER)
sahamSearch.send_keys(Keys.ENTER)
time.sleep(2)
while len(stream) < target: 
    window = driver.find_elements_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]')
    timeline = driver.find_element_by_xpath('//*[@id="stimeline"]')
    stream = timeline.find_elements_by_xpath(".//div[contains(@class, 'stream-box')]")
    print(len(stream))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)", window)
    time.sleep(1)
print('selesai scroll')
for i in range(1,target):
    box = driver.find_element_by_xpath(".//div[contains(@class, 'stream-username')]")
    username = box.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div/div[4]/div[1]/a[1]/b").text  
    boxDate = driver.find_element_by_xpath(".//div[contains(@class, 'stream-date')]")
    date = boxDate.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div[1]/div/div[1]/div[4]/div[2]/a").text
    date1 = boxDate.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div/div[4]/div[2]/a").text
    saham = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div/div[4]/div[5]/div[2]/div/h3").text
    perusahaan = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div/div[4]/div[5]/div[2]/div/span").text
    tipe = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div[1]/div[4]/div[5]/div[2]/p").text
    targetprice = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div[1]/div[4]/div[5]/div[4]/div/h2").text
    if (len(driver.find_elements_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div/div[4]/div[5]/div[3]/span/a")) > 0 ):
        result = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div[1]/div[4]/div[5]/div[3]").text
    elif (len(driver.find_elements_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div[1]/div[4]/div[5]/div[3]/img")) > 0 ) :
        image = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div[1]/div[4]/div[5]/div[3]/img").get_attribute("src")    
        if (image == 'https://my.stockbit.com/assets/img/settargetprice/correct.png'):
            result = 'Hit'
        else :
            result = 'Missed'
    else :
        print('IHSG')
    print(username)                        
    print(date1)
    print(saham , perusahaan)
    print(tipe , targetprice,result)
    print('========')


    # image = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div[2]/div/div/div[4]/div[5]/div[3]/img").get_attribute("src")    
    # print(image)



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