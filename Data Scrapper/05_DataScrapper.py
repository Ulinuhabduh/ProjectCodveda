import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
response = requests.get(url)
print(response.status_code)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})

data = []

for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    if len(cols) >= 3:
        location = cols[0].get_text(strip=True)
        population = cols[1].get_text(strip=True)
        percent = cols[2].get_text(strip=True)
        date = cols[3].get_text(strip=True)
        data.append([location, population, percent, date])

df = pd.DataFrame(data, columns=['Location', 'Population', '% of world', 'Date'])

# convert population to integer
df['Population'] = df['Population'].str.replace(',', '').astype('int64')

# convert date to datetime
df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True, errors='coerce')

# save to csv
df.to_csv('Data Scrapper/world_population.csv', index=False)
