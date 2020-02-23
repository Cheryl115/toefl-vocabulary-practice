
import urllib.request
import http.cookiejar as cookielib
import requests, json
from lxml import html
from bs4 import BeautifulSoup
import csv
import importlib,sys
import time
from selenium import webdriver
importlib.reload(sys)

for j in range(1,11):
    num=str(j)
    quote_page = 'https://www.examword.com/toefl-list/5000-vocabulary-'+num+'?la=en'
    page = urllib.request.urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    voc = soup.find_all('div', attrs={'class': 'glface'})
    for i in voc:
        vocabulary = i.text
        print(vocabulary)
        try:
            quote_page = 'https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E-%E6%BC%A2%E8%AA%9E-%E7%B9%81%E9%AB%94/' + vocabulary
            time.sleep(1)
            page = urllib.request.urlopen(quote_page)
            soup = BeautifulSoup(page, 'html.parser')
            p = soup.find('span', attrs={'class': 'pos dpos'})
            pos = p.text
            voc = soup.find('span', attrs={'class': 'trans dtrans dtrans-se'})
            meaning = voc.text

        except Exception:
            pos='None'
            meaning='None'

        print(pos)
        print(meaning)
        with open('voc.csv','a',encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([vocabulary,pos,meaning])
