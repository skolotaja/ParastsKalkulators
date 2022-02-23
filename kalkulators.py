from tkinter import*
import math
mansLogs=Tk()
mansLogs.title("kalkulators")
#================================================================================
def btnClick(number):
    current=e.get()
    e.delete(0,END)
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)
    return 0
 #======================================================================
def btnCommand(command):
    global number
    global num1 #jāiegaumē skaitlis, darbība
    global mathOp
    mathOp=command
    num1=int(e.get())
    e.delete(0,END)
    return 0
#==========================================================================
def Equals():
    num2=int(e.get())
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0
#======================================================================
def Clear():
    e.delete(0,END)
    num1=0
    mathOp=""
    return 0





e=Entry(mansLogs,width=15,font=("Arial Black",20),justify="right")
btn0=Button(mansLogs,text="0",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick(0))
btn1=Button(mansLogs,text="1",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick(1))
btn2=Button(mansLogs,text="2",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick(2))
btn3=Button(mansLogs,text="3",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick(3))
btn4=Button(mansLogs,text="4",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick(4))
btn5=Button(mansLogs,text="5",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick(5))
btn6=Button(mansLogs,text="6",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick(6))
btn7=Button(mansLogs,text="7",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick(7))
btn8=Button(mansLogs,text="8",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick(8))
btn9=Button(mansLogs,text="9",padx="40",font=('arial',12,'bold'),bd=3,bg='powderblue',pady="20",command=lambda:btnClick(9))
btnAdd=Button(mansLogs,text="+",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick('+'))
btnSub=Button(mansLogs,text="-",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick('-'))
btnReiz=Button(mansLogs,text="*",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick('*'))
btnDal=Button(mansLogs,text="/",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick('/'))
btnEquals=Button(mansLogs,text="=",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=Equals)
btnClear=Button(mansLogs,text="C",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=Clear)
btnx2=Button(mansLogs,text="^2",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick('^2'))
btnProc=Button(mansLogs,text="%",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick('%'))
btnKvs=Button(mansLogs,text="S",font=('arial',12,'bold'),bd=3,bg='powderblue',padx="40",pady="20",command=lambda:btnClick('S'))
e.grid(row=0,column=0,columnspan=4)

btnx2.grid(row=1,column=0)
btnProc.grid(row=1,column=1)
btnKvs.grid(row=1,column=2)



btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
btnAdd.grid(row=2,column=3)

btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
btnSub.grid(row=3,column=3)

btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)
btnReiz.grid(row=4,column=3)

btn0.grid(row=5,column=0)
btnClear.grid(row=5,column=1)
btnEquals.grid(row=5,column=2)
btnDal.grid(row=5,column=3)








mansLogs.mainloop()