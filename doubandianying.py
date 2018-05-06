import os
import re
import requests
from bs4 import BeautifulSoup

def gethtmltext(url):
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,timeout=1,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return""

def saveinfo(n,title,score,jpgurl):
    n=str(n)
    n=n.zfill(3)+'-'+title+'-'+score+'.jpg'
    path=r"豆瓣TOP250"
    if not os.path.exists(path) :
        os.mkdir(path)
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(jpgurl,timeout=1,headers=kv)
        r.raise_for_status()
        with open(path+r'\\'+n,'wb') as f:
            f.write(r.content)
            f.close()
    except:
        return''

def htmlinfo(html,lst):
    soup=BeautifulSoup(html,'html.parser')
    divs=soup.find_all('div',attrs={'class':'item'})
    for i in range(len(divs)):
        n=divs[i].find_all('em')[0].string
        img=divs[i].find_all('img')[0]
        jpgurl=img['src']
        title=img['alt']
        score=divs[i].find_all('span',attrs={'class':'rating_num'})[0].string
        saveinfo(n,title,score,jpgurl)
def main():
    n=0
    while n<250:
        url="https://movie.douban.com/top250?start="+str(n)+"&filter="
        lst={}
        html=gethtmltext(url)
        htmlinfo(html,lst)
        n=n+25
main()