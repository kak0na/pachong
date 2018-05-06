import requests
from bs4 import BeautifulSoup
import re
def gethtml(url):
    try:
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        return ""
def fenbu(html):
    soup=BeautifulSoup(html,"html.parser")
    hrefs=re.findall(r'href="/item/.*?"',html)
    for href in hrefs:
        url='https://baike.baidu.com'+re.findall(r'".*?"',href)[0][1:-1]
        if url not in info:
            try:
                r=requests.get(url,headers=headers)
                r.raise_for_status()
                r.encoding='utf-8'
                title=re.findall(r'<h1 >.*?</h1>',r.text)[0][5:-5]
                if (r.status_code)==200:
                    info.append(url)
                    print(len(info),':',title,':',info[-1])
            except:
                pass
def main():
    global info
    global headers
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
             'Referer':'https://www.baidu.com/'}
    info=["https://baike.baidu.com/item/Python/407313?fr=aladdin"]
    n=0
    print(len(info),':',info[n])
    while n<len(info):
        html = gethtml(info[n])
        fenbu(html)
        n=n+1
main()
