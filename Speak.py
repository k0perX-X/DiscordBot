import requests
import json

def zapros(id, text):
    url = 'https://aiproject.ru/api/'
    headers = {'Content-type': 'application/x-www-form-urlencoded',
               'Content-Encoding': 'utf-8'}
    data = {"ask":text,"userid":str(id),"key":""}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    print(answer)
    response = answer.json()
    return response


if __name__ == "__main__":
    print(zapros(13213132, 'Привет как дела'))