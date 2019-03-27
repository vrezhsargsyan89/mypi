import os
SENDMAIL = '/usr/sbin/sendmail'

def send_mail ():
	""" This function sends email with HTML table"""
	TO =  ["vsargsya@qti.qualcomm.com"]
	SUBJECT = 'FME(D)A Test'
	#COLOR = 'palegreen'
	COLOR = '#F7CFCF '
	html_file = open('html.txt','r')
	html_cnt = html_file.read()
	
	message = html_cnt % (", ".join(TO), SUBJECT, COLOR, COLOR, "%")	
	
	p = os.popen ("%s -t -i" % SENDMAIL, "w")
	p.write(message)
	status = p.close()
	if status:
			print "Sendmail exit status", status

send_mail()
