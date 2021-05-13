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

Saham = ['AALI', 'ABBA', 'ABDA', 'ABMM', 'ACES', 'ACST', 'ADES', 'ADHI', 'ADMF', 'ADMG', 'ADRO', 'AGAR', 'AGII', 'AGRO', 'AGRS', 'AHAP', 'AIMS', 'AISA', 'AKKU', 'AKPI', 'AKRA', 'AKSI', 'ALDO', 'ALKA', 'ALMI', 'ALTO', 'AMAG', 'AMAN', 'AMAR', 'AMFG', 'AMIN', 'AMOR', 'AMRT', 'ANDI', 'ANJT', 'ANTM', 'APEX', 'APIC', 'APII', 'APLI', 'APLN', 'ARGO', 'ARII', 'ARKA', 'ARMY', 'ARNA', 'ARTA', 'ARTI', 'ARTO', 'ASBI', 'ASDM', 'ASGR', 'ASII', 'ASJT', 'ASMI', 'ASPI', 'ASRI', 'ASRM', 'ASSA', 'ATAP', 'ATIC', 'AUTO', 'AYLS', 'BABP', 'BACA', 'BAJA', 'BALI', 'BANK', 'BAPA', 'BAPI', 'BATA', 'BAYU', 'BBCA', 'BBHI', 'BBKP', 'BBLD', 'BBMD', 'BBNI', 'BBRI', 'BBRM', 'BBSI', 'BBSS', 'BBTN', 'BBYB', 'BCAP', 'BCIC', 'BCIP', 'BDMN', 'BEBS', 'BEEF', 'BEKS', 'BELL', 'BESS', 'BEST', 'BFIN', 'BGTG', 'BHAT', 'BHIT', 'BIKA', 'BIMA', 'BINA', 'BIPI', 'BIPP', 'BIRD', 'BISI', 'BJBR', 'BJTM', 'BKDP', 'BKSL', 'BKSW', 'BLTA', 'BLTZ', 'BLUE', 'BMAS', 'BMRI', 'BMSR', 'BMTR', 'BNBA', 'BNBR', 'BNGA', 'BNII', 'BNLI', 'BOGA', 'BOLA', 'BOLT', 'BOSS', 'BPFI', 'BPII', 'BPTR', 'BRAM', 'BRIS', 'BRMS', 'BRNA', 'BRPT', 'BSDE', 'BSIM', 'BSSR', 'BSWD', 'BTEK', 'BTEL', 'BTON', 'BTPN', 'BTPS', 'BUDI', 'BUKK', 'BULL', 'BUMI', 'BUVA', 'BVIC', 'BWPT', 'BYAN', 'CAKK', 'CAMP', 'CANI', 'CARE', 'CARS', 'CASA', 'CASH', 'CASS', 'CBMF', 'CCSI', 'CEKA', 'CENT', 'CFIN', 'CINT', 'CITA', 'CITY', 'CLAY', 'CLEO', 'CLPI', 'CMNP', 'CMPP', 'CNKO', 'CNTX', 'COCO', 'COWL', 'CPIN', 'CPRI', 'CPRO', 'CSAP', 'CSIS', 'CSMI', 'CSRA', 'CTBN', 'CTRA', 'CTTH', 'DADA', 'DART', 'DAYA', 'DCII', 'DEAL', 'DEFI', 'DEWA', 'DFAM', 'DGIK', 'DGNS', 'DIGI', 'DILD', 'DIVA', 'DKFT', 'DLTA', 'DMAS', 'DMMX', 'DMND', 'DNAR', 'DNET', 'DOID', 'DPNS', 'DPUM', 'DSFI', 'DSNG', 'DSSA', 'DUCK', 'DUTI', 'DVLA', 'DWGL', 'DYAN', 'EAST', 'ECII', 'EDGE', 'EKAD', 'ELSA', 'ELTY', 'EMDE', 'EMTK', 'ENRG', 'ENVY', 'ENZO', 'EPAC', 'EPMT', 'ERAA', 'ERTX', 'ESIP', 'ESSA', 'ESTA', 'ESTI', 'ETWA', 'EXCL', 'FAPA', 'FAST', 'FASW', 'FILM', 'FINN', 'FIRE', 'FISH', 'FITT', 'FMII', 'FOOD', 'FORU', 'FORZ', 'FPNI', 'FREN', 'FUJI', 'GAMA', 'GDST', 'GDYR', 'GEMA', 'GEMS', 'GGRM', 'GGRP', 'GHON', 'GIAA', 'GJTL', 'GLOB', 'GLVA', 'GMFI', 'GMTD', 'GOLD', 'GOLL', 'GOOD', 'GPRA', 'GSMF', 'GTBO', 'GWSA', 'GZCO', 'HADE', 'HDFA', 'HDIT', 'HDTX', 'HEAL', 'HELI', 'HERO', 'HEXA', 'HITS', 'HKMU', 'HMSP', 'HOKI', 'HOME', 'HOMI', 'HOTL', 'HRME', 'HRTA', 'HRUM', 'IATA', 'IBFN', 'IBST', 'ICBP', 'ICON', 'IDPR', 'IFII', 'IFSH', 'IGAR', 'IIKP', 'IKAI', 'IKAN', 'IKBI', 'IMAS', 'IMJS', 'IMPC', 'INAF', 'INAI', 'INCF', 'INCI', 'INCO', 'INDF', 'INDO', 'INDR', 'INDS', 'INDX', 'INDY', 'INKP', 'INOV', 'INPC', 'INPP', 'INPS', 'INRU', 'INTA', 'INTD', 'INTP', 'IPCC', 'IPCM', 'IPOL', 'IPTV', 'IRRA', 'ISAT', 'ISSP', 'ITIC', 'ITMA', 'ITMG', 'JAST', 'JAWA', 'JAYA', 'JECC', 'JGLE', 'JIHD', 'JKON', 'JKSW', 'JMAS', 'JPFA', 'JRPT', 'JSKY', 'JSMR', 'JSPT', 'JTPE', 'KAEF', 'KARW', 'KAYU', 'KBAG', 'KBLI', 'KBLM', 'KBLV', 'KBRI', 'KDSI', 'KEEN', 'KEJU', 'KIAS', 'KICI', 'KIJA', 'KINO', 'KIOS', 'KJEN', 'KKGI', 'KLBF', 'KMDS', 'KMTR', 'KOBX', 'KOIN', 'KONI', 'KOPI', 'KOTA', 'KPAL', 'KPAS', 'KPIG', 'KRAH', 'KRAS', 'KREN', 'LAND', 'LAPD', 'LCGP', 'LCKM', 'LEAD', 'LIFE', 'LINK', 'LION', 'LMAS', 'LMPI', 'LMSH', 'LPCK', 'LPGI', 'LPIN', 'LPKR', 'LPLI', 'LPPF', 'LPPS', 'LRNA', 'LSIP', 'LTLS', 'LUCK', 'MABA', 'MAGP', 'MAIN', 'MAMI', 'MAPA', 'MAPB', 'MAPI', 'MARI', 'MARK', 'MASA', 'MAYA', 'MBAP', 'MBSS', 'MBTO', 'MCAS', 'MCOR', 'MDIA', 'MDKA', 'MDKI', 'MDLN', 'MDRN', 'MEDC', 'MEGA', 'MERK', 'META', 'MFIN', 'MFMI', 'MGNA', 'MGRO', 'MICE', 'MIDI', 'MIKA', 'MINA', 'MIRA', 'MITI', 'MKNT', 'MKPI', 'MLBI', 'MLIA', 'MLPL', 'MLPT', 'MMLP', 'MNCN', 'MOLI', 'MPMX', 'MPOW', 'MPPA', 'MPRO', 'MRAT', 'MREI', 'MSIN', 'MSKY', 'MTDL', 'MTFN', 'MTLA', 'MTPS', 'MTRA', 'MTSM', 'MTWI', 'MYOH', 'MYOR', 'MYRX', 'MYTX', 'NASA', 'NATO', 'NELY', 'NFCX', 'NICK', 'NIKL', 'NIPS', 'NIRO', 'NISP', 'NOBU', 'NRCA', 'NUSA', 'NZIA', 'OASA', 'OCAP', 'OKAS', 'OMRE', 'OPMS', 'PADI', 'PALM', 'PAMG', 'PANI', 'PANR', 'PANS', 'PBID', 'PBRX', 'PBSA', 'PCAR', 'PDES', 'PEGE', 'PEHA', 'PGAS', 'PGJO', 'PGLI', 'PGUN', 'PICO', 'PJAA', 'PKPK', 'PLAN', 'PLAS', 'PLIN', 'PMJS', 'PMMP', 'PNBN', 'PNBS', 'PNGO', 'PNIN', 'PNLF', 'PNSE', 'POLA', 'POLI', 'POLL', 'POLU', 'POLY', 'POOL', 'PORT', 'POSA', 'POWR', 'PPGL', 'PPRE', 'PPRO', 'PRAS', 'PRDA', 'PRIM', 'PSAB', 'PSDN', 'PSGO', 'PSKT', 'PSSI', 'PTBA', 'PTDU', 'PTIS', 'PTPP', 'PTPW', 'PTRO', 'PTSN', 'PTSP', 'PUDP', 'PURA', 'PURE', 'PURI', 'PWON', 'PYFA', 'PZZA', 'RAJA', 'RALS', 'RANC', 'RBMS', 'RDTX', 'REAL', 'RELI', 'RICY', 'RIGS', 'RIMO', 'RISE', 'RMBA', 'ROCK', 'RODA', 'RONY', 'ROTI', 'RUIS', 'SAFE', 'SAME', 'SAMF', 'SAPX', 'SATU', 'SBAT', 'SCCO', 'SCMA', 'SCNP', 'SCPI', 'SDMU', 'SDPC', 'SDRA', 'SFAN', 'SGER', 'SGRO', 'SHID', 'SHIP', 'SIDO', 'SILO', 'SIMA', 'SIMP', 'SINI', 'SIPD', 'SKBM', 'SKLT', 'SKRN', 'SKYB', 'SLIS', 'SMAR', 'SMBR', 'SMCB', 'SMDM', 'SMDR', 'SMGR', 'SMKL', 'SMMA', 'SMMT', 'SMRA', 'SMRU', 'SMSM', 'SOCI', 'SOFA', 'SOHO', 'SONA', 'SOSS', 'SOTS', 'SPMA', 'SPTO', 'SQMI', 'SRAJ', 'SRIL', 'SRSN', 'SRTG', 'SSIA', 'SSMS', 'SSTM', 'STAR', 'STTP', 'SUGI', 'SULI', 'SUPR', 'SURE', 'SWAT', 'TALF', 'TAMA', 'TAMU', 'TARA', 'TAXI', 'TBIG', 'TBLA', 'TBMS', 'TCID', 'TCPI', 'TDPM', 'TEBE', 'TECH', 'TELE', 'TFAS', 'TFCO', 'TGKA', 'TGRA', 'TIFA', 'TINS', 'TIRA', 'TIRT', 'TKIM', 'TLKM', 'TMAS', 'TMPO', 'TNCA', 'TOBA', 'TOPS', 'TOTL', 'TOTO', 'TOWR', 'TOYS', 'TPIA', 'TPMA', 'TRAM', 'TRIL', 'TRIM', 'TRIN', 'TRIO', 'TRIS', 'TRJA', 'TRST', 'TRUK', 'TRUS', 'TSPC', 'TUGU', 'TURI', 'UANG', 'UCID', 'UFOE', 'ULTJ', 'UNIC', 'UNIQ', 'UNIT', 'UNSP', 'UNTR', 'UNVR', 'URBN', 'VICI', 'VICO', 'VINS', 'VIVA', 'VOKS', 'VRNA', 'WAPO', 'WEGE', 'WEHA', 'WICO', 'WIFI', 'WIIM', 'WIKA', 'WINS', 'WMUU', 'WOMF', 'WOOD', 'WOWS', 'WSBP', 'WSKT', 'WTON', 'YELO', 'YPAS', 'YULE', 'ZBRA', 'ZINC', 'ZONE']
All = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div[2]/a[1]/span').click()
# time.sleep(5)
target = 1000
# targetSaham = 'antm'
list = []
timeline = driver.find_element_by_xpath('//*[@id="stimeline"]')
stream = timeline.find_elements_by_xpath(".//div[contains(@class, 'stream-box')]")
print(len(stream))
window = driver.find_elements_by_xpath('/html')                             
# driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[4]/div[1]/div[4]/span[1]').click()
# sahamSearch = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[4]/div[3]/form/input')
# sahamSearch.send_keys(targetSaham, Keys.ENTER)


