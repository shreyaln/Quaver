from tkinter import *
import os
#tkinter works with labels


#The Entry widget allows you to enter a sing-line text.
#In Tkinter, to create a textbox, you use the Entry widget:

def registeruser():
    usernameinfo = username.get()
    passwordinfo = password.get()

    #entering it into text file called ?
    file = open(usernameinfo,'w')
    file.write(usernameinfo+'\n')
    file.write(passwordinfo+'\n')
    file.close()

    #This clears the fields once a registration is done 
    usernameentry.delete(0, END)
    passwordentry.delete(0,END)

    #TELL USER THAT REGISTRATION IS DONE
    Label(screen1, text = "You have been registered succcessfully!", fg = "green", font = ("Calibri",11)).pack()

def register():
    #new screen screen1 is equated to top level of our original screen
    '''The toplevel widget is used when a python application needs
    to represent some extra information, pop-up, or the group of widgets on the new window.'''
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register for QUAVER")
    screen1.geometry("300x250")

    #The Tkinter StringVar helps you manage the value of a widget such as a Label or Entry more 
    #effectively
    global username
    global password
    global usernameentry
    global passwordentry
    username = StringVar()
    password = StringVar()
    
    Label(screen1,text="Please Enter Your Details Below to Register").pack()
    Label(screen1,text="").pack() 
    Label(screen1,text="Username *").pack()
    #entry is for input
    usernameentry = Entry(screen1, textvariable = username)
    usernameentry.pack()
    Label(screen1,text="Password *").pack()
    passwordentry = Entry(screen1,textvariable = password)
    passwordentry.pack()
    Label(screen1,text="").pack()
    Button(screen1, text = "REGISTER",width = 10, height = 1,command = registeruser).pack()

    # we are creating 2 entries and assigning them to store value in the text variable
def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()
def session():
    #everytime a user logs in, he is given a session
    None
def loginsuccess():

    #make this go to our main quaver page
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("SUCCESS")
    screen3.geometry("150x100")
    Label(screen3,text = " LOGIN SUCCESSFUL").pack()
    Button(screen3,text = "OK", command = delete2).pack()
    session()
def passwordwrong():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("PASSWORD ERROR")
    screen4.geometry("250x100")
    Label(screen4, text=" PASSWORD NOT RECOGNISED!").pack()
    Button(screen4, text="OK", command=delete3).pack()


def usernotfound():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("USERNAME ERROR")
    screen5.geometry("150x100")
    Label(screen5, text=" USER NOT FOUND!").pack()
    Button(screen5, text="OK", command=delete4).pack()



def loginuser():
    #called when login button clicked
    username1 = usernameverify.get()
    password1 = passwordverify.get()

    usernameentry1.delete(0,END)
    passwordentry1.delete(0,END)

    #to get files in working directory list
    listoffiles = os.listdir()
    #this returns a list of all files in our current directory

    if username1 in listoffiles:
        file1 = open(username1,'r')
        if password1 in file1.read().splitlines() and password1 !=username1:
            loginsuccess()
            print("LOGIN SUCCESS")
        else:
            passwordwrong()
            print("Password is wrong!")
    else:
        usernotfound()
        print("User not found!")
    
def login():
    #pretty much just like the register function
    print("bing bam boom")
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")

    global usernameverify
    global passwordverify
    global usernameentry1
    global passwordentry1
    
 
    Label(screen2,text="Please Enter Your Details Below to Login").pack()
    Label(screen2,text="").pack()

    usernameverify = StringVar()
    passwordverify = StringVar()
    Label(screen2,text="Username").pack()
    usernameentry1 = Entry(screen2, textvariable = usernameverify)
    usernameentry1.pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Password").pack()
    passwordentry1 = Entry(screen2,textvariable = passwordverify)
    passwordentry1.pack()
    Label(screen2,text="").pack()
    Button(screen2, text = "LOGIN",width = 10, height = 1,command = loginuser).pack()
 
def mainscreen():
    #Main Screen with all options
    global screen # coz we access it in register func too
    screen =Tk() #SCREEN VARIABLE
    screen.geometry("300x250") # to set screen size
    screen.title("THIS IS A TITLE") # SETTING TITLE
    #first label
    Label(text = "QUAVER LOGIN", bg= "grey", width = "300", height = "2", font = ("Calibri",13)).pack()
    #pack adds it to screen
    Label(text="").pack() #this is a blank label to leave a line on screen 
    Button(text="LOGIN",height = "2", width = "30", command = login).pack()
    Button(text = "Register",height = "2", width = "30", command = register).pack()
    #default packing in centre
    screen.mainloop()#ADDS THE SCREEN VARIABLE TO MAIN PROGRAM LOOP, IMP

    #packing makes sure that even if we change window size, buttons are still
    #aligned
    
#MAIN PROGRAM
mainscreen()
    
