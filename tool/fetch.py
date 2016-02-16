#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import json

def parseHTML(path, outpath):
  urls = []
  with open(path, 'r') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    for link in soup.find_all("a"):
      urls.append(link.get("href"))

  with open(outpath, 'w') as fo:
    fo.write(json.dumps(urls))

if __name__ == '__main__':
  # "http://nanomi.pixnet.net/blog/listall/1"
  #parseHTML("nanomiAll1.html", "1.json")
