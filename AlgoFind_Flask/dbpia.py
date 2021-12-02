import pandas as pd
import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from time import sleep

import keywordMatching
def dbpia_searchig(lists, flag):

    df = pd.DataFrame(columns = ['text'])

    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("user-agent={Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36}")
    driver = webdriver.Chrome(r'C:\chromedriver.exe', chrome_options=chrome_options)

    driver.get('https://www.dbpia.co.kr/')

    elm = driver.find_elements(By.ID, 'keyword')[0]
    elm.send_keys(lists)
    time.sleep(2)
    btn_elm = driver.find_elements(By.CLASS_NAME, 'btnSearch')[0]
    btn_elm.click()
    time.sleep(2)
    #유사한 결과 다 나오니까, 유사한 거 빼고 내가 검색한 거만 나오게 하려면, 첫번째 데이터 h5 텍스트 추출해서 하나하나씩 대조해야 할 듯
    res = driver.page_source

    soup = BeautifulSoup(res,"html.parser")


    # DBPIA
    data_types = soup.select('#dev_search_list > li > div > div.typeWrap > ul > li.data')
    data_title =soup.select('#dev_search_list > li > div > div.titWrap > h5 > a')
    data_author =soup.select('#dev_search_list > li > div > ul.info')
    data_company = soup.select('#dev_search_list > li > div > ul > li.publisher > a')
    data_date = soup.select('#dev_search_list > li > div > ul > li.date')
    is_there=0
    #author_0 > a:nth-child(1)
    for types, title, author, company, date in zip(data_types, data_title, data_author, data_company, data_date ):
        df.loc[df.shape[0]] = [types.get_text() + '!!' + title.get_text() + '!!' + author.get_text()[0:3] + '!!' + company.get_text() + '!!' + date.get_text()]
    for text in df.text: #first data_wrap in searching_key
        types = text.split("!!")[0]
        title = text.split("!!")[1]
        author = text.split("!!")[2]
        company = text.split("!!")[3]
        date = text.split("!!")[4]
        print(types, title, author, company, date)
        if(flag==1): #키워드 검색
            is_there = keywordMatching.comparePattern(title, lists)
            if(is_there==1):
                return ["dbpia", types, title, author, company, date]
        else:
            if(title == lists):
                is_there=1
   
    sleep(1)
    driver.quit()
    
    if(is_there==1):
        return ["dbpia", types, title, author, company, date]
    else:
        return -1