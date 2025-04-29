import tkinter as tk
from tkinter import ttk, messagebox
from db import SessionLocal
from models import Cliente, CDR
from servicos import registrar_voz, registrar_sms, registrar_dados

# Conectar ao banco
db = SessionLocal()
clientes = db.query(Cliente).all()

# Inicializa a janela principal
root = tk.Tk()
root.title("Sistema de Tributação de Clientes")
root.geometry("650x550")

# --- Funções ---
def atualizar_lista_cdr(cliente_id):
    cdr_listbox.delete(0, tk.END)
    cdrs = db.query(CDR).filter(CDR.cliente_id == cliente_id).all()
    for cdr in cdrs:
        cdr_listbox.insert(tk.END, f"{cdr.tipo_servico} - {cdr.quantidade} - {cdr.custo:.2f}Mt")

def atualizar_cliente(event=None):
    nome_selecionado = cliente_combo.get()
    cliente = next((c for c in clientes if c.nome == nome_selecionado), None)
    if cliente:
        saldo_var.set(f"Saldo: {cliente.saldo:.2f}Mt")
        atualizar_lista_cdr(cliente.id)

def executar_acao(tipo):
    nome = cliente_combo.get()
    cliente = next((c for c in clientes if c.nome == nome), None)
    if not cliente:
        return

    if tipo == "voz":
        resposta = registrar_voz(cliente, "841234567", 2)
    elif tipo == "sms":
        resposta = registrar_sms(cliente, "841234567")
    elif tipo == "dados":
        resposta = registrar_dados(cliente, 5)
    else:
        resposta = "Ação inválida"
    
    db.commit()
    saldo_var.set(f"Saldo: {cliente.saldo:.2f}Mt")
    atualizar_lista_cdr(cliente.id)
    messagebox.showinfo("Info", resposta)

# --- GUI Widgets ---
tk.Label(root, text="Cliente:").pack(pady=5)
cliente_combo = ttk.Combobox(root, values=[c.nome for c in clientes])
cliente_combo.pack()
cliente_combo.bind("<<ComboboxSelected>>", atualizar_cliente)
cliente_combo.current(0)

saldo_var = tk.StringVar()
tk.Label(root, textvariable=saldo_var, font=("Arial", 12)).pack(pady=10)

frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)
tk.Button(frame_botoes, text="📞 Chamada", command=lambda: executar_acao("voz")).pack(side="left", padx=5)
tk.Button(frame_botoes, text="✉️ SMS", command=lambda: executar_acao("sms")).pack(side="left", padx=5)
tk.Button(frame_botoes, text="🌐 Dados", command=lambda: executar_acao("dados")).pack(side="left", padx=5)

tk.Label(root, text="Histórico de CDRs").pack(pady=10)
cdr_listbox = tk.Listbox(root, width=70)
cdr_listbox.pack()

# Inicializa com o primeiro cliente
atualizar_cliente()

# Inicia GUI
root.mainloop()
