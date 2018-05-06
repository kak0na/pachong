# -*- coding=utf-8 -*-
import requests
import time
def main():
    url="https://lucky.nocode.com/public_lottery?page=1&size=5"
    header={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 MicroMessenger/6.6.6 NetType/WIFI Language/zh_CN',
            'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNzUyMzE0LCJuaWNrX25hbWUiOiLmqZnmnpznspIiLCJhdmF0YXIiOiJodHRwczovL3d4LnFsb2dvLmNuL21tb3Blbi92aV8zMi9EWUFJT2dxODNlcHppYWxpYnBBNmlhaWFTd29CSncyUk9URW1vS0hSZG1IeVdmMFgyTjlHbUtpYW1nUEg5aElFZ1dEd0N1dGppYVdzeUZEbG5MaWFScjJRTW1GVHcvMCIsInByb3ZpbmNlIjoiRnVqaWFuIiwiY2l0eSI6IkZ1emhvdSIsImdlbmRlciI6IjEiLCJpYXQiOjE1MjU1MDk4OTgsImV4cCI6MTUyNjExNDY5OH0.s-ayQyrQXgIDs2mIEUmE4vad8n3gG1vBEH5qgAGHX3w',
            }
    html=requests.get(url,headers=header)
    Datas=html.json().get('data')
    join_url = "https://lucky.nocode.com/lottery/{id}/join"
    for data in Datas:
        id = data.get('id')
        if id not in MC:
            newhtml=requests.post(join_url.format(id=data.get('id')),headers=header)
            newdata=newhtml.json()
            if newhtml.status_code==200 and 'errors' not in newdata:
                n=data.get("prizes").get("data")[0].get("name")
                MC[id]=n
                print(u'成功参加抽奖：《%s》%s'%(n,id))
        else:
            print(u'旧-已经参加%s'%MC[id])
if __name__=='__main__':
    MC={}
    while 1:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        main()
        time.sleep(3600)