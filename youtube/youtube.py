from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.youtube.com/@jacksfilms/videos")

for _ in range(72):
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # driver.find_element_by_tag_name('body').send_keys(Keys.END)
    body_element = driver.find_element("tag name", "body")
    body_element.send_keys(Keys.END)
    time.sleep(3)
    
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

title = soup.title
print(title)