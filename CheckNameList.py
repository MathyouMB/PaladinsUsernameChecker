import time
from selenium import webdriver
from time import sleep
from time import gmtime, strftime

print('Paladins-Name-Check------------------------------ '+strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print(" ")
#driver = webdriver.Chrome("C:/PythonPractice/chromedriver.exe")
driver = webdriver.PhantomJS()
nameTable = []
i = 0
with open('namelist.txt') as my_file:
    for line in my_file:
        nameTable.append(line)
for line in nameTable:
	print(" ")
	print("	    	Checking "+(str(nameTable[i]))+"-----------------------------------------")
	driver.get("http://paladins.guru/profile/pc/"+(str(nameTable[i])))
	sleep(3)
	if ((str(driver.current_url)) == (str("http://paladins.guru/"))):
		print(" ")
		print(nameTable[i].strip()+" is available, banned, or blocked by administration.")
		OpenList = open("openList.txt",'a')
		OpenList.write((str(nameTable[i])))
		print("Wrote to file...")
	else:
		print(" ")
		print(nameTable[i].strip()+" is taken.")	
	i+=1
driver.quit()