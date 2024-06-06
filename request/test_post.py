import requests

# json raw
json_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
post = requests.post("https://jsonplaceholder.typicode.com/posts", json=json_data)
print(post.status_code)
print(post.json())

# form data
data = {"text": "hello"}
requests_post = requests.post("https://dict.youdao.com/keyword/key", data=data)
print(requests_post.status_code)
print(requests_post.json())
