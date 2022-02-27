import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pygame
import time 
from threading import *
import os
import tkinter.ttk as ttk
from mutagen.mp3 import MP3

change=False
wait=False
Length=1
slider_pointer=1
volume_pointer=0
Pause = False
Num=0
win = Tk()
path="C://Users//tirth//source//repos//Music_Player//music"        #  You can add path in listdir("") to specify any other specific folder without pasting
                                                                   #  the program in same folder with the music files
dir_list=os.listdir()
song_list=[]
count=len(dir_list)
for i in range(count):
    if dir_list[i].endswith('.mp3'):
        song_list.append(dir_list[i])

pygame.mixer.init()

def slide(x):
    global change
    global wait
    change=True
    pygame.mixer.music.pause()
    global slider_pointer
    wait=True
    global Length
    slider_pointer=my_slider.get()
    print(round(slider_pointer,1))
    #percent=(Slide_pointer/100)*Length
    slider_label.config(text=slider_pointer)
    slider_pointer=round(slider_pointer,1)
    
    pygame.mixer.music.set_pos(slider_pointer)
    #time.sleep(0.09)
    
    #my_slider.config(value=slider_pointer)
    pygame.mixer.music.unpause()
   
    wait=False

    #time.sleep(0.05)


def volume(y):
    global volume_pointer
    volume_pointer=volume_slider.get()
    volume_pointer=100-volume_pointer
    volume_label.config(text=int(volume_pointer))
    pygame.mixer.music.set_volume(volume_pointer/100.0)
    


def Tracker():
        #Tracker()
    while True:
        global wait
        #if wait:
        #    time.sleep(1)
        while wait==False:#time.sleep(0.095)
            global Pos
            global change
            
            #Pos=slider_pointer
            Pos=pygame.mixer.music.get_pos()
            Pos=round(Pos/1000.0,1)
            if change:
                #Pos=slider_pointer
                Pos=int(my_slider.get())
                change=False
                print('slider_pointer=',slider_pointer)
                print('NEW POS=',Pos)
            if Pos==-0.0:
                Pos=0.0
            print(str(Pos)+ ' Second')
            #present=(Pos/Length)*100
            #pygame.mixer.music.set_pos(slider_pointer)
            my_slider.config(value=Pos)             #value=pygame.mixer.music.get_pos()/1000.0
            slider_label.config(text=Pos)
            #present=round(present)
            # slider_label.config(text=present)
            time.sleep(0.095)  
            os.system('CLS')
        print('EXIT')


def Refresh():
    my_slider.config(value=0)
    slider_label.config(text='0')


def Prev():
    Refresh()
    global Length
    pygame.mixer.music.unload()
    global Num
    Num=Num-1
    if Num<0:
        Num=0
    pygame.mixer.music.load(song_list[Num])
    song=MP3(song_list[Num])
    Length = song.info.length
    Size=round(Length)
    print(Size)
    my_slider.config(to=Size)
    #print(Length)
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
    Refresh()
    global Length
    pygame.mixer.music.unload()
    global Num
    Num=Num+1
    if Num>2:
        Num=2
    
    #print(Length)

    pygame.mixer.music.load(song_list[Num])                   #  str(Num)+'.mp3'
    song=MP3(song_list[Num])
    Length = song.info.length
    Size=round(Length)
    print(Size)
    my_slider.config(to=Size)
    pygame.mixer.music.play(loops=0)

win.geometry("1000x400")
#Label(win, bg='red').pack()
###############################################################
frame1 = Frame(win)
#frame1.pack()
#frame1.place(anchor='center', relx=0.2, rely=0.5)
frame1.grid(row=2,column=0,padx=20,pady=50)

img1 = ImageTk.PhotoImage(Image.open('prev.png'))
#label1 = Label(frame1, image = img1 )
#label1.pack()
button1=Button(frame1, image=img1, command=Prev)
button1.pack()
################################################################

################################################################
frame2 = Frame(win)
#frame2.pack()
#frame2.place(anchor='center', relx=0.5, rely=0.5)
frame2.grid(row=2,column=1,padx=20,pady=50)

img2 = ImageTk.PhotoImage(Image.open('play.png'))
#label2 = Label(frame2, image = img2 )
#label2.pack()
button2=Button(frame2, image=img2, command=Play)
button2.pack()
################################################################

################################################################
frame3 = Frame(win)
#frame3.pack()
#frame3.place(anchor='center', relx=0.8, rely=0.5)
frame3.grid(row=2,column=2,padx=20,pady=50)

img3 = ImageTk.PhotoImage(Image.open('next.png'))
#label3 = Label(frame3, image = img3 )
#label3.pack()
button3=Button(frame3, image=img3, command=Next)
button3.pack()

my_slider=ttk.Scale(win,from_=0,to=100,value=0,orient=HORIZONTAL,length=400,command=slide)
my_slider.grid(row=9,column=1,padx=20,pady=20)

slider_label=Label(win,text='0')
slider_label.grid(row= 11, column=1)

volume_slider=ttk.Scale(win,from_=0,to=100,value=0,orient=VERTICAL,length=200,command=volume)
volume_slider.grid(row=2,column=3,padx=90,pady=20)

volume_label=Label(win,text='100')
volume_label.grid(row=4,column=3,pady=20)
#Entry(win,width=50,borderwidth=5).grid(row=5,column=1)
################################################################
print(dir_list)
print(song_list)
#time.sleep(2)
thread1 = Thread(target=Tracker)
thread1.start()

thread2= Thread(target=win.mainloop())
thread2.start()
