import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


response = requests.get('https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bangalore')
print(response)
# print(response.content)

soup = BeautifulSoup(response.content,'html.parser')
# print(soup.prettify())

cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})
# print(card)
records = []
for card in cards:
    price = card.find("div",attrs={"class":"m-srp-card__price"}).text
    # print(price)
    title = card.find("span", attrs={"class":"m-srp-card__title__bhk"}).text.strip('\n')
    # print(title)
    carpet_area = card.find("div",attrs={"class":"m-srp-card__summary__info"}).text.strip("sqft")
    # print(carpet_area)
    records.append((title,carpet_area,price))
# print(records)
df = pd.DataFrame(records,columns=['title','carpet_area','price'],index=None)
df.to_csv('scrap.csv',encoding='utf-8')

scrap_data = pd.read_csv('scrap.csv')
# print(scrap_data.info())
scrap_data.drop('Unnamed: 0',axis=1,inplace=True)
print(scrap_data.head(5))
print(scrap_data.title.value_counts())
# scrap_data['title'] = scrap_data['title'].replace('BHK Flat','')
print(scrap_data.head())