import logging
from pathlib import Path
import pandas as pd
from modulos.envio_db import conexao_envio_doc
import csv
import chardet
import customtkinter

def delimi_encode_doc(caminho,tamanho):
    with open(caminho, 'r') as file:
        arquivo = file.read(tamanho)
        sniffer = csv.Sniffer()
        delimitador = sniffer.sniff(arquivo).delimiter
        
    with open(caminho, 'rb') as file:
        dados = file.read()
        resultado = chardet.detect(dados)
        encoding = resultado['encoding']
    
    return delimitador,encoding
    
def validar_doc(frame,caminho,colunas,conexao,erro):
        caminho = caminho.get()
        caminho = Path(caminho)
        logging.info(f'Arquivo selecionado: {caminho}')
        if not caminho.is_file():
            #mostra mensagem de erro apaga após 1 seg
            erro.grid(row=2, column=0, padx=10, pady=10)
            frame.after(1000,lambda:erro.grid_forget())
            print(('O caminho fornecido não é um arquivo válido.'))
            logging.info('O caminho fornecido não é um arquivo válido.')
        else:    
            extensao = caminho.suffix.lower()
            if extensao == '.csv':
                delimitador,doc_encode = delimi_encode_doc(caminho,1024)
                df = pd.read_csv(caminho, delimiter=delimitador, encoding=doc_encode)
            elif extensao == '.xlsx':
                #delimitador,doc_encode = delimi_encode_doc(caminho,1024)

                arquivo = pd.ExcelFile(caminho)
                arquivo = arquivo.sheet_names
                planilha = customtkinter.CTkOptionMenu(frame, values=arquivo)
                planilha(row=9, column=2, padx=10, pady=10)

                df = pd.read_excel(caminho,sheet_name=planilha)
            else:
                print('Tipo de arquivo não suportado. Use arquivos CSV ou Excel.')
                logging.error('Tipo de arquivo não suportado. Use arquivos CSV ou Excel.')
                return
            colunas.configure(text=df.dtypes)
            conexao_envio_doc(df,conexao)


