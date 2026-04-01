import requests
import pandas as pd
import json

#Definindo uma váriavel para uma API
api_url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=available'

#Fazendo uma requisição da API
try:
    response = requests.get(api_url)
    response.raise_for_status()  # Resposta de status
    data = response.json() #Traz resposta em JSON

    # Conversão para um dataframe do pandas
    df = pd.DataFrame(data)

#Exceptions para erros na requisição
except requests.exceptions.RequestException as e:
    print(f"Erro ao conectar com a API: {e}")
except ValueError as e:
    print(f"Erro em converter JSON da API: {e}")
except Exception as e:
    print(f"Aconteceu um erro inesperado: {e}")


#Realiza uma cópia para manter o original
def transform(df):
  df = df.copy()

#Criação de uma nova coluna que pega apenas o nome da categoria que o pet está atribuido
df["category_pet"] = df["category"].apply(
    lambda x: x.get("name") if isinstance(x, dict) else None)

#Criado uma lista que percorrre atribuindo para caso tenha mais de uma 'tag' que seria a informação do pet
df["tags_pet"] = df["tags"].apply(
    lambda lista: "; ".join(
        [item.get("name") for item in lista if isinstance(item, dict) and item.get("name") is not None]
    ) if isinstance(lista, list) else ""
)

#Remoção das colunas com informações desnecessárias
df = df.drop(columns=["category", "tags","photoUrls"])
df = df.fillna("")

#Visualização do dataframe 
transformed_df = transform(df)
display(df.head(20))

def load(transformed_df,output_path):
  df.to_excel(output_path, index=False)

#Tranforma em arquivo excel na Google Colab
load (transformed_df,'/content/pets_disponiveis.xlsx')

#Baixa o arquivo diretamente na minha máquina
from google.colab import files
files.download('/content/pets_disponiveis.xlsx')
