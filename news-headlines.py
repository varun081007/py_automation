from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = r"C:\Users\VARUN\Desktop\varun\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)

containers = driver.find_elements(by="xpath",value='//div[@class="story__copy-container"]')

titles=[]
subtitles=[]
links=[]

for container in containers:
    title = container.find_element(by="xpath",value='./a/p').text
    subtitle = container.find_element(by="xpath",value='./a/h3').text
    link = container.find_element(by="xpath",value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict={'titles':titles , 'subtitles':subtitles , 'links':links}

df_headline = pd.DataFrame(my_dict)
df_headline.to_csv('headline.csv')

driver.quit()


