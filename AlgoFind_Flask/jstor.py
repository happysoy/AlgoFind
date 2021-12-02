import pandas as pd
import time
import json
import keywordMatching
def jstor_searchig(lists,flag):

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


    driver.get('http://www.jstor.org')
    btn_elm = driver.find_elements(By.ID, 'query-builder-input')[0]
    btn_elm.send_keys(lists)

    time.sleep(2)
    btn_elm = driver.find_elements(By.CLASS_NAME, 'icon')[0]
    btn_elm.click()
    time.sleep(2)


    res = driver.page_source

    # 여기는 nth 빼줘야 함
    soup = BeautifulSoup(res,"html.parser")
    data_types = soup.select('#search-results-vue > div > div > div.search-results-layout > ol > li > div > div > div > div > ol >  div > div.result__metadata > div.badge.result__badge')
    data_title =soup.select('#search-results-vue > div > div > div.search-results-layout > ol > li > div > div > div > div > ol > div > div.result__metadata > div.title > pharos-heading > a')
    data_author =soup.select('#search-results-vue > div > div > div.search-results-layout > ol > li > div > div > div > div > ol > div > div.result__metadata > div.contrib.metadata-row > a')
    data_company = soup.select('#search-results-vue > div > div > div.search-results-layout > ol > li > div > div > div > div > ol > div > div.result__metadata > div.break-word.metadata-row > span')
    data_date = soup.select('#search-results-vue > div > div > div.search-results-layout > ol > li > div > div > div > div > ol > div > div.result__metadata > div.break-word.metadata-row > span')

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
                return ["KCI", types, title, author, company, date]
        else:
            if(title == lists):
                is_there=1

    sleep(1)
    driver.quit()
    
    if(is_there==1):
        return ["KCI", types, title, author, company, date]
    else:
        return -1