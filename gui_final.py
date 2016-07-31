from Tkinter import *
import Tkinter 
import Tkconstants
import tkFileDialog
import mp3play
import tkFont
import os
import ttk
import sys
import re
from os import listdir
from os.path import isfile, join

#regular expression pattern 
pat1= r"(0110|0111|0100|1001|1011|1000|11|00|01\b|10\b){1,100}"

#input string
ipstr=sys.argv[1]


#validate the input string using the regex
match=re.search(pat1, ipstr)
if match:
	ipstr= match.group(0)
else:
	print "No match!"
	
indice=0


nextip=""

#array to store the playlist
#play_List=[]

#mediaplayer instance
music=None
#array to store track's path
trackLocations = []

#variable to hold the current track id in the list
idx=0

def nextop():
    global ipstr
    global indice
    global nextip
    global idx 
    global music
    global trackLocations
    global name

    print "00 Play Previous\n01 Play\n10 Stop\n11 Play Next"
    print "\n"
     
    try: 
         nextip=ipstr[indice]+ipstr[indice+1]
    except:
         music.stop()
         print "user input EOL"
         
         #loop control variable
         control=True
         while control:
         
          ipstr=raw_input("enter new input: ")
         
          match=re.search(pat1, ipstr)
         
          if match:
                ipstr= match.group(0)
                control=False
          else:
                print "No match!"
                control=True
                
         indice=0
         nextip=ipstr[indice]+ipstr[indice+1]

    print "\n"
    print "Input String :",ipstr 
    
    indice+=2
    
    if nextip == "01":
       pieces=trackLocations[int(idx)].split("\\")
       name.set(pieces[-1])
       print "\n"
       print "Current input : ",nextip," (play current)"
       print "Now Playing : ",pieces[-1]
       print "\n"
       music.play()
       
    elif nextip == "10":
       pieces=trackLocations[int(idx)].split("\\")
       name.set(pieces[-1])
       print "\n"
       print "Current input : ",nextip," (stop)"
       print "\n"
       music.stop()
       
    elif nextip == "11":

       if idx < (count-1):
        idx+=1
       elif idx == (count-1):       
        idx=0
        
#      print "idx",idx
       music.stop()
       pieces=trackLocations[int(idx)].split("\\")
       name.set(pieces[-1])
       music = mp3play.load(trackLocations[int(idx)])
       print "\n"
       print "Current input : ",nextip," (play next)"
       print "Now Playing : ",pieces[-1]
       print "\n"
       music.play()
       
    elif nextip == "00":

       if idx != 0:
        idx-=1
       elif idx == 0:
        idx=count-1
        
#       print "idx",idx
       music.stop()
       pieces=trackLocations[int(idx)].split("\\")
       name.set(pieces[-1])
       music = mp3play.load(trackLocations[int(idx)])
       print "\n"
       print "Current input : ",nextip," (play previous)"
       print "Now Playing : ",pieces[-1]
       print "\n"
       music.play()

               
    root.after(10000, nextop) # every 10 seconds....

#function to load the mp3 files
def open_file():
   global play_List
   global trackLocations
   global music
   global name
   filename.set(tkFileDialog.askopenfilename(defaultextension = ".mp3",filetypes=[("All Types", ".*"), ("MP3", ".mp3")]))
   playlist =filename.get()
   playlist_pieces = playlist.split("/")
   play_list.set (playlist_pieces[-1])
   playl = play_list.get()
   play_list_display.insert(END, playl)
#   print filename.get()
   music = mp3play.load(filename.get())
   pieces = filename.get().split("/")
   trackLocations += [filename.get()]
   name.set(pieces[-1])


#function to play the mp3 file
def musicplay():
  music.play()


#funtion to stop the mp3 file
def musicstop():
  music.stop() 


#function to play previous mp3 in the playlist
def musicprev():
  global idx 
  global music
  global trackLocations
  global name
  idx-=1
#  print "idx",idx
  music.stop()
  pieces=trackLocations[int(idx)].split("/")
  name.set(pieces[-1])
  music = mp3play.load(trackLocations[int(idx)])
  music.play()

 
