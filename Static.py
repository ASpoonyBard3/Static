#Static
#An application to create artificial web traffic. The idea is to hide in the forest of data that would be useless to anyone who might be monitoring your connection, and make it as hard as possible for them to differentiate between real and fake traffic
#Released under the MIT license.

from urllib.request import *
from os import *
from random import *
from time import *
from walkerLib import *

listOfSites=[]
variety=4 #Increase the variety of addresses to use so that once they figure out what's fake more fake addresses will begin to appear, confusing the attacker
#You'll want at least 40 or so websites in your safeWebsiteList.txt and make sure they aren't something that would cause anyone to suspect anything (e.g: torproject.org), it's also a good idea to add different areas of the website
maxVariety=0
maxVisitFrequency=30 #Define the maximum time the program should wait before visiting another site
maxPages=10 #Define the maximum amount of pages the program should view on a given site
curPages=0.0 #The max pages for the given 'session'
frequency=0
currently_visiting=""
connection=""

def gap():
	print("_________________________________________________________________")
def errorGap():
	print("=================================================================")

def write_log(entry):
	with open('Static_Log.txt','a') as output:
		output.write(entry + '\n')

f = open(path.dirname(path.realpath(__file__))+"/safeWebsiteList.txt", "r")
for i in f:
	listOfSites.append(i.replace("\n","")) #Load the file into memory, removing the new line escape code
f.close()

maxVariety=len(listOfSites)


#print(listOfSites)
while 1==1:
	gap()
	frequency=randrange(maxVisitFrequency)
	curPages=(frequency//maxPages)
	if variety<maxVariety:
		if randrange(10)==1: #Chance of increasing variety
			variety+=1
			gap()
			print("Variety increased, variety is now "+str(variety))
			gap()
	
	currently_visiting=listOfSites[randrange(len(listOfSites[0:variety]))]
	if randrange(10)==1: #Chance of misspelling the web address
		for i in range(randrange(len(currently_visiting)//4)): #Decide how many letters to misspell
			currently_visiting=currently_visiting.replace(currently_visiting[randrange(len(currently_visiting))],chr(randrange(32,128)))
		gap()
		print("Looks like I misspelled some letters!")
		gap()
			
	
	
	print("Currently 'visiting' http://"+ currently_visiting)
	try:
		urlopen("http://"+currently_visiting)
	except:
		print("There was an error connecting to "+currently_visiting+", I probably misspelt it")
	
	
	for i in crawl("http://"+currently_visiting, curPages):
		sleep(curPages)
		try:
			urlopen(i)
			print("		Clicked on "+i)
		except:
			print("There was an error connecting to "+currently_visiting+", I probably misspelt it")
			
			