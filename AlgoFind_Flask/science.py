import pandas as pd
import time
import json
import keywordMatching
def science_searchig(lists, flag):

    df = pd.DataFrame(columns = ['text'])
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.by import By
    #from selenium.webdriver.common.keys import Keys
    from bs4 import BeautifulSoup
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("user-agent={Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36}")
    driver = webdriver.Chrome(r'C:\chromedriver.exe', chrome_options=chrome_options)

    driver.get('https://www.sciencedirect.com/search?qs='+lists)
    #btn_elm = driver.find_elements(By.ID, 'query')[0]
    #btn_elm.send_keys('meta')


    #time.sleep(2)
    #btn_elm = driver.find_elements(By.CLASS_NAME, 'btnSearch')[0]
    #btn_elm.click()
    #time.sleep(2)


    res = driver.page_source

    # 여기는 nth 빼줘야 함
    soup = BeautifulSoup(res,"html.parser")
    data_types = soup.select('#publication-list > li > div > p.u-display-inline.js-publication-content-type')
    data_title =soup.select('#publication-list > li > a > span')
    #data_author =soup.select('//*[@id="thesisInfoDiv"]/div[2]/div[1]/ul/li[1]/div/p/a')
    #data_company = soup.select('//*[@id="thesisInfoDiv"]/div[2]/div[1]/ul/li[2]/div/p/a')
    data_date = soup.select('#publication-list > li > div > p.u-display-inline.js-publication-year.u-clr-grey8')

    is_there=0
    for types, title, author, company in zip(data_types, data_title, data_author, data_company):
        df.loc[df.shape[0]] = [title.get_text()[2:] + '!!' + author.get_text()[5:] + '!!' + company.get_text()]


    for text in df.text: #first data_wrap in searching_key
        types = text.split("!!")[0]
        title = text.split("!!")[1]
        author = text.split("!!")[2]
        company = text.split("!!")[3]
        print(types, title, author, company)
        if(flag==1): #키워드 검색
            is_there = keywordMatching.comparePattern(title, lists)
            if(is_there==1):
                return ["dbpia", types, title, author, company, date]
        else:
            if(title == lists):
                is_there=1
        #DBPIA

    sleep(1)
    driver.quit()
    
    if(is_there==1):
        return ["Science Direct", types, title, author, company]
    else:
        return -1