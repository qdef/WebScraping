import matplotlib.pyplot as plt
import psycopg2
import requests
import time
from lxml import html

try:
	connstring = "dbname='quxwmelo' user='quxwmelo' host='horton.elephantsql.com' password='q8Hks013GlhDWaJ6xHJHxuUa2T6Pv_zJ'"
	print("Connecting to database %s..." %(connstring))
	conn = psycopg2.connect(connstring)
	print("Connection is successful.")
except:
	print("Failed to connect to the database")
	
cursor = conn.cursor()


cursor.execute("select Count from TwitterAutoIncrement")
X = cursor.fetchall()
cursor.execute("select Followers from TwitterAutoIncrement")
Y = cursor.fetchall()
x=[]
y=[]
for i in range(len(X)):
	x.append(X[i][0])
	
for k in range(len(Y)):
	y.append(Y[k][0])

print(x)

print(y)

conn.close()


plt.plot(x,y)

plt.axis([1,25,31757000, 31758000])

plt.ylabel('Followers')

plt.xlabel('Samples')

plt.show()

