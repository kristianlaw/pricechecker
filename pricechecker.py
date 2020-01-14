import requests
from bs4 import BeautifulSoup
import smtplib
import time
# Product link
URL = 'https://www.amazon.de/Casio-F-91W-1YER-Collection-Unisex-Armbanduhr-F91W1YER/dp/B000J34HN4?pf_rd_p=84abf925-37ce-4385-adc5-6abfdadb17cd&pd_rd_wg=E2EZB&pf_rd_r=EMRFD26QNME15AGNBBFB&ref_=pd_gw_unk&pd_rd_w=mUh7Y&pd_rd_r=bac11420-21e2-4751-8fcf-74a289cf6b0a'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    #Use F12 in your browser and check the ID of price and product text
    title = soup2.find(id="title").get_text()
    price = soup2.find(id ="priceblock_ourprice").get_text()

    #Floats the price so it can be compareed in the IF-statement
    converted_price = float(price[15:17])

    print(converted_price)
    print(title.strip())

    if(converted_price < 5):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
# Here you put your gmail credentials
    server.login('example@gmail.com', 'password')

    subject = 'Price went down!'
    body = 'Link: https://www.amazon.de/Casio-F-91W-1YER-Collection-Unisex-Armbanduhr-F91W1YER/dp/B000J34HN4?pf_rd_p=84abf925-37ce-4385-adc5-6abfdadb17cd&pd_rd_wg=E2EZB&pf_rd_r=EMRFD26QNME15AGNBBFB&ref_=pd_gw_unk&pd_rd_w=mUh7Y&pd_rd_r=bac11420-21e2-4751-8fcf-74a289cf6b0a'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'example@gmail.com', #From
        'example@outlook.com', #To where
            msg
    )
    print('Email sent')
    server.quit()



check_price()
