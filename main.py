import easyocr
import cv2
from matplotlib import pyplot as plt
import urllib.request
import numpy as np
import os
import requests


def givetextfromimage(url, langue):
    page = requests.get(url)
    f_ext = os.path.splitext(url)[-1]
    f_name = 'img{}'.format(f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)

    reader = easyocr.Reader([langue])

    resultTExt = reader.readtext(f.name, detail=0)

    print(resultTExt)


def showtextdetection(url, langue):
    page = requests.get(url)

    f_ext = os.path.splitext(url)[-1]
    f_name = 'img{}'.format(f_ext)
    with open(f_name, 'wb') as f:
        f.write(page.content)
        print(f.name)

    reader = easyocr.Reader([langue])
    result = reader.readtext(f.name)

    top_left = tuple(result[0][0][0])
    bottom_right = tuple(result[0][0][2])
    text = result[0][1]
    font = cv2.FONT_HERSHEY_SIMPLEX

    img = cv2.imread(f.name)
    spacer = 100
    for detection in result:
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
        text = detection[1]
        img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
        img = cv2.putText(img, text, (20, spacer), font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
        spacer += 15

    plt.imshow(img)
    plt.show()


def showdetectionfromlocalimage(url, language):
    reader = easyocr.Reader([language])
    result = reader.readtext(url)

    top_left = tuple(result[0][0][0])
    bottom_right = tuple(result[0][0][2])
    text = result[0][1]
    font = cv2.FONT_HERSHEY_SIMPLEX

    img = cv2.imread(url)
    spacer = 100
    for detection in result:
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
        text = detection[1]
        img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
        img = cv2.putText(img, text, (20, spacer), font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
        spacer += 15

    plt.imshow(img)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://parade.com/.image/t_share/MTkwNTc1ODc5NDk1MjMwNTg5/life-quotes-happy.jpg'

    # givetextfromimage(url,'en')
    showtextdetection(url, 'en')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
