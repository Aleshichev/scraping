import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.airbnb.com.ua/s/new-deli/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=New%20Delhi%2C%20Deli%2C%20%C3%8Dndia&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&price_filter_num_nights=5&federated_search_session_id=4dcef0dd-de8c-4e72-84d7-f2d518f7373b&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MiwiaXRlbXNfb2Zmc2V0IjoxOCwidmVyc2lvbiI6MX0%3D"
r = requests.get(url)

print(r.status_code)
soup = BeautifulSoup(r.text, "lxml")

page = 1
while True:
    np = soup.find("a", attrs={"aria-label": "Далі"}).get("href")

    cnp = "https://www.airbnb.com.ua" + np
    page +=1
    print(page)
    

    # url = cnp

    # r = requests.get(url)

    # soup = BeautifulSoup(r.text, "lxml")



    # soup = BeautifulSoup(r.text, "lxml")

    # box = soup.find("div", class_ = '_1YokD2 _3Mn1Gg')

    # names = box.find_all("div", class_ = "_4rR01T")

    # names_list = [i.text for i in names]

    # prices = box.find_all("div", class_="_30jeq3 _1_WHN1")

    # prices_list = [i.text for i in prices]

    # desc = box.find_all("ul", class_ = "_1xgFaf")

    # desc_list = [i.text for i in desc]

    # reviews = box.find_all("div", class_ = "_3LWZlK")

    # reviews_list = [i.text for i in reviews]

    # df = pd.DataFrame({"Product_name": names_list, "Product_prices": prices_list, "Product_desc": desc_list, "Product_reviews": reviews_list})

    # print(df)
