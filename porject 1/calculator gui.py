import math
from tkinter import*

root=Tk()
#title barname
root.title("simple calculator ")
#tolid box
e=Entry(root,width=45,borderwidth=8)
e.grid(row=0,column=0,pady=9,padx=9,columnspan=4) #vorod migire v boxx o  dorost mikone
def button_click(number):
   
    current=e.get() 
    
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_num=e.get()
    global f_num
    global math
    math='addition'
    f_num=int(first_num)
    e.delete(0,END)

def button_eq():
    sec_nm=e.get()
    e.delete(0,END)
    if math=='addittion':
        e.insert(0,f_num+ int(sec_nm))
    elif math=='sub':
        e.insert(0,f_num -int(sec_nm))
    elif math=='multi':
        e.insert(0,f_num *int(sec_nm))
    else:
        e.insert(0,f_num/int(sec_nm))

def button_sub():
    first_num=e.get()
    global f_num
    global math
    math='sub'
    f_num=int(first_num)
    e.delete(0,END)

def button_multi():
    first_num=e.get()
    global f_num
    global math
    math='multi'
    f_num=int(first_num)
    e.delete(0,END)

def button_divid():
    first_num=e.get()
    global f_num
    global math
    math='divid'
    f_num=int(first_num)
    e.delete(0,END)



    #dif butt

button_1= Button(root,text='1',pady=40,padx=60,command=lambda: button_click(1))
button_2= Button(root,text='2',pady=40,padx=60,command=lambda: button_click(2))
button_3= Button(root,text='3',pady=40,padx=60,command=lambda: button_click(3))
button_4= Button(root,text='4',pady=40,padx=60,command=lambda: button_click(4))
button_5= Button(root,text='5',pady=40,padx=60,command=lambda: button_click(5))
button_6= Button(root,text='6',pady=40,padx=60,command=lambda: button_click(6))
button_7= Button(root,text='7',pady=40,padx=60,command=lambda: button_click(7))
button_8= Button(root,text='8',pady=40,padx=60,command=lambda: button_click(8))
button_9= Button(root,text='9',pady=40,padx=60,command=lambda: button_click(9))
button_0= Button(root,text='0',pady=40,padx=60,command=lambda: button_click(0))
button_ad= Button(root,text='+',pady=40,padx=60,command= button_add,bg='gray')
button_eq= Button(root,text='=',pady=40,padx=60,command=button_eq,bg='green')
button_cl= Button(root,text='clear',pady=40,padx=188,command=button_clear,bg='red')
button_sub= Button(root,text='-',pady=40,padx=60,command= button_sub,bg='gray')
button_multi= Button(root,text='*',pady=40,padx=60,command=button_multi,bg='gray')
button_divid= Button(root,text='/',pady=40,padx=60,command=button_divid,bg='gray')

#qarar dand add rooy screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0,)
button_ad.grid(row=4,column=1)
button_eq.grid(row=4,column=2)
button_sub.grid(row=5,column=0)
button_multi.grid(row=5,column=1)
button_divid.grid(row=5,column=2)



button_cl.grid(row=6,column=0,columnspan=4)
bottn=Button(root,text='enter num ')



button_1.pack






root.mainloop()