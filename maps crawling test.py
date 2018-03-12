import os
import sys
import urllib.request
from bs4 import BeautifulSoup

client_id = "W5tvrmWw8tbNlg9CdT4V"
client_secret = "e1lEzqjAn8"

encText = urllib.parse.quote("수색로 길")
url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    bs=BeautifulSoup(response_body.decode('utf-8'),'html.parser')
    print(bs.find('address'))
    print(bs.find('x'))
    print(bs.find('y'))
