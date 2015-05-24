#Static
#An application to create artificial web traffic. The idea is to hide in the forest of data that would be useless to anyone who might be monitoring your connection, and make it as hard as possible for them to differentiate between real and fake traffic
#Released under the MIT license.

from http.client import *
from os import *
from random import *
from time import *
listOfSites=[]
variety=4 #Increase the variety of addresses to use so that once they figure out what's fake more fake addresses will begin to appear, confusing the attacker
#You'll want at least 40 or so websites in your safeWebsiteList.txt and make sure they aren't something that would cause anyone to suspect anything (e.g: torproject.org), it's also a good idea to add different areas of the website
maxVariety=0
maxVisitFrequency=30 #Define the maximum time the program should wait before visiting another site
frequency=0
currently_visiting=""
f = open(path.dirname(path.realpath(__file__))+"/safeWebsiteList.txt", "r")
for i in f:
	listOfSites.append(i.replace("\n","")) #Load the file into memory, removing the new line escape code
f.close()

maxVariety=len(listOfSites)


#print(listOfSites)
while 1==1:
	
	if variety<maxVariety:
		if randrange(10)==1: #Chance of increasing variety
			variety+=1
			print("Variety increased, variety is now "+str(variety))
	
	currently_visiting=listOfSites[randrange(len(listOfSites[0:variety]))]
	if randrange(10)==1: #Chance of misspelling the web address
		for i in range(randrange(len(currently_visiting)/4)): #Decide how many letters to misspell
			currently_visiting=currently_visiting.replace(currently_visiting[randrange(len(currently_visiting))],chr(randrange(32,128)))
			
	
	if randrange(2)==1:
		HTTPConnection(currently_visiting)
		print("Currently 'visiting' http://"+ currently_visiting)
	else:
		HTTPSConnection(currently_visiting)
		print("Currently 'visiting' https://"+ currently_visiting)
	frequency=randrange(maxVisitFrequency)
	print("Waiting for "+str(frequency)+" seconds before 'visiting' another site")
	sleep(frequency)