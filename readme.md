# 🛒 Dashboard Estratégico de Compras (Procurement)

![Power BI](https://img.shields.io/badge/Power_BI-Pro-yellow?style=for-the-badge&logo=powerbi)
![Python](https://img.shields.io/badge/Python-ETL-blue?style=for-the-badge&logo=python)
![Poetry](https://img.shields.io/badge/Poetry-Manager-blueviolet?style=for-the-badge)

## 💼 Sobre o Projeto
Este projeto simula um cenário real de uma indústria de manufatura que precisa monitorar a eficiência de seu departamento de compras. O objetivo foi construir uma solução *End-to-End*, desde a geração dos dados brutos via script Python até a análise estratégica no Power BI.

O dashboard responde a perguntas críticas de negócio, como:
* O volume de **Saving** (economia) está alinhado com as metas?
* Quais fornecedores possuem o maior risco de entrega (**OTIF** baixo)?
* Onde estão os gargalos logísticos que impactam o **Lead Time**?

## 🛠️ Tecnologias Utilizadas
* **Python (Pandas/Numpy):** Script para geração de massa de dados complexa (2.500+ registros) com regras de negócio probabilísticas (sazonalidade, atrasos aleatórios e status de entrega).
* **Poetry:** Gerenciamento de dependências e ambiente virtual.
* **Power BI:**
    * **Power Query (M):** ETL, tratamento de tipagem e criação dinâmica da dimensão calendário.
    * **Modelagem:** Star Schema (Fato/Dimensão) para alta performance.
    * **DAX Avançado:** Cálculo de medidas como Saving %, OTIF (On Time In Full), Share of Wallet e Segmentação de Atrasos.
    * **Design:** UI/UX corporativo focado em clareza, uso de Storytelling e navegação por drill-through.
* **PBIP (Power BI Project):** Integração nativa com Git para versionamento do relatório.

## 📊 Estrutura do Relatório

### 1. Visão Executiva (Overview)
Foco em KPIs financeiros. Monitoramento do **Total Spend** (R$ 158M) e **Saving** (4,95%), com análise de tendência mensal para identificar desvios orçamentários.

### 2. Performance de Fornecedores
Matriz de decisão utilizando Scatter Plot (Dispersão) para cruzar **Volume de Compras x Eficiência de Entrega**. Identificação automática de parceiros estratégicos vs. fornecedores de risco.

### 3. Análise Operacional e Lead Time
Diagnóstico logístico. Utilização de Histograma para distribuição de atrasos e **Decomposition Tree** (Árvore Hierárquica) para Root Cause Analysis (Análise de Causa Raiz) dos gargalos de entrega.

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.10+
* Poetry
* Power BI Desktop

### Passos
1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/procurement-dashboard.git](https://github.com/SEU-USUARIO/procurement-dashboard.git)
    cd procurement-dashboard
    ```

2.  **Instale as dependências e gere os dados:**
    ```bash
    poetry install
    poetry run python scripts/gera_dataset.py
    ```
    *Isso criará o arquivo `data/compras_dataset.csv`.*

3.  **Abra o Dashboard:**
    * Navegue até a pasta `powerbi/`.
    * Abra o arquivo `Procurement_Dashboard.pbip`.
    * No Power Query, altere o Parâmetro `CaminhoPastaData` para o diretório local onde o CSV foi gerado.

---
*Desenvolvido como projeto de portfólio focado em Business Intelligence e Data Analytics.*ss