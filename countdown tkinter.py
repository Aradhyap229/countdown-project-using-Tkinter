import time
from tkinter import *
from tkinter import messagebox

clockWindow = Tk()
clockWindow.geometry("700x700")
clockWindow.title("countdown  For Raksha Bandhan ")
clockWindow.configure(background ="purple")

dayString = StringVar()
hourString = StringVar()
minuteString = StringVar()
secondString = StringVar()


dayString.set("00")
hourString.set("00")
minuteString.set("00")
secondString.set("00")


dayTextbox = Entry(clockWindow , width=3, font=("calibri",20,""), textvariable=dayString)
hourTextbox =Entry(clockWindow , width=3, font=("calibri",20,""), textvariable=hourString)
minuteTextbox = Entry(clockWindow , width=3, font=("calibri", 20,""), textvariable=minuteString)
secondTextbox = Entry(clockWindow, width=3,font=("calibri", 20,""), textvariable = secondString)


dayTextbox.place(x=120 ,y=180)
hourTextbox.place(x=170 , y=180)
minuteTextbox.place(x=220 , y=180)
secondTextbox.place(x=270 , y=180)

def runTimmer():
    try:
        clockTime = int(dayString.get())*24*3600 + int(hourString.get())*3600+ int(minuteString.get())*60 + int(secondString.get())
    except:
        print("incorret Values")


    while(clockTime> -1):
        # making updates
        storeTime = clockTime
        totalDays = storeTime//(24*3600)
        storeTime = storeTime%(24*3600)
        totalHours = (storeTime)//3600
        storeTime %= 3600
        totalMinutes = storeTime//60
        storeTime %=60
        totalSeconds = storeTime

        dayString.set("{0:2d}".format(totalDays))
        hourString.set("{0:2d}".format(totalHours))
        minuteString.set("{0:2d}".format(totalMinutes))
        secondString.set("{0:2d}".format(totalSeconds))
        clockTime -= 1
        clockWindow.update()
        time.sleep(1)

    if(clockTime == 0):
        messagebox.showinfo("", "your time has expired")
    clockTime -= 1
setTimeButton=Button(clockWindow, text='Set Time' , bd='5', command=runTimmer)
setTimeButton.place(x=230 , y=250, anchor=CENTER)
clockWindow.mainloop()
