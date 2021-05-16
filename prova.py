from bs4 import BeautifulSoup  #del módulo bs4, necesitamos BeautifulSoup
import requests
import schedule
import urllib.request
import re

def Entrades():
    p=0

    def bot_send_text(bot_message):
        
        bot_token = '1845246531:AAGwcoYIoGGa22GupG4bD1nH3TKstmiVftk'
        bot_chatID = '-577001740'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

        response = requests.get(send_text)

        return response

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

    html = requests.get("https://www.ticketmaster.es/artist/camilo-entradas/1049332",headers=headers)
    Codi=html.content
    soup = BeautifulSoup(Codi, 'html.parser')
    elements = soup.find_all('li', attrs={'class': 'uyyfoa-1 hHchPQ'})

    H=[""]*(len(elements))
    L=[""]*(len(elements))

    for i in elements:

        elements1 = i.find('span', attrs={'class': 'sc-1y6w6fq-3 fBQxZv'})
        elements2 = i.find('span', attrs={'class': 'sc-1y6w6fq-7 dgttHm'})

        if elements2 == None:
            elements2='Hi ha entrades'
        
        H[p] = str(elements1).replace("<span class=\"sc-1y6w6fq-3 fBQxZv\">","").replace("</span>","")
        L[p] = str(elements2).replace("<span class=\"sc-1y6w6fq-7 dgttHm\">","").replace("</span>","")
        p=p+1

    for i in range(len(H)):
        if H[i] == "Estadi Olimpic Lluis Companys - Barcelona":

            test_bot = bot_send_text(H[i])
            print(H[i])
            test_bot = bot_send_text(L[i])
            print(L[i])

    test_bot = bot_send_text('I-I-I-I-I-I-I-I-I-I-I-I-I-I-I-I')

if __name__ == '__main__':
        
    schedule.every(10).seconds.do(Entrades)

    while True:
        schedule.run_pending()