from bs4 import BeautifulSoup
import requests
from datetime import datetime
import csv

def get_data(date):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    url = f"https://www.weldsheriff.com/apps1/dailyArrests/index.cfm?date_booked={date}"

    req = requests.get(url, headers=headers)

    content = req.content
    soup = BeautifulSoup(content)

    for row in soup.find("table"):
        print(row)
    


initial_date = "02/14/06"
get_data(initial_date)