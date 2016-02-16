#!/bin/bash
# wget webpages from http://www.aia.or.th/prayerXX.htm
# Google search: bash print number with leading zeros
# run this script with the following command on Ubuntu 15.10
# $ bash wget-webpages.sh
# the following command is not working:
# $ sh wget-webpages.sh

for i in {1..3}
do
  wget "http://nanomi.pixnet.net/blog/listall/$i" -P nanomi
  sleep .3
done
