#!/usr/bin/env python
# -*- coding:utf-8 -*-

# http://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
from bs4 import Tag
import json
from datetime import datetime

def saveAsRst(dt, title, category, content, rstpath):
    with open(rstpath, 'w') as fo:
        fo.write("#######################################################\n")
        fo.write(title.encode("utf-8"))
        fo.write("\n#######################################################\n\n")
        fo.write(":date: " + dt.isoformat()[:-3] + "+08:00\n")
        fo.write(":tags: \n")
        fo.write(":category: " + category.encode("utf-8") + "\n")
        fo.write(":summary: \n\n\n")
        fo.write(":: \n\n")
        for child in content.children:
            if isinstance(child, Tag):
                if child.name == "br":
                    fo.write("\n")
            else:
                # http://stackoverflow.com/questions/11755208/how-to-remove-m-from-a-text-file-and-replace-it-with-the-next-line
                line = child.strip()
                if len(line) > 0:
                    fo.write("  " + line.encode("utf-8") + "\n")


def parsePost(path, rstpath):
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
        #print(dt.isoformat())

        # parse title
        title = article.find("li", class_="title").find("a").string.strip()
        #print(title)

        # parse category
        category = soup.find("ul", class_="refer").find_all("li")[1].find("a").string.strip()
        #print(category)

        # parse content
        content = soup.find("div", class_="article-content-inner")
        #print(content)

        saveAsRst(dt, title, category, content, rstpath)


if __name__ == '__main__':
  parsePost("42830221", "test%zh.rst")
