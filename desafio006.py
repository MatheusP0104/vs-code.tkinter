from tkinter import *




janela = Tk()
janela.config(bg='white')


fr1 = Frame(janela,bg='white', highlightbackground='black', highlightthickness=2)
fr2 = Frame(janela, bg='white', highlightbackground='black', highlightthickness=2)
fr3 = Frame(janela, bg='white', highlightbackground='black', highlightthickness=2)

imagem = PhotoImage(file='logo riot_mod.png')
lb_imagem = Label(janela, image= imagem, bg='White')
lb1 = Label(fr1, text='Dados Pessoais', font='Arial 26 italic', bg='white', foreground='black', highlightbackground='#CD143C', highlightthickness=2)
lb2 = Label(fr1, text='Nome:', font='Arial 20', anchor=E, bg='White')
lb3 = Label(fr1, text='CPF:', font='Arial 20', anchor=E, bg='White')
lb4 = Label(fr1, text='Telefone:', font='Arial 20', anchor=E, bg='White')
lb5 = Label(fr1, text='Data Nasc:', font='Arial 20', anchor=E, bg='White')
lb6 = Label(fr2, text='Endereço', font='Arial 26 italic', anchor=E, bg='White', highlightbackground='#CD143C', highlightthickness=2)
lb7 = Label(fr2, text='Rua:', font='Arial 20', anchor=E, bg='White')
lb8 = Label(fr2, text='Bairro:', font='Arial 20', anchor=E, bg='White')
lb9 = Label(fr2, text='N°:', font='Arial 20', anchor=E, bg='White')
lb10 = Label(fr2, text='UF:', font='Arial 20', anchor=E, bg='White')
lb11 = Label(fr2, text='Cidade:', font='Arial 20', anchor=E, bg='White')
en1 = Entry(fr1, font='arial 20', highlightbackground='#8b008b', highlightthickness=2)
en2 = Entry(fr1, font='arial 20', highlightbackground='#8b008b', highlightthickness=2)
en3 = Entry(fr1, font='arial 20', highlightbackground='#8b008b', highlightthickness=2)
en4 = Entry(fr1, font='arial 20', highlightbackground='#8b008b', highlightthickness=2)
en5 = Entry(fr2, font='arial 20', highlightbackground='#8b008b', highlightthickness=2)
en6 = Entry(fr2, font='arial 20', highlightbackground='#8b008b', highlightthickness=2)
en7 = Entry(fr2, font='arial 20', highlightbackground='#8b008b', highlightthickness=2)
en8 = Entry(fr2, font='arial 20', highlightbackground='#8b008b', highlightthickness=2)
en9 = Entry(fr2, font='arial 20', highlightbackground='#8b008b', highlightthickness=2)
bt1 = Button(fr3, text='Gravar Dados', font='Arial 20', bg='white', anchor=W)
bt2 = Button(fr3, text='Listar Dados', font='arial 20', bg='White',anchor=W)


fr1.grid(row=1, column=0, sticky=EW)
fr2.grid(row=2, column=0)
fr3.grid(row=3, column=0)

lb_imagem.grid(row=0, column=0)
lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0, sticky=EW)
lb3.grid(row=2, column=0,sticky=EW)
lb4.grid(row=3, column=0, sticky=EW)
lb5.grid(row=4, column=0, sticky=EW)
lb6.grid(row=0, column=0, sticky=EW)
lb7.grid(row=1, column=0, sticky=EW)
lb8.grid(row=2, column=0, sticky=EW)
lb9.grid(row=1, column=2, sticky=EW)
lb10.grid(row=2, column=4, sticky=EW)
lb11.grid(row=2, column=2, sticky=EW)

en1.grid(row=1, column=1, sticky=EW)
en2.grid(row=2, column=1, sticky=EW)
en3.grid(row=3, column=1, sticky=EW)
en4.grid(row=4, column=1, sticky=EW)
en5.grid(row=1, column=1, sticky=EW)
en6.grid(row=1, column=3, sticky=EW)
en7.grid(row=2, column=1, sticky=EW)
en8.grid(row=2, column=3, sticky=EW)
en9.grid(row=2, column=5, sticky=EW)

bt1.grid(row=0,column=0, sticky=EW)
bt2.grid(row=0, column=1, sticky=EW)

janela.mainloop()