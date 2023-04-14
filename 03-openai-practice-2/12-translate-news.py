import json
import openai
import os
import requests
# pip install requests || poetry add requests

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

STATUS = {"OK": "ok"}

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
response = requests.get(url)
# print(json.dumps(response.json()) )

_response = response.json()
cnt = 0
if _response['status'] == STATUS["OK"]:
    for article in _response["articles"]:
        _article = f"title: {article['title']}"
        _description = f"description: {article['description']}"

        prompt = f"Translate the following 'title' and 'description' in Korean \n```\n{_article}\n{_description}```"
        r = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
        )
        print(r['choices'][0]['text'])

        if cnt > 3:
            break
        cnt += 1



# title: 누출된 문서, 미국의 라틴아메리카와 아프리카에 대한 러시아와 중국의 영향력 증가에 대한 걱정 공개 - CNN
# description: 누출된 비공개 펜타곤 문서는 라틴 아메리카와 아프리카에 대한 러시아와 중국의 영향력이 증가하고 있음에 대한 미국의 걱정을 밝혀냈습니다.


# 타이틀 : Demar DeRozan & Zach LaVine, ESPN NBA에서 토론토를 겨루는 플레이인 토너먼트 승리 반응 | ESPN - ESPN
# 해설 : Demar DeRozan과 Zach LaVine은 Cassidy Hubbarth와 함께하여 No. 10 시카고 불스가 19점의 하락부터 돌아오는 방법에 대해 논의합니다. 토론토를 겨루는 승리를 얻었습니다.


# title: 제이미 폭스, '의료 사유' 발생 후 '회복 중' - PEOPLE
# description: 제이미 폭스의 가족은 그는 화요일 의료 사유가 발생한 후 회복하고 있음을 공식 발표했으며, 지금은 개인적인 공간에 대한 자제를 요청했다.


# title: 엘론 머스크가 미디어와 대결: BBC 면접에서 트위터 CEO는 당당하게 선을 들어냈다 - CNBC Television
# description: 브라이언 술리바네가 주임하는 "라스트 콜"은 돈과 문화, 현 정책의 교차점을 탐구하는 재미 있는 빠른 기업 프로그램입니다. 월요일에 맞춰..


# 리즈 해리스 아리조나 국회 의원 배출 에호감리 검토 후 - ABC15 Arizona
# 아리조나 주지사회가 공화당 리즈 해리스를 국회에서 배출하기로 투표했습니다. 해리스는 국회의 동료들에 의해 투표로 배출되었습니다.