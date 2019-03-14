#!/usr/bin/python3
#-*- coding: UTF-8 -*-

import re
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as Soup

#making the request and getting the html
URL = 'https://loteriasdominicanas.com/loteka'
UCLIENT = ureq(URL)
HTML = UCLIENT.read()
SOUP = Soup(HTML, "html.parser")

def scrapping():
    #numbers of the lottery gonna be there
    numbers = []

    #credentials of the lottery
    title = SOUP.find_all('a')[4].get_text()
    subtitle = SOUP.find_all('span')[6].get_text()
    date = SOUP.find_all('span', {'class':'session-date'})[0].get_text()
    clean_date = re.sub(r'\s\s+', '', date)

    #making the magic right over there
    for i in range(0, 3):
        number = SOUP.find_all('span', {'class':'score'})[i].get_text()
        reg = re.sub(r'\n*', '', number)
        second_reg = re.sub(r'\s\s+', '', reg)
        numbers.append(second_reg)

    #aaaand, printing it all
    print("lottery: %s\nSub tittle: %s\nDate: %s\nNumbers: %s, %s, %s"\
          %(title, subtitle, clean_date, numbers[0], numbers[1], numbers[2]))

if __name__ == '__main__':
    scrapping()

