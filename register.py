#!C:\Python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<center><h2>Thank You For Wonderla Online Booking<a href='/Wonderla'><br><br>Back to Home</a></h2></center>")

form=cgi.FieldStorage()
fName=form.getvalue("Name")
fLocation=form.getvalue("Location")
fTickets=form.getvalue("Tickets")
fAmount=form.getvalue("Amount")
fContact=form.getvalue("Contact")


#print(fName,fLocation,fTickets,fAmount,fContact)


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Wonderla"
)

mycursor=mydb.cursor()

Sql="INSERT INTO customer(Name,Location,Tickets,Amount,Contact)VALUES(%s,%s,%s,%s,%s)";
val=(fName,fLocation,fTickets,fAmount,fContact)

mycursor.execute(Sql,val)
mydb.commit()
print("</html>")
print("</body>")
