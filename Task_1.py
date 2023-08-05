import pyautogui 
from tkinter import *
from tkinter.filedialog import *


win = Tk()
win.title("Screeshot Taker")
win.geometry("500x300")
win.config(bg = "gray")
def take_ss():
    ss = pyautogui.screenshot()
    save_path = asksaveasfilename()
    ss.save(save_path)                


button = Button(win,text = "Take ScreenShot",font =("Time New Roman",20),background="white",command = take_ss,border=5 )
button.place(x=50,y=100,height=75,width=385)



win.mainloop()