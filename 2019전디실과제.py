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
check = []
Result1 = []
Result2 = []
for i in range(0,len(keywords)):
    if keywords[i][0] in '��':
        key += keywords[i].split()
    else:
        check.append(i)

j =0
for i in check:
    del(Name[i+j])
    j-=1
    
for i in range(0,len(Name)):
    Result1.append(int(key[(6*i)+3].replace(',', '').strip('��')))
for i in range(0,len(Name)):
    Result2.append(int(key[(6*i)+5].replace(',', '').strip('��')))

df = pd.DataFrame({ '����' : Name,
                   '������' : key[1::6],
                   '�ϰ�' : Result1,
                   '����' : Result2,
                  '��ŷ' : list(range(1,len(Name)+1))})


print(df.groupby('������')['�ϰ�'].nunique())

fig = plt.figure()
axes1 = fig.add_subplot(1,2,1)
axes2 = fig.add_subplot(1,2,2)
axes1.hist(df['�ϰ�'],bins = 20)
axes2.scatter(df['����'],df['�ϰ�'])

axes1.set_title("Day Spectators")
axes1.set_xlabel("Spectators")
axes1.set_ylabel('Frequency')
axes2.set_title("Day Spectators / Accumulated Spectators")
axes2.set_xlabel("Day Spectators")
axes2.set_ylabel('Accumulated Spectators')

fig.tight_layout()

