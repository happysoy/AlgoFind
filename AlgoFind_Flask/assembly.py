import pandas as pd
import time
import json
import keywordMatching
def assembly_searchig(lists, flag):

    df = pd.DataFrame(columns = ['text'])
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    from bs4 import BeautifulSoup
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("user-agent={Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36}")
    driver = webdriver.Chrome(r'C:\chromedriver.exe', chrome_options=chrome_options)


    driver.get('https://dl.nanet.go.kr/search/searchInnerList.do?queryText='+lists+'%3AALL_NI_TOC%3AAND&selectSearchType=E&query='+lists)

    res = driver.page_source

    # 여기는 nth 빼줘야 함
    soup = BeautifulSoup(res,"html.parser")
    data_types = soup.select('#wrapper > div.searchList > ul > li:nth-of-type(1) > ul > li:nth-of-type(1)')

    data_title = soup.select('#wrapper > div.searchList > ul > li:nth-of-type(1) > a')
    # 여기는 author가 title 안에 있어서 author 빼야할 듯
    # data_author = soup.select('#wrapper > div.searchList > ul > li:nth-of-type(1) > a') 
    data_company = soup.select('#wrapper > div.searchList > ul > li:nth-of-type(1) > ul > li:nth-of-type(3)')
    data_date = soup.select('#wrapper > div.searchList > ul > li:nth-of-type(1) > ul > li:nth-of-type(4)')


    is_there=0
    for types, title, company, date in zip(data_types, data_title,data_company, data_date):

        df.loc[df.shape[0]] = [types.get_text() + '!!' + title.get_text() + '!!' + company.get_text() + '!!' + date.get_text()]

    for text in df.text:
        types = text.split("!!")[0]
        temp = text.split("!!")[1]
        title = temp.split(" /")[0]
        author = temp.split("/")[1]
        author_detail = author.split(" ")[1]
        company = text.split("!!")[2]
        date = text.split("!!")[3]
        print("얏호", types, title, author_detail, company, date)
        print(len(lists), len(title))
        if(flag==1): #키워드 검색
            is_there = keywordMatching.comparePattern(title, lists)
            if(is_there==1):
                return ["RISS", types, title, author, company, date]
        else:
            if(title == lists):
                is_there=1

    sleep(1)
    driver.quit()
    
    if(is_there==1):
        return ["국회 도서관", types, title, author_detail, company, date]
    else:
        return -1