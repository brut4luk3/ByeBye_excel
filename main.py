from csv import *
from pathlib import Path
from tkinter import *
import tkinter as tk

main = tk.Tk()
main.title('Bye Bye Excel')
main.geometry("900x550")
lista_principal = []

#FUNÇÕES
def CreateAndAdd():
    lista = []

    if bool(lista):
        pass
    else:
        frame_visualizacao.delete(1.0, END)

    #CRIA A SINTAXE JSON
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
    #CRIA A SINTAXE JSON - FIM

    #SALVA O DOCUMENTO
    with open('data_entry.csv', 'w', newline='') as file:
        Writer = writer(file)
        Writer.writerows(lista_principal)

        file.close()
    #SALVA O DOCUMENTO - FIM

    #VERIFICA SE EXISTE ARQUIVO
    caminho = Path('./data_entry.csv')
    verifica_arquivo = caminho.is_file()
    #VERIFICA SE EXISTE ARQUIVO - FIM

    #EXIBE O ARQUIVO CRIADO (SE EXISTIR)
    if verifica_arquivo == True:
        visualizar_doc = open("data_entry.csv", 'r')
        acao_visualizar_doc = visualizar_doc.read()
        frame_visualizacao.insert(END, acao_visualizar_doc)

        visualizar_doc.close()
    elif verifica_arquivo != True:
        pass
    #EXIBE O ARQUIVO CRIADO (SE EXISTIR) - FIM

    #LIMPA OS CAMPOS ENTRY
    caixa_entrada.delete(0, END)
    caixa_saida.delete(0, END)
    #LIMPA OS CAMPOS ENTRY - FIM

#Função ClearLast será comentada por hora, com bugs, não funcional.
#def ClearLast():
    #VERIFICA SE EXISTE ARQUIVO
    #caminho_clearLast = Path('./data_entry.csv')
    #verifica_arquivo_clearLast = caminho_clearLast.is_file()
    #VERIFICA SE EXISTE ARQUIVO - FIM

    #APAGA A ÚLTIMA LINHA
    #if verifica_arquivo_clearLast == True:
        #linhas = open("data_entry.csv", 'r+')
        #acao_linhas = linhas.readlines()
        #linhas.seek(0)
        #linhas.truncate()
        #linhas.writelines(acao_linhas[:-1])

        #frame_visualizacao.delete(1.0, END)

        #linhas.close()

        #nova_leitura = open("data_entry.csv", 'r')
        #acao_nova_leitura = nova_leitura.read()
        #frame_visualizacao.insert(END, acao_nova_leitura)

        #nova_leitura.close()

    #elif verifica_arquivo_clearLast != True:
        #pass
    #APAGA A ÚLTIMA LINHA - FIM
#FUNÇÕES - FIM

#ÁREA DA LOGO
logo = PhotoImage(file='./byebye_excel_sem_fundo1.png')
image_label = tk.Label(image=logo)
image_label.place(x=50, y=20)
#ÁREA DA LOGO - FIM

#ÁREA DA VISUALIZAÇÃO DE DADOS NA PLANILHA
texto_visualizacao_label = tk.Label(text='Visualize as linhas adicionadas na planilha:', font=("Arial", 15), pady=10)
texto_visualizacao_label.place(x=500, y=20)

comentario_texto_visualizacao_label = tk.Label(text='Importante: os dados abaixo são apenas ilustrativos!', font=("Arial", 8), pady=1)
comentario_texto_visualizacao_label.place(x=500, y=55)

frame_visualizacao = Text(main, width=45, height=28)
frame_visualizacao.place(x=500, y=75)
#ÁREA DA VISUALIZAÇÃO DE DADOS NA PLANILHA - FIM

#ÁREA DO TEXTO DE ENTRADA
texto_entrada = 'Digite o dado de entrada da planilha:'
texto_entrada_label = tk.Label(text=texto_entrada, font=(35), pady=10)
texto_entrada_label.place(x=50, y=250)
#ÁREA DO TEXTO DE ENTRADA - FIM

#INPUT DE ENTRADA
caixa_entrada = tk.Entry(width=50, borderwidth=5)
caixa_entrada.place(x=50, y=290)
#INPUT DE ENTRADA - FIM

#ÁREA DO TEXTO DE SAÍDA
texto_saida = 'Digite o dado de saída da planilha:'
texto_saida_label = tk.Label(text=texto_saida, font=(35), pady=10)
texto_saida_label.place(x=50, y=330)
#ÁREA DO TEXTO DE SAÍDA - FIM

#INPUT DE SAÍDA
caixa_saida = tk.Entry(width=50, borderwidth=5)
caixa_saida.place(x=50, y=370)
#INPUT DE SAÍDA - FIM

#BOTÕES
CreateAndAdd = Button(main,text='Adicionar nova linha',padx=20,pady=10,command=CreateAndAdd)
#clearLast = Button(main,text='Apagar última linha',padx=18,pady=10,command=ClearLast)

CreateAndAdd.place(x=100, y=450, width=200)
#clearLast.place(x=100, y=460, width=200)
#BOTÕES - FIM

main.mainloop()