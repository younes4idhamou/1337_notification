from bs4 import BeautifulSoup
import requests
from lxml import html
import sys

def notif(token,chat_id):
    text="rah la7o"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
    results = requests.get(url_req)


with requests.session() as s:
    url="https://candidature.1337.ma/users/sign_in"
    r=s.get(url,headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    soup=BeautifulSoup(r.content,"html5lib")
    login_data={'user[email]': str(sys.argv[1]),'user[password]': str(sys.argv[2]),'commit': 'Se connecter'}
    login_data['authenticity_token']=soup.find('input',attrs={'name':'authenticity_token'})['value']
    login_data['utf8']=soup.find('input',attrs={'name':'utf8'})['value']
    r=s.post(url,data=login_data,headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    try:
        b=BeautifulSoup(r.text,'html.parser')
        if b.find('div',attrs={'id':'subs-content'}).find_all('h2')[0].text!='jhjhjhjh':
            notif(str(sys.argv[3]),str(sys.argv[4]))
    except:
        notif(str(sys.argv[3]),str(sys.argv[4]))


