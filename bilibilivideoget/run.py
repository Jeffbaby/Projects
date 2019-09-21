import requests
import random
import time
from urllib.parse import urlencode

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
base_url = "https://api.vc.bilibili.com/board/v1/ranking/top?"

for i in range(1):
    parms = {
        "page_size": 10,
        "next_offset": i*10+1,
        "tag": "今日热门",
        "platform": "pc"
    }

    response = requests.get(base_url + urlencode(parms))
    res_json = response.json()
    
    for item in res_json['data']['items']:
        name = item['item']['description']
        url = item['item']['video_playurl']
        response_mp4 = requests.get(url, headers=headers, stream=True)
        if response_mp4.status_code == 200:
            for data in response_mp4.iter_content(chunk_size=1024):
                with open(name+".mp4", mode="ab") as f:
                    f.write(data)
        time.sleep(random.randint(2, 6))
