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


def parserPage(urlList, index_Input):
    # this function recives a list with all of the URL
    # and return a string

    # test`s
    # URL = urlList[0]
    # URL1 = urlList[1]
    # URL2 = urlList[2]
    # URL = 'https://www.publico.pt/2019/10/31/sociedade/noticia/socrates-alega-prestou-ajuda-financeira-varias-mulheres-solidariedade-1892141'
    # URL1 = 'https://www.jn.pt/mundo/galerias/o-halloween-na-terra-que-o-popularizou-muitos-palhacos-maus-uma-batwoman-e-um-galo-11470392.html'
    # URL2 = 'https://www.amazon.co.uk/dp/B07TWFWJDZ/ref=gw_uk_desk_mso_dc_avs_fb2?pf_rd_p=457e28bf-1411-4173-8c3b-2157cd451f29&pf_rd_r=SXCEV9ANDEKTSF0290CG'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

    page = requests.get(urlList[index_Input], headers=headers)

    pageParser = BeautifulSoup(page.content, 'html.parser')

    # TagWords = pageParser.find_all("title").get_text()
    # Tag_Words = pageParser.find(id="title").get_text().strip()
    Tag_Words = pageParser.find("title").get_text().strip()

    # return string contains title`s
    return Tag_Words

def verify(Tag_Words_Input, word_Input):
    # this function verify if the pre determinated word_input exist`s in the page
    list = Tag_Words.rsplit()
    for word in list:
        flag = False
        if (word == word_Input):
            flag = True
            break
        else:
            flag = False

    return flag

# SMTP protocol
def send_message(Tag_Words_Input, url):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # this password is generated with "google app passwords"
    from_mail = '@gmail.com'
    to_mail = '@gmail.com'
    password = ''
    server.login(from_mail, password)

    # message
    message = MIMEMultipart()
    message['From'] = from_mail
    message['To'] = to_mail
    message['Subject'] = 'Founded Tags: ' + str(url)
    body = 'Check the link: ' + str(url)
    # message = ("From: %s\r\nTo: %s\r\n\r\n"
    #       % (from_mail, to_mail))
    # message = message + subject + body
    message.attach(MIMEText(body, 'plain'))
    message = message.as_string()
    # https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail
    server.sendmail(from_mail, to_mail, message)
    # debug final message
    # print(message)
    print('Send Success!')

    # finnaly end server session
    server.quit()

# main
if __name__ == '__main__':

    # parserPage function
    # this list need`s work
    # depending in the method of input for the user of the app
    urlList = ['', '', '']
    urlList[0] = 'https://www.publico.pt/2019/10/31/sociedade/noticia/socrates-alega-prestou-ajuda-financeira-varias-mulheres-solidariedade-1892141'
    urlList[1] = 'https://www.jn.pt/mundo/galerias/o-halloween-na-terra-que-o-popularizou-muitos-palhacos-maus-uma-batwoman-e-um-galo-11470392.html'
    urlList[2] = 'https://www.amazon.co.uk/dp/B07TWFWJDZ/ref=gw_uk_desk_mso_dc_avs_fb2?pf_rd_p=457e28bf-1411-4173-8c3b-2157cd451f29&pf_rd_r=SXCEV9ANDEKTSF0290CG'
    urlList[3] = 'https://www.publico.pt/tecnologia'
    Tag_Words = parserPage(urlList, 0)
    print(Tag_Words)

    # verify function
    # the string passed to the function need work
    flag = verify(Tag_Words, "que")
    print(flag)

    # email tests
    send_message(Tag_Words, urlList[0])
