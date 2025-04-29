from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base, sessionmaker 
from dotenv import load_dotenv  # importa função para ler o arquivo .env
import os 

load_dotenv()  # carrega as variáveis do arquivo .env para o ambiente do sistema

DATABASE_URL = os.getenv("DATABASE_URL")  # lê a variável DATABASE_URL do .env

engine = create_engine(DATABASE_URL, echo=True)  

SessionLocal = sessionmaker(bind=engine) 

Base = declarative_base()  # classe base para declarar modelos (tabelas)

