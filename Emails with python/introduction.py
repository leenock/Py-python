# send emails with python and how to check our inbox for received  messages.

import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

x = smtp_object.ehlo()
print(x)

z = smtp_object.starttls()
print(z)

import getpass

email = getpass.getpass("Email:")
password = getpass.getpass("Password: ")
print(smtp_object.login(email,password))

recepient = 'djamburidennis@hotmail.com '
from_address = email
to_address =  recepient
subject = input("Enter the subject line:")
message = input("Enter the body message: ")
msg = "Subject: "+subject+'\n'+message

print(smtp_object.sendmail(from_address,to_address,msg) )

smtp_object.quit()