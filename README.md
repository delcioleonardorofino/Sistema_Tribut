
# Sistema de Gestão de Clientes

Este é um sistema simples de gestão de clientes, desenvolvido com **Python**, **Tkinter** para a interface gráfica, e **SQLAlchemy** para a interação com o banco de dados. O objetivo deste sistema é armazenar e gerenciar informações sobre os clientes, como nome, número de telefone, plano, consumo e saldo.

## Funcionalidades

- Cadastro de novos clientes.
- Exibição de uma lista de clientes cadastrados.
- Edição de informações de clientes existentes.
- Exclusão de clientes.
- Armazenamento em banco de dados SQLite.
- Interface gráfica intuitiva e fácil de usar.

## Tecnologias

- **Python 3.x**
- **Tkinter** - Interface gráfica.
- **SQLAlchemy** - ORM para interação com o banco de dados SQLite.
- **SQLite** - Banco de dados.

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado no seu ambiente de desenvolvimento:

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

Além disso, instale as dependências necessárias com o seguinte comando:

```bash
pip install -r requirements.txt
```

## Como rodar o projeto

### Passo 1: Clone o repositório

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/sist-trib.git
cd sist-trib
```

### Passo 2: Criação do banco de dados

O banco de dados será automaticamente criado na primeira execução do sistema. Caso queira criar o banco manualmente, execute:

```bash
python db/create_db.py
```

### Passo 3: Executar o aplicativo

Agora, execute o arquivo `main.py` para rodar o sistema:

```bash
python main.py
```

A interface gráfica será aberta, e você poderá interagir com o sistema.

## Estrutura do projeto

A estrutura do projeto é a seguinte:


/Sist_trib
├── /main.py               # Código principal que inicia o aplicativo
├── /db/                   # Arquivos relacionados ao banco de dados
│   └── create_db.py       # Criação do banco de dados
├── /models/               # Modelos de dados do SQLAlchemy
│   └── client_model.py    # Modelo do cliente
├── /cdr_utils/            # Utilitários para manipulação de dados CDR
│   └── utils.py           # Funções utilitárias para manipulação de CDR
├── /gui/                  # Código responsável pela interface gráfica
│   └── app_ui.py          # Interface com Tkinter
├── /services/             # Serviços auxiliares como lógica de negócios
│   └── client_service.py  # Lógica para gerenciar os clientes
├── .env                   # Arquivo de configuração do ambiente
├── requirements.txt       # Dependências do projeto
├── README.md              # Este arquivo
└── /venv/                 # Ambiente virtual


## Contribuindo

Se você deseja contribuir para este projeto, fique à vontade para enviar um **pull request** com melhorias, correções ou novas funcionalidades.

### Passos para contribuir:

1. Fork o repositório.
2. Crie uma branch para a sua modificação (`git checkout -b nova-funcionalidade`).
3. Faça as alterações e commit (`git commit -am 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin nova-funcionalidade`).
5. Envie o **pull request**.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

