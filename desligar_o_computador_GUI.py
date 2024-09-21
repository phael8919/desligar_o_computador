import pyautogui as auto
from tkinter import *
from tkinter import messagebox

tela = Tk()
tela.geometry('510x300')
tela.title('Agendar para desligar o PC')

def desligar(escolha):    
    auto.sleep(2)
    auto.hotkey('win','r')
    
    auto.sleep(2)
    auto.typewrite('cmd')
    
    auto.sleep(2)
    auto.press('enter')
    
    auto.sleep(4)
    auto.typewrite(f'shutdown -s -f -t {escolha}')
    
    auto.sleep(2)
    auto.press('enter')
    
def btn1():
    return desligar(60)

def btn2():
    return desligar(60*5)

def btn3():
    return desligar(60*10)

def btn4():
    return desligar(60*15)

def btn5():
    return desligar(60*30)

def btn6():
    return desligar(60*60)

def btn7():
    return desligar(60*120)

def btn8():
    return desligar(60*180)

def btn9():
    tela.destroy()    
    


rotulo = Label(tela, text="Clique em uma das opções desejadas:", font='Arial 20')
rotulo.grid(row=1,column=1, pady=20, padx=15, columnspan=3)

botao1 = Button(tela, text='01 Min.', font='Arial 15', command=btn1)
botao1.grid(row=2,column=1, pady=10, padx=10)

botao2 = Button(tela, text='05 Min.', font='Arial 15', command=btn2)
botao2.grid(row=2,column=2, pady=10, padx=10)

botao3 = Button(tela, text='10 Min.', font='Arial 15', command=btn3)
botao3.grid(row=2,column=3, pady=10, padx=10)

botao4 = Button(tela, text='15 Min.', font='Arial 15', command=btn4)
botao4.grid(row=3,column=1, pady=10, padx=10)

botao5 = Button(tela, text='30 Min.', font='Arial 15', command=btn5)
botao5.grid(row=3,column=2, pady=10, padx=10)

botao6 = Button(tela, text='01 Hor.', font='Arial 15', command=btn6)
botao6.grid(row=3,column=3, pady=10, padx=10)

botao7 = Button(tela, text='02 Hor.', font='Arial 15', command=btn7)
botao7.grid(row=4,column=1, pady=10, padx=10)

botao8 = Button(tela, text='03 Hor.', font='Arial 15', command=btn8)
botao8.grid(row=4,column=2, pady=10, padx=10)

botao9 = Button(tela, text='  Sair.  ', font='Arial 15', command=btn9, fg='red')
botao9.grid(row=4,column=3, pady=10, padx=10)
            

tela.mainloop()
