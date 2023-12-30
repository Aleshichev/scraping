# Refactored code from main.py - pandas

from bs4 import BeautifulSoup
import requests
import pandas as pd


def extract_data(soup, tag, class_name, attribute=None):
    elements = soup.find_all(tag, class_=class_name)
    if attribute:
        return [element.get(attribute) for element in elements]
    else:
        return [element.text for element in elements]


def scrape_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    product_names = extract_data(soup, "a", "title", attribute="title")
    prices = extract_data(soup, "h4", "float-end price card-title pull-right")
    descriptions = extract_data(soup, "p", "description")
    review_counts = extract_data(soup, "p", "float-end review-count")

    return pd.DataFrame(
        {
            "Product Name": product_names,
            "Prices": prices,
            "Description": descriptions,
            "number of reviews": review_counts,
        }
    )


url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
data_frame = scrape_data(url)
data_frame.to_csv("products_details_ref.csv", index=False)
