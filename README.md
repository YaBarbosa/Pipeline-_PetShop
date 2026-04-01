# Pipeline-_PetShop
Criação de um Pipeline para boas práticas do ETL levando em consideração uma API Pública de PetShop

# 🐍 ETL Pipeline - Petstore API

Este projeto implementa um pipeline ETL em Python que consome dados da API pública Petstore, transforma campos JSON aninhados e gera um DataFrame estruturado para análise.

Tecnologias Utilizadas

* Python 3
* Pandas
* Requests
* Google Colab / Jupyter Notebook

## 📥 Extract

Os dados são extraídos da API pública:

```
https://petstore.swagger.io/v2/pet/findByStatus?status=available
```

## 🔄 Transform

Transformações aplicadas:

* Extração de `category.name` de JSON aninhado
* Extração de múltiplas `tags`
* Conversão de listas em string separada por `;`
* Remoção de colunas JSON originais
* Tratamento de valores nulos

Exemplo de transformação:

```python
df["category.name"] = df["category"].apply(
    lambda x: x.get("name") if isinstance(x, dict) else None
)
```
## 📤 Load

Resultado final exibido como DataFrame estruturado:


Opcionalmente pode ser exportado para:

* CSV
* Excel
* Banco de dados

## 📁 Estrutura dos Dados

| id | name | status | category.name | tags.name |
| -- | ---- | ------ | ------------- | --------- |

## ▶️ Como Executar

1. Clone o repositório
2. Instale dependências:

```
pip install pandas requests
```

3. Execute o notebook ou script Python

## 📌 Exemplo de Saída

```
id | name | status | category.name | tags.name
1  | dog  | available | Dogs | friendly; cute
```

## 🧠 Conceitos Demonstrados

* ETL Pipeline
* API Data Extraction
* JSON Flattening
* Pandas Data Transformation
* Data Cleaning

## 👨‍💻 Autor

Projeto desenvolvido para prática de Engenharia de Dados e criação de pipelines ETL em Python.

