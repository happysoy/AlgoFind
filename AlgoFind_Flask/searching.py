from typing import Sized
import pandas as pd
import time
import json

import dbpia
import wiley
import kiss
import google_scholar
import ebsco
import kci
import riss
import science
import assembly
import proquest
import jstor
def backtracking(lists, checked):

    if(checked == "all_citation"): #모든
        file_path="./json/all_citation.json" #인기순
    elif(checked == "all_alphabet_order"):
        file_path="./json/all_alphabet.json" #가나다순
    elif (checked =="all_ex"):
        file_path="./json/all_ex.json" #키워드

    elif (checked =="domestic_citation"): #국내
        file_path="./json/domestic_citation.json" #인기순
    elif (checked =="domestic_alphabet_order"):
        file_path="./json/domestic_alphabet.json" #가나다순
    elif (checked =="domestic_ex"):
        file_path="./json/domestic_ex.json" #키워드

    elif (checked =="abroad_citation"): #국외
        file_path="./json/abroad_citation.json" #인기순
    elif (checked =="abroad_alphabet_order"):
        file_path="./json/abroad_alphabet.json" #가나다순
    elif (checked =="abroad_ex"):
        file_path="./json/abroad_ex.json" #키워드
    
    with open(file_path, "r") as json_file:
        json_data = json.load(json_file)
        #print(json_data[0][0])
        #print(json_data[1][0])
  
    for idx in json_data:
        print("논문 site >> ", idx[0], idx[1])
        flag=0
        if(idx[0]=="DBPIA"):
            if(idx[1]=="key"):
                flag= 1
            dbpia_result = dbpia.dbpia_searchig(lists, flag)
            if(dbpia_result!= -1 ):
                return dbpia_result
        elif(idx[0]=="wiley"):
            if(idx[1]=="key"):
                flag= 1
            proquest_result= wiley.wiley_searchig(lists, flag)
            if(proquest_result!= -1):
                return proquest_result
        elif(idx[0]=="KISS"):
            if(idx[1]=="key"):
                flag= 1
            kiss_result= kiss.kiss_searchig(lists, flag)
            if(kiss_result!= -1):
                return kiss_result
        elif(idx[0]=="google_scholar"):
            if(idx[1]=="key"):
                flag= 1
            google_result = google_scholar.google_scholar_searchig(lists, flag)
            if(google_result!= -1):
                return google_result
        elif(idx[0]=="EBSCOhost_ASC"):
            if(idx[1]=="key"):
                flag= 1
            ebsco_result = ebsco.ebsco_searchig(lists, flag)
            if(ebsco_result!= -1):
                return ebsco_result
        elif(idx[0]=="KCI"):
            if(idx[1]=="key"):
                flag= 1
            kci_result = kci.kci_searchig(lists, flag)
            if(kci_result!= -1):
                return kci_result
        elif(idx[0]=="RISS"):
            if(idx[1]=="key"):
                flag=1
            riss_result = riss.riss_searchig(lists, flag)
            if(riss_result!= -1):
                return riss_result
        elif(idx[0]=="science_direct"): 
            if(idx[1]=="key"):
                flag= 1
            science_result = science.science_searchig(lists, flag)
            if(science_result!= -1):
                return science_result
        elif(idx[0]=="ASSEMBLY"): #국회도서관
            if(idx[1]=="key"):
                flag= 1
            assembly_result = assembly.assembly_searchig(lists, flag)
            if(assembly_result!= -1):
                return assembly_result
        elif(idx[0]=="ProQuest_Central"): 
            if(idx[1]=="key"):
                flag= 1
            proquest_result = proquest.proquest_searchig(lists, flag)
            if(proquest_result!= -1):
                return proquest_result
        elif (idx[0]=="JSTOR_Archive"):
            if(idx[1]=="key"):
                flag= 1
            jstor_result = jstor.jstor_searchig(lists, flag)
            if(jstor_result!= -1):
                return jstor_result
        result=-1
    if(result==-1):
        return -1

   
        
    