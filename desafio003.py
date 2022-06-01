from tkinter import *

def calcular(event):
    if ety1.get().replace('.', '',1).isdigit() and ety2.get().replace('.','',1).isdigit():
        imc = float(ety1.get()) / (float(ety2.get()) * float(ety2.get()))
        lb3['text'] = f'{imc:,.2f}'
        lb3['foreground'] = 'Green'
    else:
        lb3['text'] = 'Por favor, Digite somente Números'
        lb3['foreground'] = 'red'

janela = Tk()
janela.bind('<Return>' ,calcular)

lb1 = Label(janela, text='Peso:', font='Arial 22')
lb2 = Label(janela, text='Altura:', font='Arial 22')
lb3 = Label(janela, text='Resultado', font='arial 22', foreground='black')
ety1 = Entry(janela, font='arial 22')
ety2 = Entry(janela, font='arial 22')
bt1 = Button(janela, text='IMC', font='arial 22', command=calcular)



lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
ety1.grid(row=0, column=1)
ety2.grid(row=1, column=1)
bt1.grid(row=2, column=1, sticky=EW)
lb3.grid(row=3, column=1)




janela.mainloop()