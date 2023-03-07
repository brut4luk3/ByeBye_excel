#import csv
from csv import *
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import json

main = tk.Tk()
main.title('Bye Bye Excel')
main.geometry("700x550")
lista_principal = []

#FUNÇÕES
def Add():
    chave_json = "retorno"
    dois_pontos = ":"
    chave_1 = "{"
    chave_2 = "}"
    aspas_1 = "'"
    aspas_2 = "'"
    aspas_3 = "'"
    aspas_4 = "'"
    entrada = caixa_entrada.get()
    saida = caixa_saida.get()

    saida_formatada = f'{chave_1}{aspas_1}{chave_json}{aspas_2}{dois_pontos} {aspas_3}{saida}{aspas_4}{chave_2}'

    lista = [entrada, saida_formatada]
    lista_principal.append(lista)
    messagebox.showinfo('Informação', 'Dados adicionados com sucesso!')

def Save():
    with open('data_entry.csv', 'w', newline='') as file:
        Writer = writer(file)
        Writer.writerows(lista_principal)
        messagebox.showinfo('Informação', 'Planilha salva com sucesso!')

def Clear():
    caixa_entrada.delete(0, END)
    caixa_saida.delete(0, END)
#FUNÇÕES - FIM

#ÁREA DA LOGO
logo = PhotoImage(file='./byebye_excel_sem_fundo1.png')
image_label = tk.Label(image=logo)
image_label.pack()
#ÁREA DA LOGO - FIM


#ÁREA DO TEXTO DE ENTRADA
texto_entrada = 'Digite o dado de entrada da planilha:'
texto_entrada_label = tk.Label(text=texto_entrada, font=(35), pady=10)
texto_entrada_label.pack()
#ÁREA DO TEXTO DE ENTRADA - FIM

#INPUT DE ENTRADA
caixa_entrada = tk.Entry(width=50, borderwidth=5)
caixa_entrada.pack()
#INPUT DE ENTRADA - FIM

#ÁREA DO TEXTO DE SAÍDA
texto_saida = 'Digite o retorno da planilha dentro das aspas:'
texto_saida_label = tk.Label(text=texto_saida, font=(35), pady=10)
texto_saida_label.pack()
#ÁREA DO TEXTO DE SAÍDA - FIM

#INPUT DE SAÍDA
caixa_saida = tk.Entry(width=50, borderwidth=5)
caixa_saida.pack()
#INPUT DE SAÍDA - FIM

#BOTÕES
save = Button(main,text='Salvar e finalizar',padx=20,pady=10,command=Save)
add = Button(main,text='Adicionar nova linha',padx=20,pady=10,command=Add)
clear = Button(main,text='Limpar',padx=18,pady=10,command=Clear)
Exit = Button(main,text='Sair',padx=20,pady=10,command=main.quit)

save.pack()
add.pack()
clear.pack()
Exit.pack()
#BOTÕES - FIM

main.mainloop()

print(lista_principal)
