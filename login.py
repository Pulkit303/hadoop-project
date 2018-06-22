#!/usr/bin/python2


import cgi,cgitb
import commands,time
cgitb.enable()

print "Content-type:text/html"
print ""

#taking data from apacheand storing into web variable
web=cgi.FieldStorage()

# taking user name
user=web.getvalue('u')
# taking password 
password=web.getvalue('p')

if user == "root" and password == "q":
	print "<a href='http://192.168.100.1/service.html'>"
	print "Click here to go to Hadoop Services"
	print "</a>"
else:
	print "wrong values redirecting to login page"
	time.sleep(3)
	print "<a href='http://192.168.100.1/index.html'>"
	print "Click here to try again"
	print "</a>"
