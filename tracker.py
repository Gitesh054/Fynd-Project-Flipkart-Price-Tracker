import requests
from bs4 import BeautifulSoup
from datetime import datetime


def track(url):
    response = requests.get(url)
    # print(response.status_code)
    flipkart_data = response.text

    soup = BeautifulSoup(flipkart_data, "html.parser")

    price_div = soup.find(name = "div", class_="_30jeq3 _16Jk6d")
    name_div = soup.find(name = "span", class_ = "B_NuCI")
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    date = now.date()
    price = price_div.getText()
    name = name_div.getText()
    items = [name, price, time, date]
    return items
