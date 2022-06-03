from tkinter import *

def clicar(valor):
    if lb['text'] == 'Conta Inválida':
        lb['text'] = ''
        lb['text'] += valor
        lb['foreground'] = 'Black'
    else:
        lb['text'] += valor
        lb['foreground'] = 'Black'
        

def calcular():

    try:
        resultado = eval(lb['text'])
        lb['text'] = str(resultado)
        lb['foreground'] = 'Green'
    except ZeroDivisionError:
        lb['text'] = 'Conta Inválida'
        lb['foreground'] = 'Red'    
    except SyntaxError:
        lb['text'] = 'Conta Inválida'
        lb['foreground'] = 'Red'
    except TypeError:
        lb['text'] = 'Conta Inválida'
        lb['foreground'] = 'Red'
    


      
def apagar():
    lb['text'] = ''
    lb['foreground'] = 'Black'

def apagar_um():
    lb['text'] = lb['text'] [:-1] 
  

janela = Tk()
janela.title('Calculadora')
janela.geometry('320x500')
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=1)
janela.grid_rowconfigure(3, weight=1)
janela.grid_rowconfigure(4, weight=1)
janela.grid_rowconfigure(5, weight=1)
janela.resizable(False, False)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_columnconfigure(3, weight=1)

janela.bind('0', lambda event:clicar(valor='0'))
janela.bind('1', lambda event:clicar(valor='1'))
janela.bind('2', lambda event:clicar(valor='2'))
janela.bind('3', lambda event:clicar(valor='3'))
janela.bind('4', lambda event:clicar(valor='4'))
janela.bind('5', lambda event:clicar(valor='5'))
janela.bind('6', lambda event:clicar(valor='6'))
janela.bind('7', lambda event:clicar(valor='7'))
janela.bind('8', lambda event:clicar(valor='8'))
janela.bind('9', lambda event:clicar(valor='9'))
janela.bind('+', lambda event:clicar(valor='+'))
janela.bind('-', lambda event:clicar(valor='-'))
janela.bind('*', lambda event:clicar(valor='*'))
janela.bind('/', lambda event:clicar(valor='/'))
janela.bind('<Return>', lambda event:calcular())
janela.bind('(', lambda event:clicar(valor='('))
janela.bind(')', lambda event:clicar(valor=')'))
janela.bind('.', lambda event:clicar(valor='.'))
janela.bind('<Escape>', lambda event:apagar())
janela.bind('<BackSpace>', lambda event:apagar_um())

lb = Label(janela, bg='#495057', text='', font='Arial 26', foreground='Black')
bt1 = Button(janela, text='1',bg='white', font='36', command=lambda: clicar('1'))
bt2 = Button(janela, text='2',bg='white', font='36', command=lambda: clicar('2'))
bt3 = Button(janela, text='3',bg='white', font='36', command=lambda: clicar('3'))
bt4 = Button(janela, text='4',bg='white', font='36', command=lambda: clicar('4'))
bt5 = Button(janela, text='5',bg='white', font='36', command=lambda: clicar('5'))
bt6 = Button(janela, text='6',bg='white', font='36', command=lambda: clicar('6'))
bt7 = Button(janela, text='7',bg='white', font='36', command=lambda: clicar('7'))
bt8 = Button(janela, text='8',bg='white', font='36', command=lambda: clicar('8'))
bt9 = Button(janela, text='9',bg='white', font='36', command=lambda: clicar('9'))
bt0 = Button(janela, text='0',bg='white', font='36', command=lambda: clicar('0'))
bt_apagar = Button(janela, text='CE', font='40', bg='white', command=lambda:apagar())
bt_somar = Button(janela, text='+',bg='white', font='40', command=lambda: clicar('+'))
bt_subtrair = Button(janela, text='-', bg='white', font='40', command=lambda:clicar('-'))
bt_mult = Button(janela, text='*', bg='white',font='40', command=lambda:clicar('*'))
bt_div = Button(janela, text='/',bg='white', font='40', command=lambda:clicar('/'))
bt_igual = Button(janela,text='=', bg='#6c757d', foreground='Black', font='40', command=lambda: calcular())
bt_ponto = Button(janela, text='.',bg='white', font='40', command=lambda:clicar('.'))
bt_del = Button(janela, text='Del', bg='white', font='40', command=lambda:apagar_um())
bt_pd = Button(janela, text='(', bg='white', font='40', command=lambda:clicar('('))
bt_pe = Button(janela, text=')', bg='white', font='40', command=lambda:clicar(')'))


lb.grid(columnspan=4,sticky=NSEW)
bt9.grid(row=1, column=2, sticky=NSEW)
bt8.grid(row=1, column=1,sticky=NSEW)
bt7.grid(row=1, column=0,sticky=NSEW)
bt_mult.grid(row=1, column=3,sticky=NSEW)
bt4.grid(row=2, column=0,sticky=NSEW)
bt5.grid(row=2, column=1,sticky=NSEW)
bt6.grid(row=2, column=2,sticky=NSEW)
bt_somar.grid(row=2, column=3,sticky=NSEW)
bt1.grid(row=3, column=0,sticky=NSEW)
bt2.grid(row=3, column=1,sticky=NSEW)
bt3.grid(row=3, column=2,sticky=NSEW)
bt_subtrair.grid(row=3, column=3,sticky=NSEW)
bt0.grid(row=4, column=1,sticky=NSEW)
bt_igual.grid(row=4, column=2, sticky=NSEW)
bt_ponto.grid(row=4, column=0,sticky=NSEW)
bt_div.grid(row=4, column=3,sticky=NSEW)
bt_apagar.grid(row=5, column=1, sticky=NSEW)
bt_del.grid(row=5, column=0, sticky=NSEW)
bt_pd.grid(row=5, column=2, sticky=NSEW)
bt_pe.grid(row=5, column=3, sticky=NSEW)

janela.mainloop()