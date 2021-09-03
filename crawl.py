from selenium import webdriver
from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.alert import Alert
import requests
import numpy as np
import pandas as pd
from datetime import datetime
from tabulate import tabulate





options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")
# options.add_argument('--disable-gpu')
driver = webdriver.Chrome("/usr/bin/chromedriver",options=options)
# driver = webdriver.Chrome("/Users/goyoonjae/Desktop/dongmonitor/chromedriver")

def gamelog(nickname):

    driver = webdriver.Chrome("/usr/bin/chromedriver",options=options)
    url = 'https://www.op.gg/summoner/userName='
    # inp = input('롤 닉넴 입력 : ')
    url = url+nickname

    driver.get(url)
    print('사이트 접속')
    alert = Alert(driver)
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    pd.set_option('expand_frame_repr',False)
    
    driver.find_element_by_css_selector('#SummonerRefreshButton').click()
    print('.click()')
    try:
        # time.sleep(3)
        alert = Alert(driver)
        # alert = driver.switch_to.alert
        
        print(alert)
        time.sleep(1)
        print('alert detected!')
        alert.accept()
        time.sleep(1)
        alert.accept()
    except:
        "noal"
        # time.sleep(3)
        # print('no alert!')
    # kda = soup.select('.KDA .KDA span')

    kda = soup.select('.GameItem>.Content>.KDA>.KDA>span')
    kdas = []
    for tag in kda:
        kdas.append(tag.get_text().strip())
    KDA = np.reshape(kdas,(20,3))
    print('kda 조회중...')
    # print(KDA)


    gameresult = soup.select('.GameStats>.GameResult')
    gameresults = []
    for tag in gameresult:
        gameresults.append(tag.get_text().strip())
    GRES = np.reshape(gameresults,(20,1))
    print('게임결과 조회중...')
    # print(GRES)


    champion = soup.select('.Content>.GameSettingInfo>.ChampionName>a')
    champions = []
    for tag in champion:
        champions.append(tag.get_text())
    CHAMP = np.reshape(champions,(20,1))
    print('챔피언 조회중...')

    # for tag in champion:
    #     print(tag.get_text())

    data = pd.DataFrame(CHAMP)
    subdf = pd.DataFrame(GRES)
    data = pd.concat([data, subdf],axis = 1)
    subdf = pd.DataFrame(KDA)
    data = pd.concat([data,subdf],axis = 1)
    data.columns = ['CHAMP','RESULT','KILL','DEATH','ASSIST']
    data = tabulate(data,headers='keys',tablefmt='pretty',showindex=range(1,21))
    
    # print(data)
    # for tag in kda:
    #     print(tag.get_text())
    driver.delete_all_cookies()
    driver.quit()
    print('정보반환완료')
    print(data)
    print(type(data))
    return data
    

def nowtier(nickname):
    driver = webdriver.Chrome("/usr/bin/chromedriver",options=options)
    url = 'https://www.op.gg/summoner/userName='
    # inp = input('롤 닉넴 입력 : ')
    url = url+nickname
    driver.get(url)
    alert = Alert(driver)
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')

    driver.find_element_by_css_selector('#SummonerRefreshButton').click()

    try:
        # time.sleep(3)
        alert = Alert(driver)
        # alert = driver.switch_to.alert
        
        print(alert)
        # time.sleep(1)
        print('alert detected!')
        alert.accept()
        # time.sleep(1)
        alert.accept()
    except:
        "noal"
        # time.sleep(3)
        # print('no alert!')

    
    soltier = soup.find(class_= 'TierRank').get_text()
    subtier = soup.find(class_="sub-tier__rank-tier").get_text().strip()
    driver.delete_all_cookies()
    driver.quit()
    return soltier, subtier




    # kda = soup.select('.KDA .KDA span')

# inp = input('닉네임입력')
# crawler(inp)