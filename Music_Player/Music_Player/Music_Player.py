import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pygame
import time 
from threading import *
import os

Pause = False
Num=0
win = Tk()
path="C://Users//tirtha//source//repos//Music_Player//music"    
dir_list=os.listdir()                                        #  You can add path in listdir("") to specify any other specific folder without pasting
                                                             #  the program in same folder with the music files
song_list=[]
count=len(dir_list)
for i in range(count):
    if dir_list[i].endswith('.mp3'):
        song_list.append(dir_list[i])

pygame.mixer.init()

def Tracker():
        #Tracker()
        while(True):
            Pos=pygame.mixer.music.get_pos()
            Pos=round(Pos/1000.0,1)
            print(str(Pos)+ ' Second')
            time.sleep(0.095)
            os.system('CLS')

def Prev():
    
    
    pygame.mixer.music.unload()
    global Num
    Num=Num-1
    if Num<0:
        Num=0
    pygame.mixer.music.load(song_list[Num])
    pygame.mixer.music.play(loops=0)

    

def Play():
    global Pause
    #if pygame.mixer.music.get_busy():
    if Pause:
        Pause= False
    else:
       Pause= True
    if Pause:
        pygame.mixer.music.pause()
    else:
       pygame.mixer.music.unpause()
    
    
    
    #else:
    #    pygame.mixer.music.unpause()
        #pygame.mixer.music.load(str(Num)+'.mp3')
        #pygame.mixer.music.play(loops=0)
    #pygame.mixer.music.unload()
    #global Num
    #if Num<0:
    #    Num=0
    #elif Num>2:
    #    Num=2
    #pygame.mixer.music.load(str(Num)+'.mp3')
    #pygame.mixer.music.play(loops=0)


def Next():
    pygame.mixer.music.unload()
    global Num
    Num=Num+1
    if Num>2:
        Num=2
    pygame.mixer.music.load(song_list[Num])                   #  str(Num)+'.mp3'
    pygame.mixer.music.play(loops=0)

win.geometry("1000x400")
#background=Label(win, bg='red').pack()
###############################################################
frame1 = Frame(win, width=50, height=50,bg='red')
frame1.pack()
frame1.place(anchor='center', relx=0.2, rely=0.5)

img1 = ImageTk.PhotoImage(Image.open('prev.png'))
#label1 = Label(frame1, image = img1 )
#label1.pack()
button1=Button(frame1, image=img1, command=Prev)
button1.pack()
################################################################

################################################################
frame2 = Frame(win, width=50, height=50,bg='red')
frame2.pack()
frame2.place(anchor='center', relx=0.5, rely=0.5)

img2 = ImageTk.PhotoImage(Image.open('play.png'))
#label2 = Label(frame2, image = img2 )
#label2.pack()
button2=Button(frame2, image=img2, command=Play)
button2.pack()
################################################################

################################################################
frame3 = Frame(win, width=400, height=400,bg='red')
frame3.pack()
frame3.place(anchor='center', relx=0.8, rely=0.5)

img3 = ImageTk.PhotoImage(Image.open('next.png'))
#label3 = Label(frame3, image = img3 )
#label3.pack()
button3=Button(frame3, image=img3, command=Next)
button3.pack()
################################################################
print(dir_list)
print(song_list)
#time.sleep(2)
thread1 = Thread(target=Tracker)
thread1.start()

thread2= Thread(target=win.mainloop())
thread2.start()
