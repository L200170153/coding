from Tkinter import *

aq = Tk(className='Bank')


a = Label(aq, text='Deposito or Withdrawal')
a.grid(row=0,column=0,sticky=W,pady=10,padx=10)
dw = StringVar()
aa = Entry(aq, textvariable=dw)
aa.grid(row=0,column=1,sticky=W,padx=10)

saldo = 0

def ddww():
    saldo = 0
    DW = dw.get()
    DW = [x for x in DW.split(' ')]
    if DW[0].lower()=='d':
        saldo+=int(DW[1])
        h.config(text=saldo)
    elif DW[0].lower()=='w':
        if int(DW[1])<=saldo:
            saldo-=int(DW[1])
            h.config(text=saldo)
        else:
            h.config(text='Saldo Anda kurang')
    else:
        h.config(text='Invalid Input')


b = Button(aq, text='cek', command=ddww, width=10)
b.grid(row=1,column=1,sticky=W)
c = Label(aq, text='Saldo sekarang')
c.grid(row=2,column=0,sticky=W)
h = Label(aq, text=0)
h.grid(row=2,column=1,sticky=W)
a.mainloop()
