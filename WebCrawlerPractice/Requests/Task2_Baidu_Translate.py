
import requests as rq
import json

if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'
    kw = str(input('Please enter word you want to translate: '))
    # User Agent disguise
    headers = {
        "User-Agent": "Mozilla / 5.0(Macintosh; Intel MacOSX10_15_6) AppleWebKit / 537.36(KHTML, "
                      "likeGecko)Chrome/88.0.4324.192Safari/537.36 "
    }
    data = {
        'kw': kw
    }
    response = rq.post(url=post_url, data=data, headers=headers)
    dic_obj = response.json()

    fp = open('./'+kw+'.json', 'w', encoding='utf-8')
    json.dump(obj=dic_obj, fp=fp, ensure_ascii=False)

