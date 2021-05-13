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

driver.get('https://stockbit.com/#/StockbitNews')
time.sleep(5)
target = 100
targetSaham = 'ANTM'
list = []
timeline = driver.find_element_by_xpath('//*[@id="stimeline"]')
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
    time.sleep(1)

for i in range(1,target):
    textBox = driver.find_element_by_xpath(".//div[contains(@class, 'stream-col-right')]")
    teksPosting = textBox.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div["+str(i)+"]/div[4]/div[3]").text
    dateTime = textBox.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div["+str(i)+"]/div[4]/div[2]/a").text
    # print(teksPosting)
    print ('Berita ke-' + str(i))

    if (len(textBox.find_elements_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div["+str(i)+"]/div[4]/span")) > 0) :
        labelField = textBox.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div["+str(i)+"]/div[4]/span")
        if (labelField.text == "Bisnis.com" or labelField.text == "bisnis.com"):
            link = '/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div['+str(i)+']/div[4]/div[3]/div/a'
            a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, link))).get_attribute('href')
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(a)
            try:
                time = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div[2]/div/span").text
                title = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/h1").text
                link = driver.current_url
                box = driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div[5]/div/div[1]")
                paragraf = box.find_elements_by_xpath("./child::*")
                teksPosting = []
                for a in paragraf:
                    if (a.tag_name == "p" or a.tag_name == "table"):
                        if not (a.text[:7]=="Sumber:" or a.text[7:]=="Editor :"):
                            a = a.text.split("\n")
                            a = " ".join(a)
                            teksPosting.append(a)

                teksPosting = " ".join(teksPosting)
            except:
                time = "Bisnis.com Error"
                title = "Bisnis.com Error"
                teksPosting = "Bisnis.com Error"
                link = "Bisnis.com Error"

            print('Waktu', time)
            print('Judul', title)
            print(link)
            print(teksPosting) 
            print("=======================================================================================================================")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        elif (labelField.text == "ipotnews.com"):
            print(dateTime)
            link = '/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div['+str(i)+']/div[4]/div[3]/div/a'
            a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, link))).get_attribute('href')
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(a)
            box = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/section/div/div[1]/div[1]/div/div/dl')
            paragraf = box.find_elements_by_xpath('/html/body/div[2]/div[2]/section/section/div/div[1]/div[1]/div/div/dl/article')
            title = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/section/div/div[1]/div[1]/div/div/dl/dt').text
            time = driver.find_element_by_xpath('/html/body/div[2]/div[2]/section/section/div/div[1]/div[1]/div/div/dl/div/small').text
            link = driver.current_url

            print('Judul = ' +title)
            print('Waktu = ' +time)
            print(link)
            teksPosting = ''
            for n in range(len(paragraf)):
                teksPosting = teksPosting + paragraf[n].text + ' '
            for match in re.finditer('Sumber', teksPosting):
                sumber = match.start()
            teksPosting = teksPosting[:sumber]
            print(teksPosting)
            print("=======================================================================================================================")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        elif (labelField.text == "cnbcindonesia.com"):
            try :
                link = '/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div['+str(i)+']/div[4]/div[3]/div/a'
                a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, link))).get_attribute('href')
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(a)
                box = driver.find_element_by_xpath('/html/body/div[4]/div[2]/article')
                nampung = box.find_element_by_xpath(".//div[@class='detail_text']")
                paragraf = nampung.find_elements_by_tag_name('p')
                time = driver.find_element_by_xpath(".//div[@class='date']").text
                link = driver.current_url

                if (len(driver.find_elements_by_xpath("/html/body/div[4]/div[2]/article/div[3]/div/div/h2")) > 0 ): 
                    title = driver.find_element_by_xpath("/html/body/div[4]/div[2]/article/div[3]/div/div/h1").text
                else : 
                    title = driver.find_element_by_xpath("/html/body/div[4]/div[2]/article/div[1]/div/div/h1").text
                
                teksPosting = ''
                if (len(driver.find_elements_by_xpath("/html/body/div[4]/div[2]/article/div[7]/a/i")) > 0):
                    for n in range(len(paragraf)):
                        if not ("NEXT:" in paragraf[n].text[:5]):
                            teksPosting = teksPosting + paragraf[n].text
                    next = driver.find_element_by_xpath("/html/body/div[4]/div[2]/article/div[7]/a/i")
                    driver.execute_script("arguments[0].scrollIntoView(true);", next )
                    next.click()
                    box = driver.find_element_by_xpath('/html/body/div[4]/div[2]/article')
                    nampung = driver.find_element_by_xpath(".//div[@class='detail_text']")
                    paragraf = nampung.find_elements_by_tag_name('p')

                    for i in range(len(paragraf)):
                        if not ("NEXT:" in paragraf[i].text[:5]):
                            teksPosting = teksPosting + paragraf[i].text 
                else :
                    for i in range(len(paragraf)):
                        if not ("NEXT:" in paragraf[i].text[:5]):
                            teksPosting = teksPosting + paragraf[i].text
            except :
                time = 'error cnbc'
                title = 'error cnbc'
                teksPosting = 'error cnbc'
                link = 'error cnbc'
            teksPosting = teksPosting.replace('Jakarta, CNBC Indonesia - ','')
            teksPosting = teksPosting.replace('TIM RISET CNBC INDONESIA','')   
            print('Judul = ' +title)
            print('Waktu = ' +time)
            print(link)
            print(teksPosting)
            print("=======================================================================================================================")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        elif (labelField.text == "kontan.co.id"):
            link = '/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div['+str(i)+']/div[4]/div[3]/div/a'
            a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, link))).get_attribute('href')
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(a)
            artikel = driver.find_element_by_class_name('tmpt-desk-kon')
            isi = artikel.find_elements_by_tag_name('p')
            title = driver.find_element_by_class_name('detail-desk').text
            #time = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div[2]').text
            #time = driver.find_element_by_xpath('html/body/div[2]/div[2]/div[1]/div[1]/div[2]').text
            if (len(driver.find_elements_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div[2]")) > 0 ): 
                time = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[1]/div[2]").text
            else : 
                time = driver.find_element_by_xpath("html/body/div[2]/div[2]/div[1]/div[1]/div[2]").text
                                                        
            link = driver.current_url
            teksPosting = ''
            for n in range(1, len(isi)):
                if(isi[n].text[:9] != "Baca Juga"):
                    teksPosting= teksPosting + isi[n].text + ' '
            print('Judul = ' +title)
            print('Waktu = ' +time)
            print(link)
            print(teksPosting)
            print("=======================================================================================================================")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        elif (labelField.text == "kompas.com"):
            try :
                link = '/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div['+str(i)+']/div[4]/div[3]/div/a'
                a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, link))).get_attribute('href')
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(a)
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
                teksPosting = ''
                for n in range(len(paragraf)):
                    if not ("Baca jug" in paragraf[n].text[:9]):
                        teksPosting = teksPosting + paragraf[n].text + ''
            except :
                time = 'error kompas'
                title = 'error kompas'
                teksPosting = 'error kompas'
                link = 'error'
            print('Judul = ' +title)
            print('Waktu = ' +time)
            print(link)
            print('Isi = ' +teksPosting)
            print("=======================================================================================================================")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        elif (labelField.text == "indotelko.com"):
            try :
                link = '/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div['+str(i)+']/div[4]/div[3]/div/a'
                a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, link))).get_attribute('href')
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(a)
                teksPosting = driver.find_element_by_xpath("//div[@id='font_news']").text
                teks2 = teksPosting.find_element_by_xpath('//*[@id="box_bj"]')
                title = driver.find_element_by_xpath('//*[@id="title"]').text
                time = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div[4]').text
                link = driver.current_url

                if (len(driver.find_elements_by_xpath("/html/body/div[1]/div[4]/div[1]/div[4]")) > 0 ): 
                    time = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[1]/div[4]").text
                else : 
                    time = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[5]/div[1]/div[4]").text
                print('Judul = ' +title)
                print('Waktu = ' +time)
                print(link)
                print(teksPosting.text.replace(teks2.text, ''))
                print("=======================================================================================================================")
            except :
                time = 'indotelko error'
                title = 'indotelko error'
                teksPosting = 'indotelko error'
                link = 'indotelko error'
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
           

        elif (labelField.text == "neraca.co.id"):
            link = '/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[5]/div/div['+str(i)+']/div[4]/div[3]/div/a'
            a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, link))).get_attribute('href')
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(a)
            box = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div')
            paragraf = box.find_elements_by_tag_name('p')
            title = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/h1').text
            time = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/span[2]').text
            link = driver.current_url
            
            print('Judul = ' +title)
            print('Waktu = ' +time)
            print(link)
            teksPosting = ''
            for n in range(len(paragraf)):
                teksPosting = teksPosting + paragraf[n].text + ' '
            print(teksPosting)
            print("=======================================================================================================================")
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        else :
            time = 'error nih'
            title = 'error nih'
            teksPosting = 'error'
            link = 'error'
    else : 
        time = 'error realstockbit'
        title = 'error realstockbit'
        teksPosting = 'realstockbit'
        link = 'realstockbit'
        print("=======================================================================================================================")
    item = {
        'DateTime' : time,
        'Judul' : title,
        'link' : link,
        'News' : teksPosting
    }
    list.append(item)
print('selesai')
df = pd.DataFrame(list)
print(df)
df.to_csv('ANTM1.csv', encoding='utf-8')
driver.quit()