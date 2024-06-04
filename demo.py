# Project-1 ( Student Report card generator using tkinter ) -:


# School Mark Sheet

from tkinter import *
from tkinter.messagebox import askokcancel
win = Tk()

def get_data():
   name = st_name_1.get()
   try:
    hindi = hindi_name_1.get()
    english = english_name_1.get()
    science = science_name_1.get()
    sst = sst_name_1.get()
    math = math_name_1.get()
   except ValueError:
        print("Please enter valid numeric values for marks.")
        return

   total = hindi+english+math+science+sst 

   per = (total/500)*100

   div = ""
   if per>=60:
        div = "first divison"
   elif per<60 and per>=50:
        div = "second divison"
   elif per<50 and per>=35:
        div = "third divison"
   else:
        div = "fail"
   messagebox(name,total,per,div) 
   
def messagebox(*data):   
    print_1 = f""" 
    Name : {data[0]}
    Total : {data[1]}
    Percentage :  {data[2]}
    Divison : {data[3]}"""
    askokcancel(title="Ws Cube E School", message=print_1)



#-------------------------------------------------------------------------------------------------------------------------------------------#
win.config(bg="yellow")
win.title("Wscube E School")
win.iconbitmap("earth_planet_icon_263082.ico")
win.geometry("650x650")
win.resizable(False,False)
#-------------------------------------------------------------------------------------------------------------------------------------------#
# title name
school_name = Label(win,text="Wscube E School",font=("Times New Roman",40,"bold"),bg="yellow")
school_name.place(x=20,y=20,height=60,width=550)
#-------------------------------------------------------------------------------------------------------------------------------------------#
# Name Entry
st_name = Label(win,text="Student Name",font=("Times New Roman",20,"bold"),bg="yellow")
st_name.place(x=10,y=100,height=40,width=200)

st_name_1 = StringVar()
st_name_Entry = Entry(win,font=("Times New Roman",20,"bold"),textvariable=st_name_1)
st_name_Entry.place(x=230,y=100,height=40,width=300)
#-------------------------------------------------------------------------------------------------------------------------------------------#
# subject name
subject_name = Label(win,text="Subject Number",font=("Times New Roman",33,"bold"),bg="yellow")
subject_name.place(x=129,y=160,height=45,width=300)
#-------------------------------------------------------------------------------------------------------------------------------------------#
# variable declare

hindi_name_1 = DoubleVar()
english_name_1 = DoubleVar()
math_name_1 = DoubleVar()
science_name_1 = DoubleVar()
sst_name_1 = DoubleVar()

#-------------------------------------------------------------------------------------------------------------------------------------------#
# Subject no. 

hindi_name = Label(win,text="Hindi",font=("Times New Roman",20,"bold"),bg="yellow")
hindi_name.place(x=10,y=220,height=40,width=200)

hindi_name_Entry = Entry(win,font=("Times New Roman",20,"bold"),textvariable=hindi_name_1)
hindi_name_Entry.place(x=200,y=220,height=40,width=300)
#-------------------------------------------------------------------------------------------------------------------------------------------#

english_name = Label(win,text="English",font=("Times New Roman",20,"bold"),bg="yellow")
english_name.place(x=10,y=280,height=40,width=200)

english_name_Entry = Entry(win,font=("Times New Roman",20,"bold"),textvariable=english_name_1)
english_name_Entry.place(x=200,y=290,height=40,width=300)
#-------------------------------------------------------------------------------------------------------------------------------------------#

math_name = Label(win,text="Math",font=("Times New Roman",20,"bold"),bg="yellow")
math_name.place(x=10,y=340,height=40,width=200)

math_name_Entry = Entry(win,font=("Times New Roman",20,"bold"), textvariable=math_name_1)
math_name_Entry.place(x=200,y=350,height=40,width=300)
#-------------------------------------------------------------------------------------------------------------------------------------------#

science_name = Label(win,text="Science",font=("Times New Roman",20,"bold"),bg="yellow")
science_name.place(x=10,y=410,height=40,width=200)
science_name_Entry = Entry(win,font=("Times New Roman",20,"bold"), textvariable=science_name_1)
science_name_Entry.place(x=200,y=410,height=40,width=300)
#-------------------------------------------------------------------------------------------------------------------------------------------#

sst_name = Label(win,text="SST",font=("Times New Roman",20,"bold"),bg="yellow")
sst_name.place(x=10,y=480,height=40,width=200)

sst_name_Entry = Entry(win,font=("Times New Roman",20,"bold"), textvariable=sst_name_1)
sst_name_Entry.place(x=200,y=480,height=40,width=300)
#-------------------------------------------------------------------------------------------------------------------------------------------#
# Button

button = Button(win,text="Done",font=("Times New Roman",20,"bold"),command=get_data)
button.place(x=200,y=550,height=60,width=200)

win.mainloop() 