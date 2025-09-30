import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configurações
dias = 7
intervalo_minutos = 15
inicio = datetime(2025, 1, 1, 0, 0, 0)
fim = inicio + timedelta(days=dias)

# Lista para armazenar dados
dados = []

# Função para simular valores
def gerar_dados(timestamp):
    hora = timestamp.hour
    dia_semana = timestamp.weekday()  # 0 = segunda, 6 = domingo

    # Temperatura (varia mais no horário comercial)
    if 6 <= hora <= 18:
        temperatura = np.random.normal(23, 2)  # média 23°C
    else:
        temperatura = np.random.normal(20, 1.5)  # noite mais fria

    # Luminosidade (0 à noite, maior no dia)
    if 6 <= hora <= 18:
        luminosidade = np.random.normal(500, 100)  # lux médio
    else:
        luminosidade = np.random.normal(5, 2)  # praticamente escuro

    # Ocupação (maior em horário comercial nos dias úteis)
    if dia_semana < 5 and 8 <= hora <= 18:
        ocupacao = np.random.choice([0, 1], p=[0.3, 0.7])  # 70% ocupado
    else:
        ocupacao = np.random.choice([0, 1], p=[0.9, 0.1])  # pouco uso

    return temperatura, luminosidade, ocupacao

# Geração dos registros
atual = inicio
sensor_id = 1

while atual < fim:
    temperatura, luminosidade, ocupacao = gerar_dados(atual)

    dados.append({
        "timestamp": atual.strftime("%Y-%m-%d %H:%M:%S"),
        "sensor_id": sensor_id,
        "temperatura_C": round(temperatura, 2),
        "luminosidade_lux": round(luminosidade, 2),
        "ocupacao": ocupacao
    })

    atual += timedelta(minutes=intervalo_minutos)

# Salvar em CSV
df = pd.DataFrame(dados)
df.to_csv("smart_office_data.csv", index=False)

print("Arquivo smart_office_data.csv gerado com sucesso!")
