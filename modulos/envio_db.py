import logging
import sqlalchemy as db

def conexao_envio_doc(df,conexao):
        user = conexao['usuario,']
        pwd =  conexao['senha']
        host = conexao['server']
        port = conexao['porta']
        dbt =  conexao['database']
        tipo = conexao['tipo']

        logging.info(f'Banco selecionado:{tipo}')
        try:
            if tipo == 'PostgreSQL':
                engine = db.create_engine(f'postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{dbt}')
            else:
                engine = db.create_engine(f'mysql+pymysql://{user}:{pwd}@{host}:{port}/{dbt}')
            with engine.connect() as con:
                df.to_sql('teste', con, if_exists='replace', index=False)
                logging.info("Dados enviados para o banco com sucesso.")
        except Exception as err:
            logging.error(f"Erro ao enviar dados para o banco: {err}")