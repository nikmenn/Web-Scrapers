from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.nhl.com/').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('nhl_news_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Subheader', 'Link'])

for article in soup.find_all('li', class_= 'mixed-feed__item mixed-feed__item--article'):
    headline = article.find('div', class_ ='mixed-feed__item-header-text').h4.text
    print(headline)

    subheader = article.find('div', class_ ='mixed-feed__item-header-text').h5.text
    print(subheader)

    link = 'https://www.nhl.com/' + article.find('div', class_ ='mixed-feed__item-header-text').a['href']
    print(link)

    print()
    csv_writer.writerow([headline, subheader, link])

csv_file.close()
