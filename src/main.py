from bs4 import BeautifulSoup
import requests
from datetime import datetime
import csv

def get_data(date):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    url = f"https://www.weldsheriff.com/apps1/dailyArrests/index.cfm?date_booked={date}"

    req = requests.get(url, headers=headers)

    content = req.content
    soup = BeautifulSoup(content, 'html.parser')

    data = []
    for row in soup.find_all("tr"):
        import code; code.interact(local=dict(globals(), **locals()))
        
        # name = row.find("span", attrs={"class": "boldtextSmall"}).text

        row_data = row.find("div", attrs={"class": "tdspace"}).text.split("\r\n")

        row_data = [x.strip() for x in row_data]
        data = [x for x in row_data if len(x.strip()) > 0]

        
    


initial_date = "02/14/06"
get_data(initial_date)