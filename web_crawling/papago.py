import requests
import json

app_id = "tpZMojrmWvCvXqpDfeql"
app_pw = "*******" # 파파고 api 어플리케이션 시크릿으로 값 변경 필요

def papago():
    x = input('번역이 필요한 영어를 입력하세요 : ')
    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id" : app_id,
        "X-Naver-Client-Secret" : app_pw
    }

    data = {
        "source" : "en",
        "target" : "ko",
        "text" : x
    }

    resp = requests.post(url, headers=header, data=data)

    resp.text

    json_data = json.loads(resp.text)

    json_data['message']['result']['translatedText']
    
    return json_data['message']['result']['translatedText']
    