# A empresa decidiu aplicar uma taxa de entrega de R$ 15,00 em todas as vendas para calcular o valor total final do pedido. Usando o mesmo df, crie uma nova coluna chamada 'valor_total' que seja a soma do 'valor' original da venda mais os R$ 15,00 da taxa.

import pandas as pd

tabela = [
    {'id': 101, 'tipo': 'Eletrônicos', 'valor': 1500.0, 'status': 'Concluída'},
    {'id': 102, 'tipo': 'Vestuário', 'valor': 200.0, 'status': 'Concluída'},
    {'id': 103, 'tipo': 'Eletrônicos', 'valor': 800.0, 'status': 'Cancelada'},
    {'id': 104, 'tipo': 'Eletrônicos', 'valor': 3000.0, 'status': 'Concluída'},
    {'id': 105, 'tipo': 'Vestuário', 'valor': 150.0, 'status': 'Cancelada'}
]

df = pd.DataFrame(tabela)

valor_total = df['taxa'] = df['valor'] + 15.0

print(df)