from array import array
import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

titles_bs = soup.find_all(
    "a", "gem-c-document-list__item-title")

descriptions_bs = soup.find_all("p", "gem-c-document-list__item-description")

titles = []

for title in titles_bs:
    titles.append(title.string)

descriptions = []

for description in descriptions_bs:
    descriptions.append(description.string)

print(titles)
print(descriptions)
