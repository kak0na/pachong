#!usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request
import re #使用正则表达式
def getResponse(url):
    url_request=request.Request(url)
    print('这个对象的方法是：',url_request.get_method())
    url_response=request.urlopen(url) #打开一个url或者一个Request对象
    return url_response #返回这个对象
def getjpg(data):
    jpglist=re.findall(r'src="http.+?.jpg"',data)
    return jpglist
def download(jpgurl,n):
    try:
        request.urlretrieve(jpgurl,'%s.jpg'%n)
    except Exception as e:
        print(e)
    finally:
        print('图片%s下载操作完成'%n)
m=0
global n
n=1
while m<=1830:
    URL='https://movie.douban.com/celebrity/1018562/photos/?type=C&start='+str(m)+'&sortby=like&size=a&subtype=a'
    http_response = getResponse(URL)#拿到http请求后的上下文对象（HTTPResponse object）
    data=(http_response.read().decode('utf-8')) #打印这个对象
    L=getjpg(data)
    j=1
    for jpginfo in L:

        print(n,'--->',jpginfo)
        s=re.findall(r'http.+?.jpg',jpginfo)
        download(s[0],n)
        j=j+1
        if j==30:
            break
        n=n+1
    m=m+30
