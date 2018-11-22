from email_sender import send_mail
import csv
import os
# Add your processing code here


def find(name) : 
	#print (os.listdir('Invi'))
	for i in os.listdir('IC') :
		if i.lower().split('.pdf')[0] in name.lower() :
			return os.path.join(os.getcwd(), 'Invig/' + i)


# We are using a dict to store mail info
mail = {}


email = []
name = []

a = open('ic.txt', 'r')






#_list = ['Aruna Malapati', 'PK Sahoo', 'TSL Radhika']


count =0
_list = os.listdir('IC') 
_list.sort()

f = open('InvigilatorsEmails.csv', 'r') 
count_Send = 0
reader = csv.reader(f)
for row in reader :
	email.append(row[1])
	name.append(row[0])

for i in range (len(_list)): 
	mail = {}
	file = _list[i]
	for n in range(len(name)) : 
		if file.split('.pdf')[0].lower() in name[n].lower() :
						
			#print (email[n])
			#print (name[n])
			#print (find(name[n]))

			mail['sender'] = 'timetable@hyderabad.bits-pilani.ac.in'
			mail['reciever'] = email[n]
			mail['subject'] = 'Invigilation Duty'
			with open('text.txt', 'r') as f : 
				mail['body'] = f.read().format(name[n])
			mail['file'] = os.path.join(os.getcwd(), 'Invig/'+ file)

			send_mail(mail)
			count_Send += 1
	if mail == {} :
		count += 1
		a.write(_list[i])
		a.write("\n")
		print ('DID NOT SEND : ' + file)
	
print (count, count_Send) 
a.close()



'''
_listic = ["Pranjal Gupta"]
for name in _listic : 
	#for row in reader : 
		#if (name.lower() in row[0].lower()) :
	mail = {}
	mail['sender'] = 'timetable@hyderabad.bits-pilani.ac.in'
	mail['reciever'] = 'f20170124@hyderabad.bits-pilani.ac.in'
	mail['subject'] = 'IC Sheet'
	with open('text.txt', 'r') as f : 
		mail['body'] = f.read().format(name)
	mail['file'] = "Ic/ARUNA MALAPATI.pdf"

	print (mail)
	send_mail(mail)'''
