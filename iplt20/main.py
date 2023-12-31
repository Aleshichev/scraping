import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.iplt20.com/auction"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_ = "ih-td-tab auction-tbl")

header = table.find_all("th")

titles = [i.text for i in header]

df = pd.DataFrame(columns=titles)


rows = table.find_all("tr")

for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text.replace('\n', '') for tr in data]
    l = len(df)
    df.loc[l] = row

df.to_csv("IPl_auction.csv")