while len(stream) < target: 
    window = driver.find_elements_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[1]/div[1]/div[2]')
    timeline = driver.find_element_by_xpath('//*[@id="stimeline"]')
    stream = timeline.find_elements_by_xpath(".//div[contains(@class, 'stream-box')]")
    print(len(stream))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)", window)
    time.sleep(1)
print('selesai scroll')
time.sleep(2)
# Icon
for i in range(1,target):                   
    if (len(driver.find_elements_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div/div[4]/div[5]/div/a[3]")) > 0 ): 
        box = driver.find_element_by_xpath(".//div[contains(@class, 'stream-username')]")
        usernamePost = box.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div/div[4]/div[1]/a[1]/b").text  
        boxDate = driver.find_element_by_xpath(".//div[contains(@class, 'stream-date')]")
        datePost = boxDate.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div/div[4]/div[2]/a").text
        posting = box.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div[1]/div[4]/div[3]").text
        posting = posting
        count = box.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div/div[4]/div[5]/div/a[3]").text
        # else :
            # print('count skip')
        print(usernamePost) 
        print(datePost)
        print(posting)

        masuk = False
        stop = [",", ".", "#", "?", "*", "-","$"]
        cek = posting
        bahas = []
        akumulasi = {}
        for x in stop:
            cek = cek.replace(x, " ")
        for x in posting:
            b = x.isascii()
            if not b:
                posting = posting.replace(x, ' ')
        if any(word in cek.upper().split() for word in Saham):
            masuk = True
        if(masuk):
            bahas = [word for word in Saham if word in cek.upper().split()]
            for a in bahas :
                if a in akumulasi:
                    akumulasi[a]+=1
                else :
                    akumulasi[a]=1
            bahas = ",".join(bahas)
            print('SAHAM', bahas)
            print("+++++++++++++++")

        # print('jumlah count' , count)
        if (count == ''):
            count = 0
            if (count == 0):
                username = 'Tidak ada'
                date1 = 'Tidak ada'
                textComment = 'Tidak'
        else :     
            count = int(count)
        print('jumlah komen', count)
        # print('========')
        if (1 <= count <= 16 ):
            driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div/div[4]/div[5]/div/a[3]").click()
            time.sleep(5)
            for i in range(1,(count+1)):
                boxDate = driver.find_element_by_xpath(".//div[contains(@class, 'stream-date')]")
                date1 = boxDate.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[5]/div[4]/div[2]/div[3]/div["+str(i)+"]/div[4]/div[2]/a").text
                box = driver.find_element_by_xpath(".//div[contains(@class, 'stream-username')]")
                textComment = box.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[5]/div[4]/div[2]/div[3]/div["+str(i)+"]/div[4]/div[3]").text
                username = box.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[5]/div[4]/div[2]/div[3]/div["+str(i)+"]/div[4]/div[1]/a[1]").text  
                
                print(date1)
                print(username)
                print(textComment)
                print('========')
            driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[5]/div[2]/div/div/div/div[2]/div/i").click()

        else :
            driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[6]/div/div["+str(i)+"]/div/div/div[4]/div[5]/div/a[3]").click() # icon coment
            time.sleep(5)
            belum = True 
            while belum :
                if (len(driver.find_elements_by_xpath(".//div[contains(@class, 'stream-box load-prev')]")) > 0) :
                    load = driver.find_element_by_xpath(".//div[contains(@class, 'stream-box load-prev')]")
                    load.click()
                    time.sleep(20)
                else : 
                    belum = False
            for i in range(1,(count+1)):
                boxDate = driver.find_element_by_xpath(".//div[contains(@class, 'stream-date')]")
                date1 = boxDate.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[5]/div[4]/div[2]/div[3]/div["+str(i)+"]/div[4]/div[2]/a").text
                box = driver.find_element_by_xpath(".//div[contains(@class, 'stream-username')]")
                textComment = box.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[5]/div[4]/div[2]/div[3]/div["+str(i)+"]/div[4]/div[3]").text
                username = box.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[5]/div[4]/div[2]/div[3]/div["+str(i)+"]/div[4]/div[1]/a[1]").text  
                
                print(date1)
                print(username)
                print(textComment)
                print('========')
            driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div[5]/div[2]/div/div/div/div[2]/div/i").click() # tombol close
        print('+++++++++++++++++++++++++++++++++++++++++++++')
    else :
        print('skip')

    item = {
        # 'UsernamePost' : usernamePost,
        # 'DatePosting' : datePost,
        # 'Posting' : posting,
        'UsernameComment' : username,
        'DateComment' : date1,
        'Comment' : textComment,
        'Saham' : bahas
    }
    list.append(item)
print('SELESAI')
df = pd.DataFrame(list)
print(df)
df.to_csv('Posting1.csv', encoding='utf-8')
driver.quit()





