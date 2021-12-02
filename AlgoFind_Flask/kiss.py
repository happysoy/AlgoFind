import pandas as pd
import time
import json
import keywordMatching
def kiss_searchig(lists, flag):

    df = pd.DataFrame(columns = ['text'])
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.by import By
    from bs4 import BeautifulSoup
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("user-agent={Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36}")
    driver = webdriver.Chrome(r'C:\chromedriver.exe', chrome_options=chrome_options)
    
    driver.implicitly_wait(1)
    driver.get('https://kiss.kstudy.com/')
    btn_elm = driver.find_elements(By.ID, 'query')[0]
    btn_elm.send_keys(lists)
    time.sleep(2)
    btn_elm = driver.find_elements(By.ID, 'btnIndexSearch')[0]
    btn_elm.click()
    time.sleep(2)

    res = driver.page_source

    # 여기는 nth 빼줘야 함
    soup = BeautifulSoup(res,"html.parser")
    data_title =soup.select('#form_main > table > tbody > tr > td.bd-r > div > h5 > a')
    data_author =soup.select('#form_main > table > tbody > tr > td.bd-r > div > p:nth-of-type(2)')
    data_company = soup.select('#form_main > table > tbody > tr > td.bd-r > div > p:nth-of-type(3) > a:nth-of-type(1)')
    print(data_company)
    is_there=0
    for title, author, company in zip(data_title, data_author, data_company):
        df.loc[df.shape[0]] = [title.get_text()[2:] + '!!' + author.get_text()[5:] + '!!' + company.get_text()]


    for text in df.text: #first data_wrap in searching_key
        title = text.split("!!")[0]
        author = text.split("!!")[1]
        company = text.split("!!")[2]
        print(title, author, company)
        if(flag==1): #키워드 검색
            is_there = keywordMatching.comparePattern(title, lists)
            if(is_there==1):
                return ["KISS", title, author, company]
        else:
            if(title == lists):
                is_there=1
        #DBPIA

    sleep(1)
    driver.quit()
    
    if(is_there==1):
        return ["KISS", title, author, company]
    else:
        return -1