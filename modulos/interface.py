import customtkinter 
from modulos.validacao import validar_doc
import os
from pathlib import Path

def criar_label_e_entrada(app, linha, coluna, texto_label, placeholder=""):
        label = customtkinter.CTkLabel(app, text=texto_label)
        label.grid(row=linha, column=coluna, padx=10, pady=5)
        entrada = customtkinter.CTkEntry(app, placeholder_text=placeholder)
        entrada.grid(row=linha+1, column=coluna, padx=10, pady=5)
        return entrada

def interface(app):
    # Entrada de caminho do arquivo
    caminho_doc_var = customtkinter.StringVar()
    caminho_doc_var.trace_add("write", lambda *args: validacao_input_caminho(caminho_doc_var,erro,frame))
    caminho_doc = criar_label_e_entrada(app, 0, 0, "Insira o caminho do CSV ou Excel:", "C://...")
    caminho_doc.configure(textvariable=caminho_doc_var)
    erro = customtkinter.CTkLabel(app, text='erro')
    frame = customtkinter.CTkFrame(app)

def validacao_input_caminho(doc,erro,frame):
    if not len(doc.get()) < 9 and (doc.get().endswith('.xlsx') or doc.get().endswith('.csv')):
        #esconde a mensagem de erro
        erro.grid_forget()

        #cria um container do para o banco
        frame.grid(row=3, column=0, padx=10, pady=10)
        frame_banco(doc,frame,erro)
        
    else:
        #mostra mensagem erro novamente
        erro.grid(row=2, column=0, padx=10, pady=10)
        frame.after(1000,lambda:erro.grid_forget())
        #esconde o container do banco
        frame.grid_forget()
 
def frame_banco(doc,frame,erro):
    #Exibição dos tipos de colunas
    tipo_colunas = customtkinter.CTkLabel(frame, text='')
    tipo_colunas.grid(row=2, column=0, padx=10, pady=10)

    # Entradas de conexão com o banco de dados
    usuario = criar_label_e_entrada(frame,3, 0, "Insira o usuário do banco:", "user")
    senha = criar_label_e_entrada(frame,3, 1, "Insira a senha do banco:", "password")
    server = criar_label_e_entrada(frame,5, 0, "Insira o host/servidor do banco:", "host")
    porta = criar_label_e_entrada(frame,5, 1, "Insira a porta do banco:", "port")
    database = criar_label_e_entrada(frame,7, 0, "Insira o nome do banco de dados:", "database")

    # Seleção do tipo de banco de dados
    label_tipo_db = customtkinter.CTkLabel(frame, text='Insira o tipo do banco:')
    label_tipo_db.grid(row=7, column=1, padx=10)
    tipo_db = customtkinter.CTkOptionMenu(frame, values=['PostgreSQL', 'MariaDB','MySql'])
    tipo_db.grid(row=8, column=1, padx=10, pady=10)
    conection = {
            'usuario':usuario,
            'senha':senha,
            'server':server,
            'porta':porta,
            'database':database,
            'tipo': tipo_db
    }

    # Botão para conectar e enviar
    conecta_envia = customtkinter.CTkButton(frame, text="Conectar e enviar ao banco", command=lambda: validar_doc(frame,doc,tipo_colunas,conection,erro))
    conecta_envia.grid(row=9, column=0, padx=10, pady=10)