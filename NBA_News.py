from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://www.nba.com/news').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('nba_news_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Link'])

article = soup.find('a' )
print(article)
   