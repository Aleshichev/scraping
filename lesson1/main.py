from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

# tag = soup.header.div.a.button.span

# price = (soup.find("h4", {"class": "float-end price card-title pull-right"}))
# print(price.string)

# desc = (soup.find("p", {"class": "description"}))
# desc = (soup.find("p", class_ = "description"))
# print(desc.string)

# --------------price_all------------------------
# price_all = (soup.find_all("h4", {"class": "float-end price card-title pull-right"}))
# print(len(price_all))
# print(price_all[3])

# desc = soup.find_all("p", class_ = "description")
# print(desc[3])
# for i in price_all:
#     print(i.text)

# -------------------------re-----------------------------------

# data = soup.find_all(string = re.compile("Galaxy"))
# print(data)

# ------------------pandas----------------------------------------

names = soup.find_all("a", class_="title")
# print(names)
product_name = []

for i in names:
    name = i.get("title")
    product_name.append(name)

# print(product_name)

prices = soup.find_all("h4", class_="float-end price card-title pull-right")

prices_list = []
for i in prices:
    price = i.text
    prices_list.append(price)

# print(prices_list)

desc = soup.find_all("p", class_="description")
desc_list = []
for i in desc:
    des = i.text
    desc_list.append(des)

# print(desc_list)

reviews = soup.find_all("p", class_="float-end review-count")
reviews_list = []
for i in reviews:
    rew = i.text
    reviews_list.append(rew)

# print(reviews_list)

df = pd.DataFrame(
    {
        "Product Name": product_name,
        "Prices": prices_list,
        "Description": desc_list,
        "number of reviews": reviews_list,
    }
)
df.to_csv("products_details.csv")
# df.to_excel("products_excel_details.xlsx")

# print(df)
