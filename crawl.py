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
import requests as req
import logging



logging.basicConfig(filename='reddit.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)



#self.logger = logging.getLogger('urbanGUI')



# import pickle
# dataset = ['hello','test']
# outputFile = 'test.data'
# fw = open(outputFile, 'wb')
# pickle.dump(dataset, fw)
# fw.close()


def try_praw():

	reddit = praw.Reddit(client_id='OdmWFqaQxh6JDQ',
						 client_secret='xocefyZlXYvlOCwyOLcF7WOuxFE',
						 user_agent='android:com.example.myredditapp:v1.2.3 (by /u/kevinljc)')

						 
			
	string = 'daily discussion'
	fw = open(string+'.data','wb')

	print(reddit.read_only)

	dataset = reddit.subreddit('Stocks').search(string)
	print(dataset)
	for submission in dataset:
		print(submission.title)

	pickle.dump(dataset,fw)
	fw.close()
	
	
def try_req(after,before):

	
	url  = "https://api.pushshift.io/reddit/submission/search/?subreddit=stocks&size=500&after={0}&before={1}".format(after,before)
	
	dataset = req.get(url).json()
	
	print("len: "+len(dataset['data']))
	if len(dataset['data']) == 0:
		logging.info('no submission for'+str(after)+str(before))
		return
		
	else:
	
	
		fw = open(str(before)+'--'+str(after)+'.data','wb')
		pickle.dump(dataset,fw)
		fw.close()
		print(dataset)
		print(len(dataset['data']))
		return
	
try:
		
	for i in range(2000):
		print("+"*10)
		before = 1560143153 - i*24*3600
		after = 1560143153	- (i+1)*24*3600
		
		try_req(after,before)
		
		print("+"*10)	
except Exception as e:
	logging.fatal(e, exc_info=True)
	print(e)
		
	
	
	

	





