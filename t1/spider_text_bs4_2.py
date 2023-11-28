from bs4 import BeautifulSoup
import requests

content = requests.get("http://books.toscrape.com/").text
soup = BeautifulSoup(content, "html.parser")
all_titles = soup.findAll("h3")
for title in all_titles:
    all_links = title.findAll("a")
    for link in all_links:
        print(link.string)

