
import requests as rq
import json

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list"
    headers = {
        "User-Agent": "Mozilla / 5.0(Macintosh; Intel MacOSX10_15_6) AppleWebKit / 537.36(KHTML, "
                      "likeGecko)Chrome/88.0.4324.192Safari/537.36 "
    }
    param = {"type": "24",
             "interval_id": "100:90",
             "action": '',
             "start": "0",
             "limit": "20"}
    response = rq.get(url=url, params=param, headers=headers)
    list_data = response.json()
    f = open("./movie.json","w",encoding='utf-8')
    json.dump(obj=list_data,
              fp=f,
              ensure_ascii=False)
    print("Finished")
