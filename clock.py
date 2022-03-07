from plyer import notification
from time import *
from tkinter import *
import datetime
from playsound import playsound
import winsound


root=Tk()

def values():
    print(hour.get())
    print(min.get())
    print(sec.get())
    timing()

def timing():
    while(True):
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        alarm_time=f"{hour.get()}:{min.get()}:{sec.get()}"
        print(current_time,alarm_time)
        if current_time==alarm_time:
            notification.notify(
            title = "ALARM",
            message=(msg.get()) ,
            app_icon="clock.ico",
            timeout=7
)
            playsound("sound1.mp3")
            return
            
        sleep(1)

hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )

mins = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')     


secs = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')  

hour=StringVar(root)
min=StringVar(root)
sec=StringVar(root)
hour.set("hour")
min.set("min")
sec.set("sec")

l=Label(root,text="ALARM CLOCK",font="serif 25 bold",padx=100,fg="#222262").grid(row=0,column=0,columnspan=3)



def time():
    a=strftime("%H:%M:%S %p")
    label.config(text=a)
    label.after(1000,time)
label=Label(root,fg="#f2b6fa",font="serif 15 bold",padx=7,pady=7,bg="black")
label.grid(row=1,column=1)
time()

l1=Label(root,text="Set an alarm ",font="serif 12 italic",pady=10,bg="#222262",padx=175,fg="white").grid(row=2,column=0,columnspan=3,pady=10)


hours1=OptionMenu(root,hour,*hours).grid(row=3,column=0,sticky='e')
mins1=OptionMenu(root,min,*mins).grid(row=3,column=1)
secs1=OptionMenu(root,sec,*secs).grid(row=3,column=2,sticky='w')

m=Label(root,text="Enter a message: ",font="serif 11 bold")
m.grid(row=4,column=0,columnspan=2,sticky='w')

msg=Entry(root,width=35)
msg.grid(row=4,column=1,columnspan=3,pady=10)

submit=Button(root,text="SET",bg="#222262",command=values,padx=20,font="serif 10 bold",fg="white")
submit.grid(row=5,column=1,padx=20,pady=20)
# timing()
# print(current_value.get())
# print(a)

root.mainloop()
