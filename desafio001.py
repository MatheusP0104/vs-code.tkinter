from tkinter import *

# Back-end
def somatoria():
    if entry1.get().isnumeric() and entry2.get().isnumeric():
        label3['text'] = '=', float(entry1.get()) + float(entry2.get())
        label3['foreground'] = 'yellow'
    else:
        label3['text'] = 'Valores do tipo String/Nulo não é permitido!'
        label3['foreground'] = 'Red'



# criar a janela
janela = Tk()
janela.geometry('600x600+600+200')
janela.minsize(width=1000, height=400)
janela.maxsize(width=2000, height=2000)
janela.config(bg='black')

# criar os widgets
label1 = Label(janela, text='Calculadora Apenas Soma', font='arial 36 bold', bg='black', foreground='yellow')
entry1 = Entry(janela, font='Arial 36')
label2 = Label(janela, text='+', font='Arial 36 bold', foreground='yellow', bg='black')
entry2 = Entry(janela, font='arial 36')
label3 = Label(janela, text='', font='arial 36', bg='black', foreground='yellow')
btn1 = Button(janela, text='Soma', font='Arial 22', command=somatoria, bg='black', foreground='Yellow')

# organizar os widgets
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
btn1.pack()
label3.pack()


# executar a janela
janela.mainloop()
