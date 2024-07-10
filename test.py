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
    type = str(actionType[i])
    typeTrimmed = type[16:-12]
    

    with open("results.txt", "a") as file:
        file.write(response.text + "\n")
        file.close
    
    results_list = []
    json_array = json.loads(response.text)
    for item in json_array:
        result_details = {"name":None, "value":None}
        result_details['name'] = item['name']
        result_details['value'] = item['value']
        results_list.append(result_details['name'] + ": " + str(result_details['value']))
   
    print(typeTrimmed + "\n" + str(results_list))
    