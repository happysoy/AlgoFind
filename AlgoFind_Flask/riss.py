import pandas as pd
import time
import json
import keywordMatching
def riss_searchig(lists, flag):

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


    driver.get('http://www.riss.kr/search/Search.do?colName=all&isDetailSearch=N&searchGubun=true&oldQuery=&sflag=1&fsearchMethod=search&isFDetailSearch=N&searchQuery='+lists+'&kbid=&pageNumber=1&query='+lists)


    res = driver.page_source


    # 여기는 nth 빼줘야 함
    soup = BeautifulSoup(res,"html.parser")
    data_types = soup.select('#divContent > div > div > div.srchResultW.totalSrch > div > div.srchResultListW > ul > li > div.cont > p.etc > span:nth-of-type(4) > a')
    data_title =soup.select('#divContent > div > div > div.srchResultW.totalSrch > div > div.srchResultListW > ul > li > div.cont > p.title > a')
    data_author =soup.select('#divContent > div > div > div.srchResultW.totalSrch > div > div.srchResultListW > ul > li > div.cont > p.etc > span.writer > a')
    data_company = soup.select('#divContent > div > div > div.srchResultW.totalSrch > div> div.srchResultListW > ul > li > div.cont > p.etc > span.assigned > a')
    data_date = soup.select('#divContent > div > div > div.srchResultW.totalSrch > div > div.srchResultListW > ul > li > div.cont > p.etc > span:nth-of-type(3)')

    is_there=0
    for types, title, author, company, date in zip(data_types, data_title, data_author, data_company, data_date):

        df.loc[df.shape[0]] = [types.get_text() + '!!' + title.get_text() + '!!' + author.get_text() + '!!' + company.get_text() + '!!' + date.get_text()]

    for text in df.text:
        types = text.split("!!")[0]
        title = text.split("!!")[1]
        author = text.split("!!")[2]
        company = text.split("!!")[3]
        date = text.split("!!")[4]
        print("얏호", types, title, author, company, date)
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
        return ["RISS", types, title, author, company, date]
    else:
        return -1