#function to play previous mp3 in the playlist
def musicnext():
  global idx 
  global music
  global trackLocations
  global name
  idx+=1
#  print "idx",idx
  music.stop()
  pieces=trackLocations[int(idx)].split("/")
  name.set(pieces[-1])
  music = mp3play.load(trackLocations[int(idx)])
  music.play()
  

#function to change the selection in the playlist by mouse click
def tune_changed(event):
   global trackLocations
   global music
   global idx
   global name
   idx = event.widget.curselection()[0]
 #  print "idx",idx
   pieces=trackLocations[int(idx)].split("\\")
   name.set(pieces[-1])
   music = mp3play.load(trackLocations[int(idx)])
   music.play()
   print ("Now playing %s" % event.widget.get(idx))


#GUI

#Tk object instantiation
root=Tk()
root.resizable(width=FALSE, height=FALSE)
root.title("BCI MP3 Player")
root.geometry("350x100+550+200")
root.configure(background='gray19')


filename = StringVar()
name = StringVar()
name.set("no file selected")
play_list = StringVar()



#label to hold current file name
filenamelabel = Label(root, textvariable = name,bg="Dark Slate grey", fg="green",width="47")
filenamelabel.pack(ipady=10,pady=10)

#menu container
menubar = Menu(root)
filemenu = Menu(menubar, bg="Dark Slate grey", fg="green")
menubar.add_cascade(label='File', menu = filemenu)
filemenu.add_command(label='Open', command = open_file)
root.config(menu=menubar)

#load images fot the buttons
playphoto=PhotoImage(file=".\images\play.gif")
prevphoto=PhotoImage(file=".\images\prev.gif")

#this label is used just for the adjustment with the positioing of the buttons
nulllabel = Label(root,width="10",bg="gray19")
nulllabel.pack(padx=10,pady=2,side=LEFT)

prevbtn=Button(root,text="previous",command=musicprev,width="20",bg="gray19")
prevbtn.config(image=prevphoto,height="20")
prevbtn.pack(padx=5,pady=2,side=LEFT)

playbtn=Button(root,text="play",command=musicplay,bg="gray19")
playbtn.config(image=playphoto,width="20",height="20")
playbtn.pack(padx=5,pady=2,side=LEFT)

stopphoto=PhotoImage(file=".\images\stops.gif")
stopbtn=Button(root,text="stop",command=musicstop,bg="gray19")
stopbtn.config(image=stopphoto,width="20",height="20")
stopbtn.pack(padx=5,pady=2,side=LEFT)

nextphoto=PhotoImage(file=r".\images\next1.gif")
nextbtn=Button(root,text="next",command=musicnext,bg="gray19")
nextbtn.config(image=nextphoto,width="20",height="20")
nextbtn.pack(padx=5,pady=2,side=LEFT)

#playlist window gui
play_list_window=Toplevel(root,height="400",width="400")
play_list_window.geometry("%dx%d%+d%+d" % (350, 300,550, 355))
play_list_window.title("Playlist")
play_list_display = Listbox(play_list_window, selectmode=EXTENDED,width =300,height=400, bg="gray19",fg="green")
play_list_display.bind("<Double-Button-1>",tune_changed)
play_list_display.pack()

#autoloads the playlist
count=0
files_abs = []
dir_path=".\songs"
#dir_path="C:\Users\sreekumar\Desktop\project\songs"
for file in os.listdir(dir_path):
 if ".mp3" in file:
   count=count+1
   play_list_display.insert(END, file)
   temppath=dir_path+"\\"+file
 #  print "temppath",temppath
   trackLocations+=[temppath]
 #  print trackLocations



#print "count",count
#print "\n"
#print trackLocations

#print "\n\n\n\n\n"
print "Input String :",ipstr
print "\n"
#print "\n\n\n\n\n"

music = mp3play.load(trackLocations[int(idx)])


nextop()

#keep the mainloop running
root.mainloop()

#ENDOFGUI


