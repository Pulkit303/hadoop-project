#!/usr/bin/python2

import cgi,cgitb
import commands,time
cgitb.enable()

print "Content-type:text/html"
print ""

# taking data from apache and storing into web variable
web=cgi.FieldStorage()
# getting hadoop version
h_version=web.getvalue('h1')

if h_version =='hv1':
	clstr=web.getvalue('dropdown1')
	if clstr=='nn':
		print 'Starting the requested machine'
		print commands.getoutput('sudo virsh start h1')
		print 'Booting the machine'
		time.sleep(40)
		print commands.getoutput('sudo ansible-playbook /etc/ansible/playbooks/n1.yml')
	elif clstr =='dn':
                print 'Starting the requested machines'
		print commands.getoutput('sudo virsh start h1')
                print commands.getoutput('sudo virsh start h1dn')
                print 'Booting the machine'
                time.sleep(40)
                print commands.getoutput('sudo ansible-playbook /etc/ansible/playbooks/dn.yml')
	elif clstr =='jt':
                print 'Starting the requested machine'
                print commands.getoutput('sudo virsh start h1')
		print commands.getoutput('sudo virsh start h1dn1')
                print 'Booting the machine'
                time.sleep(40)
                print commands.getoutput('sudo ansible-playbook /etc/ansible/playbooks/tt.yml')
	else:
		print 'Select one of the above options'
elif h_version =='hv2':
	oop=web.getvalue('dropdown2')
	if oop =='nn2':
		print 'Starting the requested machine'
		print commands.getoutput('sudo virsh start h2')
		print "Booting the machine"
		time.sleep(40)
		print commands.getoutput('sudo ansible-playbook /etc/ansible/playbooks/n2.yml')
	elif oop =='dn1':
		print 'Starting the requested machines'
		print commands.getoutput('sudo virsh start h2')
		print commands.getoutput('sudo virsh start h2dn1')
		print "Booting the machines"
		time.sleep(40)
		print commands.getoutput('sudo ansible-playbook /etc/ansible/playbooks/c1.yml')
	elif oop =='dn2':
		print 'Starting the requested machines'
		print commands.getoutput('sudo virsh start h2')
		print commands.getoutput('sudo virsh start h2dn1')
		print commands.getoutput('sudo virsh start h2dn2')
		print "Booting the machines"
		time.sleep(40)
		print commands.getoutput('sudo ansible-playbook /etc/ansible/playbooks/c2.yml')
	elif oop =='dn3':
		print 'Starting the requested machines'
                print commands.getoutput('sudo virsh start h2')
                print commands.getoutput('sudo virsh start h2dn1')
                print commands.getoutput('sudo virsh start h2dn2')
		print commands.getoutput('sudo virsh start h2dn3')
                print "Booting the machines"
                time.sleep(40)
                print commands.getoutput('sudo ansible-playbook /etc/ansible/playbooks/c3.yml')
	elif oop =='dnr':
		print 'Starting the requested machines'
                print commands.getoutput('sudo virsh start h2')
                print commands.getoutput('sudo virsh start h2dn1')
                print commands.getoutput('sudo virsh start h2dn2')
                print commands.getoutput('sudo virsh start h2dn3')
                print "Booting the machines"
                time.sleep(40)
                print commands.getoutput('sudo ansible-playbook /etc/ansible/playbooks/nm.yml')
	else: 
		print "Please select one of the above"
else:
	print "Select one of the given two options"
