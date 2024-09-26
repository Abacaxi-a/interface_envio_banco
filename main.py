import customtkinter
import pandas as pd
import logging
from pathlib import Path
from modulos.interface import interface


BASE_DIR = Path(__file__).resolve().parent
LOGGING_FILE = BASE_DIR / 'logging.log'


class AplicativoEnvioBanco:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.title("ENVIAR PARA BANCO V1")
        interface(self.app)
        
    def executar(self):
        self.app.mainloop()

if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",level=logging.INFO, filename= LOGGING_FILE, encoding='utf-8')

    logging.info('>>>>> INICIADO SCRIPT')
    app = AplicativoEnvioBanco()
    app.executar()
    logging.info('FINALIZADO SCRIPT <<<<<')
