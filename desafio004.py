from tkinter import *

def converter():
    if ety1.get().replace('.', '',1).isdigit():
        r = float(ety1.get()) * 1.8 + 32
        lb2['text'] = f'{r:.2f}'
        lb2['foreground'] = 'Green'
    else:
        lb2['text'] = 'Caracter Inválido!'
        lb2['foreground'] = 'Red'

janela = Tk()
janela.bind('<Return>', lambda event:converter())
janela.config(bg='black')

fr1 = Frame(janela, bg='black')
fr2 = Frame(janela, bg='black')


lb1 = Label(fr1, text='C°', font='Arial 22', foreground='Yellow', bg='black')
lb2 = Label(fr2, text='Resultado em F°', font='Arial 22', foreground='yellow', bg='black')
ety1 = Entry(fr1, font='arial 22')
bt1 = Button(fr2, text='Converter', font='arial 22', command=converter, foreground='yellow', bg='black')


fr1.pack()
fr2.pack()
lb1.grid(row=0, column=0)
lb2.grid(row=1, column=1)
ety1.grid(row=0, column=1)
bt1.grid(row=1, column=0, sticky=EW)


janela.mainloop()