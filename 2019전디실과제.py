import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4%20%ED%9D%A5%ED%96%89%EC%88%9C%EC%9C%84"
req = requests.get(url, verify = False)
res = req.text

soup = BeautifulSoup(res, 'html.parser')
Name = soup.find_all('strong', class_ ='scm_ellipsis_text _text')
Name = [line.get_text().strip() for line in Name]

keywords = soup.find_all('dl', class_ ='movie_item')
keywords = [line.get_text().strip() for line in keywords]

key = []
for i in range(0,len(keywords)):
    key += keywords[i].split()
    

df = pd.DataFrame({ '제목' : Name[0:21],
                   '개봉일' : key[1:127:6],
                   '일간' : key[3:127:6],
                   '누적' : key[5:127:6],
                  '순위' : list(range(1,22))})
 
df