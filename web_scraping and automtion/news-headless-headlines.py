from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.npr.org/sections/news/"
path = r"C:\Users\VARUN\Desktop\varun\chromedriver-win64\chromedriver.exe"

options = Options()
options.add_argument("--headless=new")

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="item-info"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='.//h2[@class="title"]/a').text
    subtitle = container.find_element(by="xpath", value='.//p[@class="teaser"]').text
    link = container.find_element(by="xpath", value='.//h2[@class="title"]/a').get_attribute("href")
    
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'titles': titles, 'subtitles': subtitles, 'links': links}

df_news = pd.DataFrame(my_dict)
df_news.to_csv('npr-news-headless.csv')

driver.quit()