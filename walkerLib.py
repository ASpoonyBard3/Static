#WalkerLib originally by /u/anserk
#This library takes a given URL and searches for a given amount of links from the page

from urllib.request import urlopen, Request
from urllib.error import URLError
from bs4 import BeautifulSoup
from datetime import datetime



def crawl(url,number,user_agent):

	try:
		html = BeautifulSoup(urlopen(Request(url, headers={'User-Agent': user_agent})).read())
		urls = []
		listOfLinks=html.find_all('a')
		
		for a in listOfLinks[0:number]:
			link = a.get('href')
			if link:
				if link[0] == '/':
					link = url + link
				urls.append(link)

		print("	Found link on page: "+url)

	except Exception as e:
		print('	Error in walker library URL:{}.ERROR:{}'.format(url,e))
		return []
	
	return urls
