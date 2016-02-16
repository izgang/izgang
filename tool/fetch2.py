#!/usr/bin/env python
# -*- coding:utf-8 -*-

# http://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import json
from datetime import datetime

def parsePost(path):
    with open(path, 'r') as f:
        soup = BeautifulSoup(f)
        article = soup.find(id="article-box")
        #print(article.prettify())

        # parse datetime
        # http://stackoverflow.com/questions/5041008/handling-class-attribute-in-beautifulsoup
        month = article.find("span", class_="month").string.strip()
        day = article.find("span", class_="date").string.strip()
        year = article.find("span", class_="year").string.strip()
        hm = article.find("span", class_="time").string.strip()
        # http://stackoverflow.com/questions/466345/converting-string-into-datetime
        # https://en.wikipedia.org/wiki/List_of_time_zone_abbreviations
        tstr = month + " " + day + " " + year + " " + hm
        #print(tstr)
        # http://stackoverflow.com/questions/13182075/how-to-convert-a-timezone-aware-string-to-datetime-in-python-without-dateutil
        dt = datetime.strptime(tstr, "%b %d %Y %H:%M")
        print(dt.isoformat())

        # parse title
        title = article.find("li", class_="title").find("a").string.strip()
        print(title)

        # parse category
        category = soup.find("ul", class_="refer").find_all("li")[1].find("a").string.strip()
        print(category)

        # parse content
        content = soup.find("div", class_="article-content-inner")
        print(content)


if __name__ == '__main__':
  parsePost("42830221")
