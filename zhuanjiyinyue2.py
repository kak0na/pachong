from urllib import request
import requests
from bs4 import BeautifulSoup
import json
import re
import os

def get_html(url):
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Referer':'http://music.163.com/',
        'Host':'music.163.com',
    }
    try:
        url_response=requests.get(url,headers=header,timeout=5)
        url_response.encoding=url_response.apparent_encoding
        html=url_response.text
        return html
    except:
        return""
def get_singer(songid):
    url='http://music.163.com/song?id='+songid
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Referer':'http://music.163.com/',
        'Host':'music.163.com',
    }
    try:
        url_response=requests.get(url,headers=header)
        url_response.encoding=url_response.apparent_encoding
        html=url_response.text
        singer=re.findall(r'content="歌手：.*?。',str(html))[0].split('：')[1][:-1]
        print(singer)
        return singer
    except:
        return""
def get_singer_info(html):
    global n
    soup=BeautifulSoup(html)
    infos = soup.find('ul', class_='f-hide').find_all('a')
    print(3)
    print(infos)
    for i in range(len(infos)):
        n=n+1
        song_name=infos[i].string
        songid=infos[i]['href'].split('=')[1]
        singer=get_singer(songid)
        lyric = get_lyric(songid)
        write_lyric(song_name, lyric, singer)
        download_song(song_name, songid, singer)
    return ""
def get_lyric(song_id):
    url=r'http://music.163.com/api/song/lyric?'+'id='+str(song_id)+'&lv=1&kv=1&tv=-1'
    url="http://music.163.com/api/song/lyric?id=468490574&lv=1&kv=1&tv=-1"
    html=get_html(url)
    json_obj=json.loads(html)
    try:
        inital_lyric=json_obj['lrc']['lyric']
        regax=re.compile(r'\[.*\]')
        final_lyric=re.sub(regax,'',inital_lyric).strip()
        return final_lyric
    except:
        return ""
def write_lyric(song_name,lyric,singer):
    try:
        print('正在写入歌词:{}'.format(singer+'-'+song_name))
        if not os.path.exists(r'歌词'):
            os.mkdir('歌词')
        with open(r'歌词\{}.txt'.format(singer+'-'+song_name),'a',encoding='utf-8') as f:
            f.write(lyric)
    except:
        pass
def download_song(song_name,song_id,singer):
    global n
    singer_url="http://music.163.com/song/media/outer/url?id={}.mp3".format(song_id)
    try:
        print('正在下载歌曲{}'.format(singer+'-'+song_name))
        if not os.path.exists(r'song'):
            os.mkdir('song')
        m=str('%05d' % n)
        request.urlretrieve(singer_url,r'song\{}.mp3'.format(m+'-'+singer+'-'+song_name))
    except:
        pass

if __name__=='__main__':
    n=0
    start_url="http://music.163.com/playlist?id=14395225"
    print(start_url)
    html=get_html(start_url)
    print(1)
    singer_infos=get_singer_info(html)
    print(2)