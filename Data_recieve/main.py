#For reading data in csv format 
import csv 

#For download CSV files form url 
import wget

#For download each minutes 
import time
from chronometer import Chronometer

#For delete and add a new file in Opening System 
import os

#For insert in dataBase 
import sqlite3


print('░█▀█░█▀▄░█▀█░▀▀█░█▀▀░▀█▀░░░▀█▀░▀█▀░█▀█░█▀▀\n'+
'░█▀▀░█▀▄░█░█░░░█░█▀▀░░█░░░░░█░░░█░░█▀▀░█▀▀\n'+
'░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀░░▀░░░░░▀░░▀▀▀░▀░░░▀▀▀\n')


#Url where download csv file 
url = "https://docs.google.com/spreadsheets/d/131_hnZ34_Etby2U3U-xZDf1N8P3ceE0V7ncIfre_Vjw/export?format=csv&id=131_hnZ34_Etby2U3U-xZDf1N8P3ceE0V7ncIfre_Vjw&gid=2147138321"

#How to close this porgramm 
print('To stop process, press CTRL+C')


#index of the last message recieve
lastRow = 0 

 #Connecting to database 
con = sqlite3.connect('/home/jordan/Documents/TIPE/Data_process/Database/DataBase.sqlite')
cur = con.cursor()


while True :
	#wait for 60 seconds 
	long_running_task = lambda: time.sleep(3.)
	with Chronometer() as t:
		long_running_task()  
	
	
	
	#Check if data.csv exsits if true delete it 
	if os.path.exists("data.csv"):
		os.remove("data.csv")

	#Get a new version of data.csv
	wget.download(url, '/home/jordan/Documents/TIPE/Data_recieve/data.csv')




	#Open and read  only data.csv

	with open('data.csv','r') as csv_file: 
		csv_reader = csv.reader(csv_file)  
		lenght = 0 
		data = []
		#Put each line of csv file in a array 
		#Will be easier for reading 

		for line in csv_reader: 
			lenght = lenght + 1 
			data.append(line)


		#Check if last row of csv file is all ready in DB
		for i in range(lenght):
			if i > lastRow :
				print('\n \n New DATA RECIEVE ! ')

				currentData  =  data[i]
				
				date = currentData[0]

				volt = currentData[1]

				amp = currentData[2]

				Long = currentData[3]

				Lat = currentData[4]

				alt = currentData[5]

				Temp = currentData[6]

				print(date)
				

				cur.execute(('insert into data (Volt , Amp, Alt , Long, Lat, Temperature, Time)    values (?, ?,?,?,?,?,?)') , 
					(volt,amp,alt,Long,Lat,Temp,date))
			
				#saving writing in DB
				con.commit()


				#Update last row index
				lastRow = i

			
			if i < lastRow:

				print("NO new DATA RECIEVE ")
				




cur.close()