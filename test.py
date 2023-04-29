import requests
import json

url = "https://census-toy.nceng.net/prod/toy-census"
f = open('./data.json', encoding="utf8")
actionType = {"actionType":"CountByCountry","top":0,},{"actionType":"CountByGender","top":0,},{"actionType":"CountPasswordComplexity","top":0,}
users = json.load(f)

with open("results.txt", "w") as file:
        file.write("")
        file.close

for i in range(len(actionType)):

    payload = actionType[i] | users
    response = requests.post(url, json=payload)
    print(response.text + "\n")
    type = str(actionType[i])

    typeTrimmed = type[16:-12]


    with open("results.txt", "a") as file:
        file.write(typeTrimmed + ": "  + response.text + "\n")
        file.close
    
