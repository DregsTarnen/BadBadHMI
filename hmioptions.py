#!/usr/bin/env python3
from tkinter import *
import os
import subprocess
#window parameters
window = Tk()
window.geometry("1000x1000")
window.title("HMI Options")
#user feedback labels
aliasstatus = "cat /etc/environment | grep _JAVA_OPTIONS= | cut -b 46- | sed 's/.$//'"
data = subprocess.check_output(aliasstatus, shell=True)
status = data.decode("utf-8")
lbltext = "Anti-Alias default is ON. It is currently: "+status
lblalias = Label(window, text=lbltext, font=("Verdana", 22))
lblalias.pack()
#command to turn on anti-alias
def antialiason():
    directions = "_JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=on'"
    with open('/etc/environment', 'w') as file:
        file.write(directions)
    aliasstatus = "cat /etc/environment | grep _JAVA_OPTIONS= | cut -b 46- | sed 's/.$//'"
    data = subprocess.check_output(aliasstatus, shell=True)
    status = data.decode("utf-8")
    lbltext = "Anti-Alias default is ON. It is currently: "+status
    lblalias.configure(text=lbltext)
#command to turn off anti-alias
def antialiasoff():
    directions = "_JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=off'"
    with open('/etc/environment', 'w') as file:
        file.write(directions)
    aliasstatus = "cat /etc/environment | grep _JAVA_OPTIONS= | cut -b 46- | sed 's/.$//'"
    data = subprocess.check_output(aliasstatus, shell=True)
    status = data.decode("utf-8")
    lbltext = "Anti-Alias default is ON. It is currently: "+status
    lblalias.configure(text=lbltext)
#close the app
def closeapp():
    os.system('pkill python')
#button turn on anti-alias
btnantialiason = Button(window, text="Anti-Alias ON", command=antialiason)
btnantialiason.pack()
#button turn off anti-alias
btnantialiasoff = Button(window, text="Anti-Alias OFF", command=antialiasoff)
btnantialiasoff.pack()
#button to close app
btnclose = Button(window, text="CLOSE", command=closeapp)
btnclose.pack()
lblwarn = Label(window, text="YOU MUST REBOOT FOR CHANGES TO TAKE EFFECT!", font=("Verdana", 22))
lblwarn.pack()
#window main loop
window.mainloop()
 
