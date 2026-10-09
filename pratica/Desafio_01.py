# Sua missão: O chefe pediu para ver o total faturado (soma do valor) apenas das vendas menores ou iguais a R$ 1000,00 (<= 1000).

import pandas as pd

tabela = [
    {'id': 101, 'tipo': 'Eletrônicos', 'valor': 1500.0, 'status': 'Concluída'},
    {'id': 102, 'tipo': 'Vestuário', 'valor': 200.0, 'status': 'Concluída'},
    {'id': 103, 'tipo': 'Eletrônicos', 'valor': 800.0, 'status': 'Cancelada'},
    {'id': 104, 'tipo': 'Eletrônicos', 'valor': 3000.0, 'status': 'Concluída'},
    {'id': 105, 'tipo': 'Vestuário', 'valor': 150.0, 'status': 'Cancelada'}
]

df = pd.DataFrame(tabela)

vendas_baixas = df[df['valor'] <= 1000]

quantidade = vendas_baixas.groupby('tipo')['valor'].sum()

print(quantidade)