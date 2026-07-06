import requests

url = "https://www.atlus.co.jp/"

response = requests.get(url)

print(response.status_code)
print(response.text[:500])