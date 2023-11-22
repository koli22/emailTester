import smtplib
from email.message import EmailMessage
import sys
from datetime import datetime
import string
import time
import random

endline = "\n"

def send_email_gmail(subject, message, destination, numOfAttachments):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    #This is where you would replace your password with the app password
    server.login('kborec982@gmail.com', 'qwrv ymsh xsyl rcmc')

    msg = EmailMessage()

    message = f'{message}\n'
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = 'josty@centrum.cz'
    msg['To'] = 'josty@centrum.cz'
    
    for i in range(numOfAttachments):
        with open('palo.pdf', 'rb') as content_file:
            content = content_file.read()
            msg.add_attachment(content, maintype='application', subtype='pdf', filename='palo.pdf')

    server.send_message(msg)
    
def generateNewConsoleFile(nameofconsolefile):
    fp = open(nameofconsolefile + '.txt', 'w')
    fp.write(getTimeReport() + ":    created new file!" + endline)
    fp.close()

def writeToFile(line, nameofconsolefile):
    fp = open(nameofconsolefile + '.txt', 'a')
    fp.write(getTimeReport() + ":    " + line + endline)
    fp.close()
    
def getTimeReport():
    return datetime.now().isoformat()
    
    
arguments = sys.argv
filename = 'console'
maxNum = 100
delay = 300
generateNewFile = "t"
printToCon = "f"
printToFile = "t"

"""
if len(arguments) > 3:
    filename = arguments[3]

if len(arguments) > 1:
    if (arguments[1] == 'f' or arguments[1] == 't'):
        if (arguments[1] == 't'):
            generateNewConsoleFile(filename)
            generateNewFile = "t"
    else:
        raise ValueError("you can set the first argument to t/f")
    
if len(arguments) > 5:
    if (arguments[5] == 'f' or arguments[5] == 't'):
        if (arguments[5] == 't'):
            printToCon = "t"
    else:
        raise ValueError("you can set this argument to t/f")
            
if len(arguments) > 2:
    try:
        maxNum = int(arguments[2])
    except:
        print("failed to set maxNum value")
        
if (len(arguments) > 4):
    try:
        delay = int(arguments[4])
    except:
        print("you can set the delay in seconds")
        
"""

if (len(arguments) == 2 and (arguments[1] == "help")):
    print ("'file=' sets the name of report file. 'None' or 'none' doesn't write to any file")
    print ("'new=' can be set to t/f. t creates new file, f writes to old one")
    print ("'loops=' sets the amount of emails")
    print ("'delay=' sets the time between emails")
    print ("'cons=' can be set to t/f. t gives report to console, f doesn't")
    
    sys.exit()
    
ind = 0

for arg in arguments:
    if (ind == 0):
        ind = 1
        
    if (arg[:5] == "file="):
        if (arg == "file="):
            raise ValueError("file has to have a name")
        elif (arg[5:] == "none" or arg[5:] == "None"):
            printToFile = "f"
        else:
            filename = arg[5:]
            
    elif (arg[:4] == "new="):
        if (arg == "new=t"):
            generateNewFile = "t"
        elif (arg == "new=f"):
            generateNewFile = "f"
        else:
            raise ValueError("you can set this value only as t/f")
        
    elif (arg[:6] == "loops="):
        try:
            value = int(arg[6:])
            maxNum = value
        except:
            raise ValueError("loops can be only a number")
        
    elif (arg[:6] == "delay="):
        try:
            value = int(arg[6:])
            delay = value
        except:
            raise ValueError("delay can be only a number")
        
    elif (arg[:5] == "cons="):
        if (arg == "cons=t"):
            printToCon = "t"
        elif (arg == "cons=f"):
            printToCon = "f"
        else:
            raise ValueError("this value can be only t/f")
    else:
        if (ind > 1):
            raise ValueError("unknown settings, try 'file help'")
            

if (filename != "None" and filename != "none" and generateNewFile == "t"):
    generateNewConsoleFile(filename)

index = 0

print ("loops: " + str(maxNum))
print ("output file: " + filename)
print ("generate new file: " + generateNewFile)
print ("delay: " + str(delay))
print ("print to console: " + printToCon)
print ("print to file: " + printToFile)

print("\n---------------------------------------")

while index < maxNum:
    time.sleep(delay)
    
    emailLength = random.randint(1,10000)
    numberOfAttachments = random.randint(0,5)
    
    textString = ""
    
    for i in range(emailLength):
        if (random.randint(1,30) == 2):
            textString += "\n"
        elif (random.randint(1,10) == 3):
            textString += " "
        else:
            textString += random.choice(string.ascii_letters)
        
    subject = "Test: " + str(index) + " - " + str(emailLength) + " - " + str(numberOfAttachments)
    
    send_email_gmail(subject, textString, 'kborec982@gmail.com', numberOfAttachments)
    
    if (filename != "none" and filename != "None"):
        writeToFile("sent email: " + subject, filename)
    
    if (printToCon == 't'):
        print(getTimeReport() + ":    sent email: " + subject)
    
    index+=1
    
