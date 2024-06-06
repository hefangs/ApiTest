import requests

url = "https://movie.douban.com/j/search_subjects"
params = {
    "type": "movie",
    "tag": "热门",
    "page_limit": 20,
    "page_start": 0
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36"
}
get = requests.get(url, params=params, headers=headers)
print(get.status_code)
print(get.json())
