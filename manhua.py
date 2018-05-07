import re
import requests
import os
def gethtml(url):
    try:
        headers={
            'Referer':'http://www.manhuadb.com/manhua/1001',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Host':'www.manhuadb.com',
        }
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding='utf-8'
        return r
    except:
        return ''




def download(jpgurl,path):
    html=gethtml(jpgurl)
    if not os.path.exists(path[0]):
        os.mkdir(path[0])
    path='%s/%s'%(path[0],path[1])
    with open(path+'.jpg','wb') as f:
        f.write(html.content)


def main():
    url='http://www.manhuadb.com/manhua/1001'
    html=gethtml(url).text
    urlslist=re.findall('<a target="_blank" class="btn btn-outline-info btn-block px-1" href="(.*?)" role="button">',html)
    for url1 in urlslist:
        url='http://www.manhuadb.com'+url1
        html=gethtml(url).text
        name1=re.findall('<h2 class="h4 text-center">(.*?)</h2>',html)[0]
        pagelist=re.findall('<option value="(.*?)".*?>(.*?)</option>',html)
        pages=int(re.findall('共 (\d*) 页',html)[0])
        for page in pagelist[:pages]:
            pageurl='http://www.manhuadb.com'+page[0]
            path=[name1,page[1]]
            print(pageurl,page[1])
            html=gethtml(pageurl).text
            jpgurl='http://www.manhuadb.com'+re.findall(r'<img class="img-fluid" src="(.*?)" /',html)[0]
            download(jpgurl,path)

main()