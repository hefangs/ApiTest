import requests

get = requests.get("https://api.github.com/events")
print(get.status_code)
# print(get.json())

params = {"username": "fisher", "password": "123456"}
get2 = requests.get("https://api.github.com/events", params=params)
print(get2.status_code)
# print(get2.json())
