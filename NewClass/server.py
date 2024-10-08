from flask import Flask, render_template, url_for, request
import requests
import json
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        url = "https://census-toy.nceng.net/prod/toy-census"
        f = open('./data.json', encoding="utf8")
        actionType = {"actionType": "CountByCountry", "top": 0, }, {
            "actionType": "CountByGender", "top": 0, }, {"actionType": "CountPasswordComplexity", "top": 0, }
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
                file.write("<h1>Results " + typeTrimmed + "</h1>" +
                           typeTrimmed + ": " + response.text + "\n")
                file.close

    with open('results.txt', 'r') as file:
        content = file.read()
    return f'<html><body style="background: #7C8082"><div class="main-block"><div class="block-item">{content}</div></body></html>'


if __name__ == '__main__':
    app.run(debug=True)
