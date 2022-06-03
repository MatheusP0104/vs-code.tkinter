from tkinter import *


def aumentar():
    if int(label1['text']) < 10:
        label1['text'] = int(label1['text']) + 1

def diminuir():
    if int(label1['text']) > -10:
        label1['text'] = int(label1['text']) - 1

janela = Tk()
janela.grid_rowconfigure(0, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.bind('-', lambda event: diminuir())
janela.bind('+', lambda event: aumentar())


bt1 = Button(janela, text='+', font='arial 22', command=aumentar)
label1 = Label(janela, text='0', font='arial 22')
bt2 = Button(janela, text='-', font='arial 22', command=diminuir)

bt1.grid(row=0, column=0, sticky=NSEW)
label1.grid(row=0, column=1, sticky=NSEW)
bt2.grid(row=0, column=2, sticky=NSEW)



janela.mainloop()