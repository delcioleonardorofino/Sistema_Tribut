from datetime import datetime, timedelta
from models import CDR

def registrar_voz(cliente, numero_destino, duracao_minutos):
    custo = duracao_minutos * 1  # 1Mt por minuto
    if cliente.plano == 'pre-pago' and cliente.saldo < custo:
        return "Saldo insuficiente para chamada."
    
    # Atualiza saldo se for pré-pago
    if cliente.plano == 'pre-pago':
        cliente.saldo -= custo

    hora_inicio = datetime.now()
    hora_fim = hora_inicio + timedelta(minutes=duracao_minutos)

    cdr = CDR(
        cliente_id=cliente.id,
        numero_chamador=cliente.numero,
        numero_chamado=numero_destino,
        hora_inicio=hora_inicio,
        hora_fim=hora_fim,
        duracao=duracao_minutos,
        tipo_servico="voz",
        quantidade=duracao_minutos,
        custo=custo
    )
    cliente.cdrs.append(cdr)
    return f"Chamada registrada: {duracao_minutos} min"


def registrar_voz(cliente, duracao):
    # Lógica para registrar uma chamada de voz
    # Exemplo simples:
    custo = duracao * 1  # Supondo que o custo seja 1 Mt por minuto
    cdr = CDR(numero_chamador=cliente.numero, 
              numero_chamado="Número Destino",
              inicio="Hora Início",
              fim="Hora Fim",
              duracao=duracao,
              tipo_servico="voz",
              quantidade=duracao,
              custo=custo)
    cliente.cdrs.append(cdr)
    return custo


def registrar_sms(cliente, numero_destino):
    custo = 1  # 1Mt por SMS
    if cliente.plano == 'pre-pago' and cliente.saldo < custo:
        return "Saldo insuficiente para SMS."
    
    if cliente.plano == 'pre-pago':
        cliente.saldo -= custo

    cdr = CDR(
        cliente_id=cliente.id,
        numero_chamador=cliente.numero,
        numero_chamado=numero_destino,
        hora_inicio=datetime.now(),
        hora_fim=datetime.now(),
        duracao=0,
        tipo_servico="sms",
        quantidade=1,
        custo=custo
    )
    cliente.cdrs.append(cdr)
    return "SMS registrado com sucesso"

def registrar_dados(cliente, minutos):
    mb_por_minuto = 1  # Supondo 1MB/min como taxa de consumo
    mb_usados = minutos * mb_por_minuto
    custo = mb_usados * 0.5  # 0.5Mt por MB

    if cliente.plano == 'pre-pago' and cliente.saldo < custo:
        return "Saldo insuficiente para dados móveis."
    
    if cliente.plano == 'pre-pago':
        cliente.saldo -= custo

    cdr = CDR(
        cliente_id=cliente.id,
        numero_chamador=cliente.numero,
        numero_chamado="INTERNET",
        hora_inicio=datetime.now(),
        hora_fim=datetime.now() + timedelta(minutes=minutos),
        duracao=minutos,
        tipo_servico="dados",
        quantidade=mb_usados,
        custo=custo
    )
    cliente.cdrs.append(cdr)
    return f"Uso de dados registrado: {mb_usados} MB"
