import requests
from bs4 import BeautifulSoup

url = "https://www.atlus.co.jp/"

response = requests.get(url)
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text, "lxml")
# with open("atlus.html", "w", encoding="UTF-8") as f:
#     f.write(soup.prettify())
news_list = soup.find_all("li", class_="news-item")
print(len(news_list))
print("HTML saved to atlus.html")
# for news in news_list:
#     print(news.get_text())