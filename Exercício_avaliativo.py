from tkinter import *

SENAC = Tk()
SENAC.geometry('1000x600')
SENAC.config(bg='white')
SENAC.title('Cadastro')
Bg = PhotoImage(file='wallpaper.png')
Fundo = Label(SENAC, image= Bg, border=0)
Fundo.place(x=0, y=0)
Fra1= Frame(SENAC)

fr0 = Frame(SENAC)
fr1 = Frame(SENAC, bg='white')
fr2 = Frame(SENAC, bg='white')
fr3 = Frame(SENAC, bg='white')

Text_Cadastro = Label(fr0, text='CREATE YOUR ACCONT', font='Verdana 25', width=50)
lb1 = Label(fr1, text='Dados Pessoais', font='Verdana 15', anchor=W, bg='white', foreground='#4DDBEF')
Text_Nome = Label(fr1, text='Nome:', font='Verdana 15', bg='White', anchor=W)
lb3 = Label(fr1, text='CPF:', font='Verdana 15', anchor=W, bg='White')
lb4 = Label(fr1, text='Telefone:', font='Verdana 15', anchor=W, bg='White')
lb5 = Label(fr1, text='Data Nasc:', font='Verdana 15', anchor=W, bg='White')
lb_sexo = Label(fr1, text='Sexo:', font='Verdana 15', anchor=W, bg='White')
Check_Fame = Checkbutton(fr1, text='Feminino', bg='white', anchor=W, font='Verdana 15')
Check_Male = Checkbutton(fr1, text='Masculino', bg='white', anchor=W, font='Verdana 15')
lb6 = Label(fr2, text='Endereço', font='Verdana 15 italic', anchor=W, bg='white', height=2, foreground='#4DDBEF')
lb7 = Label(fr2, text='Rua:', font='Verdana 15', anchor=W, bg='White')
lb8 = Label(fr2, text='Bairro:', font='Verdana 15', anchor=W, bg='White')
lb9 = Label(fr2, text='N°:', font='Verdana 15', anchor=W, bg='White')
lb10 = Label(fr2, text='UF:', font='Verdana 15', anchor=W, bg='White')
lb11 = Label(fr2, text='Cidade:', font='Verdana 15', anchor=W, bg='White')
en1 = Entry(fr1, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en2 = Entry(fr1, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en3 = Entry(fr1, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en4 = Entry(fr1, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en5 = Entry(fr2, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en6 = Entry(fr2, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en7 = Entry(fr2, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en8 = Entry(fr2, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
en9 = Entry(fr2, font='arial 20', highlightbackground='#2B2B2B', highlightthickness=1)
bt1 = Button(fr3, text='CADASTRAR', font='Verdana 12', bg='#4DDBEF', width=23, borderwidth=10)


Butb= '#6BBC00'
Fon= 'Verdana 15'
EnLingu = Label(Fra1)
Log = Label(Fra1, text='Log in',font='Verdana 35 bold')
Mensa = Label(Fra1, text='Use an already created account',font=Fon)
Email = Label(Fra1, text='E-mail',font=Fon)
Pass = Label(Fra1, text='User',font=Fon)
Log_in = Button(Fra1, text= 'Log in',font='Verdana 20 bold', bg=Butb,command=lambda: [fr0.grid(row=0, column=0, sticky=NSEW, columnspan=2), 
fr1.grid(row=1, column=0, sticky=NSEW), fr2.grid(row=1, column=1, sticky=NSEW), fr3.grid(row=2, column=0, sticky=NSEW, columnspan=2), Fra1.destroy()])
Enty1 = Entry(Fra1, font=Fon)
Enty2 = Entry(Fra1, font=Fon)
Forgo = Label(Fra1, font='verdana 15 bold', text='Forgot your password?', fg=Butb)

Fra1.place(x=360, y=120)
Log.grid(row=0, column=0, sticky=NSEW, columnspan=1)
Mensa.grid(row=1, column=0, sticky=NSEW, columnspan=1)
Email.grid(row=2, column=0, sticky=NSEW) 
Enty1.grid(row=3, column=0, sticky=NSEW)
Pass.grid(row=4, column=0, sticky=NSEW)
Enty2.grid(row=5, column=0, sticky=NSEW)
Log_in.grid(row=7, column=0, sticky=NSEW, columnspan=1)
Forgo.grid(row=6, column=0, sticky=NSEW)

#fr0.grid(row=0, column=0, sticky=NSEW, columnspan=2)
#fr1.grid(row=1, column=0, sticky=NSEW)
#fr2.grid(row=1, column=1, sticky=NSEW)
#fr3.grid(row=2, column=0, sticky=NSEW, columnspan=2)


Text_Cadastro.grid(row=0, column=0)

lb1.grid(row=0, column=0)
Text_Nome.grid(row=1, column=0, sticky=EW)
lb3.grid(row=3, column=0,sticky=EW)
lb4.grid(row=5, column=0, sticky=EW)
lb5.grid(row=7, column=0, sticky=EW)
lb6.grid(row=0, column=0, sticky=EW)
lb7.grid(row=2, column=0, sticky=EW)
lb8.grid(row=4, column=0, sticky=EW)
lb9.grid(row=6, column=0, sticky=EW)
lb10.grid(row=8, column=0, sticky=EW)
lb11.grid(row=10, column=0, sticky=EW)
lb_sexo.grid(row=11, column=0, sticky=EW)
Check_Fame.grid(row=12, column=0, sticky=EW)
Check_Male.grid(row=12, column=1, sticky=EW)

en1.grid(row=2, column=0, sticky=EW)
en2.grid(row=4, column=0, sticky=EW)
en3.grid(row=6, column=0, sticky=EW)
en4.grid(row=8, column=0, sticky=EW)
en5.grid(row=3, column=0, sticky=EW)
en6.grid(row=5, column=0, sticky=EW)
en7.grid(row=7, column=0, sticky=EW)
en8.grid(row=9, column=0, sticky=EW)
en9.grid(row=11, column=0, sticky=EW)

bt1.grid(row=0,column=1)



SENAC.mainloop()