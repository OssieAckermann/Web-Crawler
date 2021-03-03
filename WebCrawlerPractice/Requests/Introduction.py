
import requests as rq

if __name__ == "__main__":
    url = 'https://www.google.ca/'
    respond = rq.get(url=url)
    page = respond.text
    print(page)
