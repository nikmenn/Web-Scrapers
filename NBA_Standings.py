from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://www.espn.com/nba/standings/_/group/league').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('nba_standings.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Place','Team', 'Team Link'])

place = 0

for team in soup.find_all('div', class_='team-link'):
    place += 1
    
    team_name = team.a.img['title']
    
    print(place, team_name)
    
    team_link = 'http://www.espn.com' + team.a['href']

    csv_writer.writerow([place, team_name, team_link])

csv_file.close()



