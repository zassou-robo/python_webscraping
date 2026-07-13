import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin


url = "https://www.atlus.co.jp/"

response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "lxml")
news_list = soup.find_all("li", class_="news-item")
for news in news_list:
    title = news.find("span", class_="headline").text.strip()
    print(title)
date = news.find("span", class_="date").text.strip()
game = news.find("span", class_="game-title")
category = news.find("li", class_="category")
url = urljoin("https://www.atlus.co.jp/", news.find("a")["href"])
if game:
    game = game.text.strip()
else:
    game = "なし"

if category:
    category = category.text.strip()
else:
    category = "なし"

# print("=================")
# print(title)
# print(date)
# print(game)
# print(category)
# print(url)
# print("=================")
news_data = []
for news in news_list:
    title = news.find("span", class_="headline").text.strip()
    date = news.find("span", class_="date").text.strip()

    game = news.find("span", class_="game-title")
    game = game.text.strip() if game else ""

    category = news.find("li", class_="category")
    category = category.text.strip() if category else ""

    url = news.find("a")["href"]

    news_data.append({
        "title": title,
        "date": date,
        "game": game,
        "category": category,
        "url": url
    })

print(news_data)
with open("data/news.json", "w", encoding="utf-8") as f:
    json.dump(news_data, f, ensure_ascii=False, indent=4)