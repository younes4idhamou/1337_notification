import telegram_send
from ipaddress import AddressValueError
from os import link
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup,Comment
import requests
from lxml import html
import mechanize
import json
def notif():
    telegram_send.send(messages=["chouf achwa9e3"])


with requests.session() as s:
    url="https://candidature.1337.ma/users/sign_in"
    r=s.get(url,headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    soup=BeautifulSoup(r.content,"html5lib")
    login_data={'user[email]': 'yidhamou650@gmail.com','user[password]': '0636296283Facebook12@','commit': 'Se connecter'}
    login_data['authenticity_token']=soup.find('input',attrs={'name':'authenticity_token'})['value']
    login_data['utf8']=soup.find('input',attrs={'name':'utf8'})['value']
    r=s.post(url,data=login_data,headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    try:
        b=BeautifulSoup(r.text,'html.parser')
        if b.find('div',attrs={'id':'subs-content'}).find_all('h2')[0].text!='jhjhjhjh':
            notif()
    except:
        notif() 
        

