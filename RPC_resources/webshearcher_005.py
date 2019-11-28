# !/usr/local/bin/python

# HTTP
import requests
# SCTP
# https://docs.python.org/3/library/email.examples.html
import smtplib
# https://pypi.org/project/beautifulsoup4/
from bs4 import BeautifulSoup
# for the header of the email message
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText

# from email.mime.multipart import MIMEMultipart
# from email.mime.multitext import MIMEText

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
# SMTP
# https://tools.ietf.org/html/rfc822.html

import csv
import numpy as np

import sys
# sys.path.append('F:/Dropbox/Dir_simaoppcastro/Eng/Mestrado/1ano/RedesProtocolosComunicacao/Projecto/1test')

import utils_rpc.py as ut

# def parserPage(urlList, index_Input):
def parserPage(urlList):
    # this function recives a list with all of the URL
    # and return a string

    ListTag_words = []
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

    for i in urlList:
        page = requests.get(i, headers=headers)

        pageParser = BeautifulSoup(page.content, 'html.parser')

        # TagWords = pageParser.find_all("title").get_text()
        # Tag_Words = pageParser.find(id="title").get_text().strip()
        Tag_Words = pageParser.find("title").get_text().strip()
        # Tag_Words = pageParser.find("title")

        print(Tag_Words)
        ListTag_words.append(Tag_Words)

    # return string contains title`s
    #return Tag_Words
    return ListTag_words

# for verify if exists what we want
def verifyPage(Tag_WordsList, word_Input):
    # this function verify if the pre determinated word_input exist`s in the page
    for i in Tag_WordsList:
        list = i.rsplit()
        for word in list:
            flag = False
            if (word == word_Input):
                flag = True
                break
            else:
                flag = False
            # debug
            print(flag)

    return flag


# main
if __name__ == '__main__':

    # parserPage function
    urlList = ut.urlListInput('urlList.csv')

    List1 = parserPage(urlList)
    print(List1)

    # verify function
    # the string passed to the function need work
    # flag = verifyPage(Tag_WordsList, "que")
    # print(flag)



    #if flag:
        # email tests
        #(Tag_Words, urlList[3])

