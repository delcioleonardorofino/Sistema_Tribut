from datetime import datetime
from models import CDR
from db import SessionLocal
from cdr_utils import calcular_duracao_em_minutos, calcular_custo

def registrar_voz(cliente, numero_destino, minutos):
    inicio = datetime.now()
    fim = inicio.replace(minute=inicio.minute + minutos)
    duracao = minutos
    custo = calcular_custo("voz", duracao)

    if cliente.plano == "pre" and cliente.saldo < custo:
        return "Saldo insuficiente."

    cdr = CDR(
        cliente_id=cliente.id,
        numero_chamado=numero_destino,
        inicio=inicio,
        fim=fim,
        duracao=duracao,
        tipo_servico="voz",
        quantidade=duracao,
        custo=custo
    )

    db = SessionLocal()
    db.add(cdr)
    if cliente.plano == "pre":
        cliente.saldo -= custo
    db.commit()
    db.close()
    return "Chamada registrada com sucesso."

def registrar_sms(cliente, numero_destino):
    custo = calcular_custo("sms", 1)

    if cliente.plano == "pre" and cliente.saldo < custo:
        return "Saldo insuficiente."

    agora = datetime.now()
    cdr = CDR(
        cliente_id=cliente.id,
        numero_chamado=numero_destino,
        inicio=agora,
        fim=agora,
        duracao=0,
        tipo_servico="sms",
        quantidade=1,
        custo=custo
    )

    db = SessionLocal()
    db.add(cdr)
    if cliente.plano == "pre":
        cliente.saldo -= custo
    db.commit()
    db.close()
    return "SMS enviado com sucesso."

def registrar_dados(cliente, minutos):
    mb_usados = minutos * 10  # supomos 10MB por minuto de uso
    custo = calcular_custo("dados", mb_usados)

    if cliente.plano == "pre" and cliente.saldo < custo:
        return "Saldo insuficiente."

    agora = datetime.now()
    fim = agora.replace(minute=agora.minute + minutos)
    cdr = CDR(
        cliente_id=cliente.id,
        numero_chamado="internet",
        inicio=agora,
        fim=fim,
        duracao=minutos,
        tipo_servico="dados",
        quantidade=mb_usados,
        custo=custo
    )

    db = SessionLocal()
    db.add(cdr)
    if cliente.plano == "pre":
        cliente.saldo -= custo
    db.commit()
    db.close()
    return f"Dados usados com sucesso. {mb_usados}MB tributados."
