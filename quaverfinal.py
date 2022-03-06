from tkinter import *
import os
import requests
import mysql.connector as m
import pygame
from tkinter import filedialog

#tkinter works with labels

con = m.connect(host='localhost', password='sql123', user='root')

if con.is_connected():
    print('connected')

# creating cursor object
cursor = con.cursor()

#cursor.execute('create database quaver')
cursor.execute("use quaver")

# creating music repository table
"""cursor.execute("create table music_repo(song_name varchar(12),\
album varchar(12),\
artist varchar(12), \
genre varchar(12),duration float(2),song_link varchar(250))")"""
con.commit()        

link1 = 'http://commondatastorage.googleapis.com/codeskulptor-demos/riceracer_assets/music/lose.ogg'
link2 = 'http://commondatastorage.googleapis.com/codeskulptor-demos/DDR_assets/Kangaroo_MusiQue_-_The_Neverwritten_Role_Playing_Game.mp3'
link3 = 'http://codeskulptor-demos.commondatastorage.googleapis.com/pang/paza-moduless.mp3'
link4 = 'http://commondatastorage.googleapis.com/codeskulptor-demos/DDR_assets/Sevish_-__nbsp_.mp3'
link5 = 'http://commondatastorage.googleapis.com/codeskulptor-assets/Epoq-Lepidoptera.ogg'

cursor.execute("insert into music_repo values('Song 1', 'Album 1', 'Artist 1', 'Genre 1', 2.03, '{}')".format(link1))
cursor.execute("insert into music_repo values('Song 2', 'Album 2', 'Artist 2', 'Genre 2', 2.05, '{}')".format(link2))
cursor.execute("insert into music_repo values('Song 3', 'Album 3', 'Artist 3', 'Genre 3', 2.44, '{}')".format(link3))
cursor.execute("insert into music_repo values('Song 4', 'Album 4', 'Artist 4', 'Genre 4', 2.66, '{}')".format(link4))
cursor.execute("insert into music_repo values('Song 5', 'Album 5', 'Artist 5', 'Genre 5', 2.67, '{}')".format(link5))

cursor.execute("select song_link from music_repo")
data=cursor.fetchall()
a=1
var=data[0][0]
doc = requests.get(var)
with open('Beatz'+'.mp3', 'wb') as f:
        f.write(doc.content)

a=2
var=data[1][0]
doc = requests.get(var)
with open('shake it off'+'.mp3', 'wb') as f:
        f.write(doc.content)

a=3
var=data[2][0]
doc = requests.get(var)
with open('we are one'+'.mp3', 'wb') as f:
        f.write(doc.content)

a=4
var=data[3][0]
doc = requests.get(var)
with open('lets go home'+'.mp3', 'wb') as f:
        f.write(doc.content)

a=5
var=data[4][0]
doc = requests.get(var)
with open('believer'+'.mp3', 'wb') as f:
        f.write(doc.content)
        
con.commit()

def play():
    song = songbox.get(ACTIVE)
    song = f"{song}.mp3"

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()

global paused
paused = False

def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused=True

def forward():
    nextsong = songbox.curselection()
    nextsong = nextsong[0]+1
    song = songbox.get(nextsong)
    song = f"{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songbox.selection_clear(0, END)
    songbox.activate(nextsong)
    songbox.selection_set(nextsong, last=None)

def back():
    nextsong = songbox.curselection()
    nextsong = nextsong[0]-1
    song = songbox.get(nextsong)
    song = f"{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songbox.selection_clear(0, END)
    songbox.activate(nextsong)
    songbox.selection_set(nextsong, last=None)
    






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
    global root
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("SUCCESS")
    screen3.geometry("150x100")
    Label(screen3,text = " LOGIN SUCCESSFUL").pack()
    Button(screen3,text = "OK", command = delete2).pack()
    session()
    root = Toplevel(screen)
    root.title("QUAVER")
    root.iconbitmap()
    root.geometry("500x300")
    pygame.mixer.init()
    global songbox
    songbox = Listbox(root, bg ="black", fg ="white", width = 60, selectbackground='gray', selectforeground='black')
    songbox.pack(pady=20)

    
    app()
def app():
    
    backbuttonimage = PhotoImage(file='backward.png') 
    forwardbuttonimage = PhotoImage(file='forward.png')
    playbuttonimage = PhotoImage(file="play.png")
    pausebuttonimage = PhotoImage(file='pause.png')
    stopbuttonimage = PhotoImage(file="stop.png")
    #frame
    controlframe = Frame(root)
    controlframe.pack()

    backbutton = Button(controlframe, image=backbuttonimage,borderwidth = 0, command = back) 
    #border0 to avoid having a box around
    forwardbutton= Button(controlframe, image=forwardbuttonimage,borderwidth = 0, command = forward)
    playbutton= Button(controlframe, image=playbuttonimage,borderwidth = 0, command=play)
    pausebutton= Button(controlframe, image=pausebuttonimage,borderwidth = 0, command=lambda: pause(paused) )
    stopbutton =Button(controlframe, image=stopbuttonimage,borderwidth = 0, command= stop)

    #pushing it onto frame using grid rows and cols
    backbutton.grid(row =0,column =0,padx =6)
    forwardbutton.grid(row =0,column =1,padx =6)
    playbutton.grid(row =0,column =2,padx =6)
    pausebutton.grid(row =0,column =3,padx =6)
    stopbutton.grid(row =0,column =4,padx =6)
    menu1 = Menu(root) # this is in root, not our frame
    root.config(menu = menu1)
    addsongmenu = Menu(menu1)
    menu1.add_cascade(label = "Add A New Song", menu = addsongmenu)
    addsongmenu.add_command(label = "Add song", command = addsong)

    root.mainloop()

def addsong():
    song = filedialog.askopenfilename(initialdir='',title='Choose song', filetypes=(('mp3 Files', '*.mp3'),))
    #song = song.replace(r"C:/Users/shrey/OneDrive/Documents/python shreya/", '')
    song = song.replace('.mp3', '')
    
    songbox.insert(END, song)


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
    
