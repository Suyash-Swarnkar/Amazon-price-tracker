import requests
from bs4 import BeautifulSoup
import smtplib
import re  

#Change URL if required to track price of a different product
URL = 'https://www.amazon.in/Nikon-Mirrorless-Digital-Camera-24-70mm/dp/B08L5ZGKCZ/ref=sr_1_1?sr=8-1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' #Edit user agent 
}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

#Edit search elements if searching for another product

    title = soup.find(id="productTitle").get_text().strip() 
    price_str = soup.find(class_="a-price-whole").get_text().replace(',', '')
    price_digits = re.sub(r'\D', '', price_str)
    price = int(price_digits)
    #Change slicing parameters according to the product that is being tracked
    converted_price = price_str[0:6] 
    print(converted_price)
    print(title)
    if price > 100000:
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('sender@gmail.com', 'Enter app password for your email') # Enter app password for your email for ex- ugcp quex zuzx wnks
    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Sony-Mark-Body-ILCE-7RM3-Camera/dp/B076TGDHPT/ref=sr_1_4?sr=8-4'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('sender@gmail.com', 'recipient@gmail.com', msg)  # Add recipient and sender's email address
    print("Hey the message has been sent!")
    server.quit()

check_price()

