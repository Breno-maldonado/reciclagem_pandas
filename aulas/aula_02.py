import pandas as pd # importamos a biblioteca pandas e nomeamos como pd

# Dados brutos, uma lista de dicionarios 
dados = [
    {"id_venda": 101, "categoria": "Eletrônicos", "valor": 1500.0, "status": "Concluída"},
    {"id_venda": 102, "categoria": "Vestuário", "valor": 200.0, "status": "Concluída"},
    {"id_venda": 103, "categoria": "Eletrônicos", "valor": 800.0, "status": "Cancelada"},
    {"id_venda": 104, "categoria": "Eletrônicos", "valor": 3000.0, "status": "Concluída"},
    {"id_venda": 105, "categoria": "Vestuário", "valor": 150.0, "status": "Cancelada"}
]

# Utilizamos essa função para converter os nossos dados em uma tabela de verdade
df = pd.DataFrame(dados)

# Filtra WHERE status == 'Concluída'
concluidas = df[df["status"] == 'Concluída']

# Agrupa e soma (GROUP BY categoria ... SUM(valor))
faturamento = concluidas.groupby('categoria')['valor'].sum()

print(faturamento)