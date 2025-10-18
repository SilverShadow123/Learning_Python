import os
from fileinput import filename
import time
from os import path
import smtplib
import pywhatkit as kit
import time

recipients = ['']
message = "Brother its late at night but i have to say something. the truth is your wife is having an affiar with me . i hope you can forgive me"

# Send message to each number
for number in recipients:
    print(f"Sending message to {number}...")
    kit.sendwhatmsg_instantly(
        phone_no=number,
        message=message,
        wait_time=10,
        tab_close=True,
        close_time=3
    )
    print(f"Message sent to {number} ✅")
    time.sleep(5)

print("All messages sent successfully 🎉")



def func(*args,**kwargs):
    for i in kwargs.items():
       print(i, end=' ')

func(a=20,b=23,c=43)

smObj = smtplib.SMTP('smtp.gmail.com', 587)
smObj.ehlo()
smObj.starttls()
smObj.login('test@gmail.com', '1234')
# recipents =['test@gmail.com', 'test11@gmail.com']

for i in range(10):
    smObj.sendmail('test@gmail.com', 'test1@gmail.com', 'Subject: From Test\n\nDear friend, if you find this email i hope you know that your child is mine. But i cant send child support so hang in there')
    time.sleep(1)
    print(i, 'recipents')

smObj.quit()










smtpObj=smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('asdf@gmail.com', 'afsdf')
smtpObj.sendmail('asdsdf@gmail.com', 'asdf@gmail.com', 'Subject: Dragon the King')
smtpObj.quit()
def createFile(dest):
    if not (path.isfile(dest)):
        f=open(dest, 'w')
        f.write('Welcome to python scripting')
        f.close()
dest = 'C:/Users/Sunan/PyCharmMiscProject/Learning Python/sample.txt'
createFile(dest)
print('File created')




epc=time.time()
localtime = time.localtime(epc)
print(epc)
print(localtime)
print(time.asctime(localtime))
print(time.ctime())
print(time.ctime(epc))




def current_directory():
    cwd = os.getcwd()
    print("Current working directory:", cwd)

def file_path(filename):
    path=os.path.abspath((filename))
    print(path)




filename='sample.txt'
file_path(filename)
current_directory()