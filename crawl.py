#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : crawl.py
# @Software: PyCharm
# @comments:
# @First_version : 10/1/2018 2:53 PM v0.1.0
# @This_version  : 10/1/2018 2:53 PM v0.1.0
# All rights reserved by Jiacheng Liu.
# import requests as req
#
# url = "http://data.eastmoney.com/report/#dHA9MCZjZz0wJmR0PTImcGFnZT0x"
# url = "http://www.hibor.com.cn/microns_1_2.html"
# url = "http://vis.10jqka.com.cn/free/ybzx/index/ctime/-3/pageNum/472/curPage/2"
#
# url = "https://www.reddit.com/r/stocks/new/.json"
# head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
#
# a = req.get(url,headers =head)
# print(a.content.decode("utf-8"))
import praw
import pickle

# import pickle
# dataset = ['hello','test']
# outputFile = 'test.data'
# fw = open(outputFile, 'wb')
# pickle.dump(dataset, fw)
# fw.close()

reddit = praw.Reddit(client_id='OdmWFqaQxh6JDQ',
                     client_secret='xocefyZlXYvlOCwyOLcF7WOuxFE',
                     user_agent='android:com.example.myredditapp:v1.2.3 (by /u/kevinljc)')

print(reddit.read_only)

for submission in reddit.subreddit('Stocks').top(limit=25):
    print(submission.title)