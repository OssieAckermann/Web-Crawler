import requests as rq


if __name__ == '__main__':
    # Make sure url is the image address
    url = "https://i.ytimg.com/vi/e3xdGx7Xa4w/maxresdefault.jpg"
    img_data = rq.get(url= url).content

    with open("./Task1_Alita.jpg",'wb') as fp:
        fp.write(img_data)