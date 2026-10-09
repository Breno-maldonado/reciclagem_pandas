# Crie o filtro duplo no Pandas para pegar apenas os registros que tenham: tipo igual a 'Eletrônicos' E status igual a 'Concluída'.

import pandas as pd

tabela = [
    {'id': 101, 'tipo': 'Eletrônicos', 'valor': 1500.0, 'status': 'Concluída'},
    {'id': 102, 'tipo': 'Vestuário', 'valor': 200.0, 'status': 'Concluída'},
    {'id': 103, 'tipo': 'Eletrônicos', 'valor': 800.0, 'status': 'Cancelada'},
    {'id': 104, 'tipo': 'Eletrônicos', 'valor': 3000.0, 'status': 'Concluída'},
    {'id': 105, 'tipo': 'Vestuário', 'valor': 150.0, 'status': 'Cancelada'}
]

df = pd.DataFrame(tabela)

filtro = df[(df['tipo'] == 'Eletrônicos') & (df['status'] == 'Concluída')]

print(filtro)