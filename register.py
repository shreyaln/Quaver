from tkinter import *

#tkinter works with labels

def registeruser():
    usernameinfo = username.get()
    passwordinfo = password.get()

    #entering it into text file called ?
    file = open(usernameinfo,'w')
    file.write(usernameinfo+',')
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

def loginuser():
    #called when login button clicked
    None
    
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
    
