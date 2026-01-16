import os
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd

# Configurações
num_linhas = 2500
np.random.seed(42)

# Dados Mestres
fornecedores = [
    (101, "Metalúrgica AçoForte"),
    (102, "Plásticos do Sul"),
    (103, "Eletrônicos Tech"),
    (104, "Global Embalagens"),
    (105, "Química Inovadora"),
    (106, "Transportes & Log"),
    (107, "Componentes BR"),
    (108, "Importadora Oriente"),
]

produtos_categorias = {
    "Matéria-Prima": [
        "Bobina de Aço",
        "Polímero Granulado",
        "Resina Epóxi",
        "Chapa de Alumínio",
    ],
    "Componentes": [
        "Microchip X1",
        "Parafuso Inox",
        "Placa de Circuito",
        "Sensor Óptico",
    ],
    "Embalagem": ["Caixa Papelão G", "Pallet Padrão", "Filme Stretch"],
    "MRO": ["Luvas de Proteção", "Óleo Lubrificante", "Ferramentas de Corte"],
}

# Gerando Dados
data = []

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

for i in range(1, num_linhas + 1):
    # Pedido e Datas
    id_pedido = f"PO-{10000 + i}"
    days_offset = random.randint(0, 364)
    data_pedido = start_date + timedelta(days=days_offset)

    # Lead Time Previsto (5 a 20 dias)
    lead_time_previsto = random.randint(5, 20)
    data_entrega_prevista = data_pedido + timedelta(days=lead_time_previsto)

    # Simulação de Atrasos e Entrega Real
    r = random.random()
    atraso = 0  # Inicializa com 0 para evitar erro de tipagem

    if r < 0.70:  # 70% Entregue no prazo ou antes
        atraso = random.randint(-3, 0)
        status = "Entregue"
    elif r < 0.90:  # 20% Atrasado
        atraso = random.randint(1, 15)
        status = "Entregue"
    elif r < 0.95:  # 5% Pendente (sem data real)
        atraso = 0
        status = "Pendente"
    else:  # 5% Devolvido
        atraso = random.randint(1, 5)
        status = "Devolvido"

    if status == "Pendente":
        data_entrega_real = pd.NaT
    else:
        data_entrega_real = data_entrega_prevista + timedelta(days=atraso)

    # Fornecedor e Produto
    forn = random.choice(fornecedores)
    id_fornecedor = forn[0]
    nome_fornecedor = forn[1]

    categoria = random.choice(list(produtos_categorias.keys()))
    produto = random.choice(produtos_categorias[categoria])

    # Valores
    qtd = random.randint(10, 500)
    preco_tabela = round(random.uniform(10, 500), 2)
    # Negociação: geralmente pagamos menos que a tabela (saving), mas as vezes pagamos mais (custo extra)  # noqa: E501
    fator_negociacao = random.uniform(0.85, 1.05)
    preco_negociado = round(preco_tabela * fator_negociacao, 2)

    data.append(
        [
            id_pedido,
            data_pedido,
            data_entrega_prevista,
            data_entrega_real,
            id_fornecedor,
            nome_fornecedor,
            categoria,
            produto,
            qtd,
            preco_negociado,
            preco_tabela,
            status,
        ]
    )

# Criar DataFrame
df = pd.DataFrame(
    data,
    columns=[
        "ID_Pedido",
        "Data_Pedido",
        "Data_Entrega_Prevista",
        "Data_Entrega_Real",
        "ID_Fornecedor",
        "Nome_Fornecedor",
        "Categoria_Produto",
        "Produto",
        "Qtd",
        "Preco_Unitario_Negociado",
        "Preco_Tabela",
        "Status_Entrega",
    ],
)

# DEFINIÇÃO DE CAMINHOS
# Identifica o diretório raiz do projeto (assumindo que o script está em /scripts)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
data_dir = os.path.join(project_root, "data")

# Garante que a pasta 'data' existe (cria se não existir)
os.makedirs(data_dir, exist_ok=True)

# Caminho completo do arquivo
file_path = os.path.join(data_dir, "compras_dataset.csv")

# Salvar CSV
df.to_csv(file_path, index=False)
print(f"Dataset gerado com sucesso em: {file_path}")
