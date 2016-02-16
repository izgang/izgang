#!/usr/bin/env python
# -*- coding:utf-8 -*-

# http://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import json

def parseHTML(path):
  urls = []
  with open(path, 'r') as f:
    soup = BeautifulSoup(f)
    div_id_content = soup.find(id="content")
    table = div_id_content.find("table")
    for link in table.find_all("a"):
      url = link.get("href")
      #print(url)
      urls.append(url)

  return urls

if __name__ == '__main__':
  urls = []
  urls.append(parseHTML("nanomi/1"))
  urls.append(parseHTML("nanomi/2"))
  urls.append(parseHTML("nanomi/3"))
  print(urls)
  with open("urls.json", 'w') as fo:
    fo.write(json.dumps(urls))
