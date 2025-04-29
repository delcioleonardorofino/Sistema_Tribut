import tkinter as tk
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base
from gui import construir_interface
from models import Cliente, CDR  

# # Função para inicializar o banco de dados
# def inicializar_banco():
#     # Criação da engine do banco de dados
#     engine = create_engine('sqlite:///clientes.db')  
#     # Criando todas as tabelas
#     Base.metadata.create_all(engine)
    
#     # Criar sessão
#     Session = sessionmaker(bind=engine)
#     sessao = Session()
    
#     if engine.dialect.has_table(engine, "clientes"):
#         print("Tabela 'clientes' foi criada com sucesso!")
#     else:
#         print("Erro ao criar a tabela 'clientes'.")

#     return sessao

def main():
    # Inicializar o banco de dados
    # sessao = inicializar_banco()

    # Criar a janela principal
    root = tk.Tk()
    sessao = None
    # Passar a sessão de banco de dados para a interface gráfica
    construir_interface(root, sessao)

    # Iniciar a interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()
