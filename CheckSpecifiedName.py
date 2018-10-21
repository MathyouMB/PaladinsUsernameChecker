import time
from selenium import webdriver
from time import sleep
from time import gmtime, strftime

print('Paladins-Name-Check------------------------------ '+strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print(" ")
#driver = webdriver.Chrome("C:/PythonPractice/chromedriver.exe")
driver = webdriver.PhantomJS()
name = input("Enter the name you would like to check: ")
while name != 'q':
	print(" ")
	print("	    	Checking "+(str(name+'\n'))+"-----------------------------------------")
	driver.get("http://paladins.guru/profile/pc/"+(str(name)))
	sleep(3)
	if ((str(driver.current_url)) == (str("http://paladins.guru/"))):
		print(" ")
		print(name+" is available, banned, blocked by administration, or does not follow username guidelines.")
		OpenList = open("openList.txt",'a')
		OpenList.write((str(name)))
		print("Wrote to file...")
	else:
		print(" ")
		print(name+" is taken.")	
	name = input("Enter the name you would like to check (or 'q' to quit): ")
driver.quit()