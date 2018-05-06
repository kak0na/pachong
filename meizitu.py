import re
import requests
from bs4 import BeautifulSoup
import os
'''
def gethtmltext(url):
    try:
        r=requests.get(url,timeout=10)
        r.raise_for_status()
        print(r.status_code)
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
def baocun(url,n):

    path = "D://meizitu//"
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,headers=kv)
        print(r.status_code)
        with open(path+str(n)+".jpg",'wb') as f:
            f.write(r.content)
    except:
        return ""
def main():
    url="http://www.meizitu.com/"
    html=gethtmltext(url)
    soup=BeautifulSoup(html,'html.parser')
    lst=soup.find_all('div',attrs={'id':"picture"})
    for i in range(len(lst)):
        lstimg=lst[i].find_all('img')[0]
        img=lstimg.attrs['href']
        text=re.findall(r'http.*?.jpg',img)[0]
        baocun(text,i)
        print("保存成功")
main()
print(1)
'''

def gethtmltext(url):
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,timeout=10,headers=kv)
        print(r.status_code)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        return ""
def baocun(url,n):
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,timeout=10,headers=kv)
        r.raise_for_status()
        with open("d://meizitu//"+str(n)+".jpg",'wb') as f:
            f.write(r.content)
            f.close()
    except:
        return ""


def dakai(url,n):
    html=gethtmltext(url)
    soup=BeautifulSoup(html,'html.parser')
    div = soup.find_all('div', attrs={'id':'picture'})
    img=str(div)
    src=re.findall(r'http.*?.jpg',img)
    for i in range(len(src)):
        n=n+1
        baocun(src[i],n)
    return n
def img(lst,text):
    soup=BeautifulSoup(text,'html.parser')
    div=soup.find_all('div',attrs={'class':'pic'})
    n=0
    for i in range(len(div)):
        a=div[i].find_all('a')[0]
        href=a.attrs['href']
        print(href)
        n=dakai(href,n)
    print(1)
def main():
    url="http://www.meizitu.com/a/more_1.html"
    lst=[]
    html=gethtmltext(url)
    img(lst,html)

main()