from bs4 import BeautifulSoup
import requests

response = requests.get("https://coinmarketcap.com/")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("a", {"href": "/currencie/bitcoin/#Markets"})
    for elem in soup_list:
        print(elem)



