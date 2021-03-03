# Acquiring designated content CQF on google page

import requests as rq

if __name__ == "__main__":
    url = 'https://www.google.ca/search?'
    kw = str(input('Please enter word you want to search: '))
    # User Agent disguise
    headers = {
        "user - agent": "Mozilla / 5.0(Macintosh; Intel MacOSX10_15_6) AppleWebKit / 537.36(KHTML, "
                        "likeGecko)Chrome/88.0.4324.192Safari/537.36 "
    }
    param = {
        'q': kw
    }
    respond = rq.get(url=url, params=param, headers=headers)
    page_text = respond.text
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write(page_text)
    print("File saved")
