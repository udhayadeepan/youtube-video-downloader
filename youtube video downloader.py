from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import string
import time
import os
win=Tk()
win.title("YOUTUBE VIDEO DOWNLOADER")
win.geometry('400x400')
win.resizable(0,0)
win.configure()
image_path=str(os.getcwd())+"\you.png"
bg=PhotoImage(file=image_path)
label1=Label(win,image=bg)
label1.place(x=0,y=0)
label2=Label(win,text=" YOUTUBE VIDEO DOWNLOADER\nBy:https://github.com/udhayadeepan")
label2.grid(pady=5)
def start():
      label2.grid_forget()
      label1.place_forget()
      b.grid_forget()
      Label(win,text="YOUTUBE VIDEO DOWNLOADER").grid(ipady=10,row=0,column=1,pady=20,padx=30)
      Label(win,text="Enter URL:").grid(row=1,column=0,padx=20)
      url=Entry(win)
      url.grid(row=1,column=1,sticky="nsew")
      Label(win).grid(row=2,column=1)
      Label(win,text="Enter Path:").grid(row=3,column=0)
      path=Entry(win)
      path.grid(row=3,column=1,sticky="nsew")

      def browse():
            global Path
            Path = filedialog.askdirectory(initialdir="Downlaod path")
            path.delete(0,END)
            path.insert(0,Path)
            
            
      def download():
            try:
                  down.configure(text="processing")
                  ch=radio.get()
                  res=[]
                  print(url.get())
                  yt=YouTube(str(url.get()))
                  res=[stream.resolution for stream in yt.streams.filter(progressive=True)]
                  
                  length=len(res)
                  if ch==0 or ch> length:
                        ch=1
                        lab.configure(text="No resolution selected:Default-144p")                 
                  stream=yt.streams.filter(res=str(res[ch-1]),progressive=True)
                  stream=stream[0]
                  stream.download(Path)
                  url.delete(0,END)
                  path.delete(0,END)
                  down.configure(text="Download")
                  lab.configure(text="Successfully Downloaded")
                  
            except:
                  lab.configure(text="--ERROR--")
                  url.delete(0,END)
                  path.delete(0,END)
                  down.configure(text="Download")
                  
      Button(win,text="Browse Path",command=browse).grid(row=4,column=1,pady=5,sticky="e")
      Label(win,text="Select resolution").grid(row=5,column=1,pady=10,sticky="nsew")

      radio=IntVar()
      r1=Radiobutton(win,text="Low",variable=radio,value=1).grid(pady=5,row=6,column=1,sticky="nsew")
      r1=Radiobutton(win,text="Medium",variable=radio,value=2).grid(row=7,column=1,pady=5,sticky="nsew")
      r1=Radiobutton(win,text="High",variable=radio,value=3).grid(row=8,column=1,pady=5,sticky="nsew")





      down=Button(win,text="Download",bg="light blue",comman=download)
      down.grid(row=9,column=1,pady=15,sticky="nsew")
      lab=Label(win)
      lab.grid(row=10,column=1,sticky="nsew")
b=Button(win,text="start",bg="light blue",command=start)
b.grid(padx=200,pady=330)

win.mainloop()


