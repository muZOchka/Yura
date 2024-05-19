import requests

response = requests.post("https://httpbin.org/post",
                         data="test data",
                         headers={"h1": "Vasya title"})

print(response.text)