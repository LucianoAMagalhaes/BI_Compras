import os

import pandas as pd

# 1. Carregar o Dataset
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
file_path = os.path.join(project_root, "data", "compras_dataset.csv")

df = pd.read_csv(file_path)

# Converter colunas de data
cols_data = ["Data_Pedido", "Data_Entrega_Prevista", "Data_Entrega_Real"]
for col in cols_data:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# --- CÁLCULO DOS KPIS (Simulando a lógica do DAX) ---

# 1. Total Spend
df["Spend_Line"] = df["Qtd"] * df["Preco_Unitario_Negociado"]
total_spend = df["Spend_Line"].sum()

# 2. Saving
df["Tabela_Line"] = df["Qtd"] * df["Preco_Tabela"]
total_saving_val = (df["Tabela_Line"] - df["Spend_Line"]).sum()
saving_pct = total_saving_val / df["Tabela_Line"].sum()

# 3. Lead Time Médio
# Regra: Apenas entregues/devolvidos (não pendentes)
df_entregues = df.dropna(subset=["Data_Entrega_Real"]).copy()
df_entregues["Lead_Time"] = (
    df_entregues["Data_Entrega_Real"] - df_entregues["Data_Pedido"]
).dt.days
lead_time_medio = df_entregues["Lead_Time"].mean()

# 4. OTIF %
# Regra DAX: Numerador = Entregue E No Prazo / Denominador = Tudo menos Pendente
df_finalizados = df[df["Status_Entrega"] != "Pendente"].copy()
total_pedidos_finalizados = len(df_finalizados)

# On Time: Data Real <= Prevista
# In Full: Status == 'Entregue' (Não devolvido)
otif_hits = df_finalizados[
    (df_finalizados["Status_Entrega"] == "Entregue")
    & (df_finalizados["Data_Entrega_Real"] <= df_finalizados["Data_Entrega_Prevista"])
]
otif_pct = len(otif_hits) / total_pedidos_finalizados

# --- IMPRIMIR GABARITO ---
print("=" * 40)
print("   GABARITO DE AUDITORIA (PYTHON)   ")
print("=" * 40)
print(f"Linhas Totais: {len(df)}")
print(f"Total Spend:   R$ {total_spend:,.2f}")
print(f"Total Saving:  R$ {total_saving_val:,.2f}")
print(f"Saving %:      {saving_pct:.2%}")
print(f"Lead Time:     {lead_time_medio:.1f} dias")
print(f"OTIF %:        {otif_pct:.2%}")
print("=" * 40)
