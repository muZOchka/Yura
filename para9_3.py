import requests
res_pars_list = []
response = requests.get("https://coinmarketcap.com/")

response_text = response.text
response_parse = response_text.split("<span>")
for elem_1 in response_parse:
    if elem_1.startswith("$"):
        for elem_2 in elem_1.split("</span>"):
            if elem_2.startswith("$") and elem_2[1].isdigit():
                res_pars_list.append(elem_2)


print(res_pars_list[0])

