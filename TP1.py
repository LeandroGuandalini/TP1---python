# %% 1
def soma_lista(numeros):
  '''
  Retorna a soma de todos os elementos de uma lista de números.
  
  Parâmetros:
  numeros (list): Lista contendo os números
  
  Retorno:
  int ou float: Soma de todos os elementos da lista
  '''
  return sum(numeros)

lista = [1,23,456,8752]
print(soma_lista(lista))
# %% 2
def retirar_duplicado(lista):
  ''' 
  Remove elementos duplicados de uma lista mantendo a ordem original.

  Parâmetros:
  lista (list): Lista contendo elementos possivelmente repetidos.

  Retorno:
  list: Nova lista sem elementos duplicados, mantendo a ordem original.
  '''
  elementos_vistos = set()
  nova_lista = []
  
  for item in lista:
    if item not in elementos_vistos:
      elementos_vistos.add(item)
      nova_lista.append(item)
  
  return nova_lista

lista = [1,2,2,3,4,4,5,1]
print(retirar_duplicado(lista))
# %% 3
def ordenar_por_idade(lista):
  ''' 
  Ordena uma lista de tuplas (nome, idade) com base na idade, da menor para a maior.

  Parâmetros:
  lista (list): Lista de tuplas, onde cada tupla contém um nome (str) e uma idade (int).

  Retorno:
  list: Lista ordenada de acordo com a idade, da menor para a maior.
  '''
  return sorted(lista, key=lambda pessoa: pessoa[1])

pessoas = [("Ana", 25), ("Bruno", 20), ("Carlos", 30), ("Daniela", 22)]
print(ordenar_por_idade(pessoas))
# %% 4
def contar_frequencia_palavras(texto):
  ''' 
  Conta a frequência de cada palavra em um texto.

  Parâmetros:
  texto (str): String contendo o texto a ser analisado.

  Retorno:
  dict: Dicionário onde as chaves são palavras e os valores são suas respectivas frequências.
  '''
  palavras = texto.lower().split()
  frequencia = {}
  
  for palavra in palavras:
    palavra = palavra.strip(".,!?()[]{}\"'") # Remove pontuação ao redor das palavras
    if palavra:
      # .get(palavra, 0) retorna o valor atual da palavra no dicionário.
      # Se a palavra ainda não existe, retorna 0 (valor padrão).
      # Depois, somamos 1 ao resultado para contar a ocorrência da palavra.
      frequencia[palavra] = frequencia.get(palavra, 0) + 1
  
  return frequencia

texto = "Era uma vez um gato. O gato era muito esperto, muito esperto mesmo!"
print(contar_frequencia_palavras(texto))
# %% 5
def inverter_dicionario(dicionario):
  ''' 
  Inverte as chaves e os valores de um dicionário.

  Parâmetros:
  dicionario (dict): Dicionário cujas chaves e valores serão invertidos.

  Retorno:
  dict: Novo dicionário com as chaves e valores invertidos.
  '''
  return {valor: chave for chave, valor in dicionario.items()}

dicionario = {"a": 1, "b": 2, "c": 3}
print(inverter_dicionario(dicionario))
# %% 6
def unir_dicionarios(dicionario1, dicionario2):
  ''' 
  Une dois dicionários somando os valores das chaves comuns.

  Parâmetros:
  dicionario1 (dict): Primeiro dicionário.
  dicionario2 (dict): Segundo dicionário.

  Retorno:
  dict: Novo dicionário com a união das chaves e a soma dos valores das chaves comuns.
  '''
  resultado = dicionario1.copy()
  
  for chave, valor in dicionario2.items():
    if chave in resultado:
      resultado[chave] += valor
    else:
      resultado[chave] = valor
  return resultado

dicionario1 = {"a": 1, "b": 2, "c": 3}
dicionario2 = {"b": 3, "c": 4, "d": 5}
print(unir_dicionarios(dicionario1, dicionario2))  
# %% 7
def operacoes_conjuntos(conjunto1, conjunto2):
  ''' 
  Retorna um dicionário contendo a união, interseção e diferença entre dois conjuntos.

  Parâmetros:
  conjunto1 (set): Primeiro conjunto.
  conjunto2 (set): Segundo conjunto.

  Retorno:
  dict: Dicionário com as operações "uniao", "intersecao" e "diferenca".
  '''
  return {
    "uniao": conjunto1 | conjunto2, # União dos conjuntos (equivalente a conjunto1.union(conjunto2))
    "intersecao": conjunto1 & conjunto2, # Interseção dos conjuntos (conjunto1.intersection(conjunto2))
    "diferenca": conjunto1 - conjunto2 # Diferença (elementos de conjunto1 que não estão em conjunto2)
  }
  
conj1 = {1, 2, 3, 4}
conj2 = {3, 4, 5, 6}
print(operacoes_conjuntos(conj1, conj2))
# %% 8
def elementos_unicos(lista):
  ''' 
  Retorna uma lista contendo apenas os elementos únicos da lista original, sem manter a ordem.

  Parâmetros:
  lista (list): Lista de números.

  Retorno:
  list: Lista com elementos únicos.
  '''
  return list(set(lista)) # o set(lista) remove os elementos duplicados (só permite elementos únicos), list converte em uma lista novamente

lista = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print(elementos_unicos(lista))
# %% 9
def eh_subconjunto(conjunto1, conjunto2):
  ''' 
  Verifica se o primeiro conjunto é um subconjunto do segundo.

  Parâmetros:
  conjunto1 (set): Primeiro conjunto.
  conjunto2 (set): Segundo conjunto.

  Retorno:
  bool: True se conjunto1 for um subconjunto de conjunto2, False caso contrário.
  '''
  return conjunto1.issubset(conjunto2)

conj1 = {1, 2, 3}
conj2 = {1, 2, 3, 4, 5}
print(eh_subconjunto(conj1, conj2))  # Saída: True

conj3 = {1, 6}
print(eh_subconjunto(conj3, conj2))  # Saída: False
# %% 10
import pandas as pd

def ler_csv(nome_arquivo):
  ''' 
  Lê um arquivo CSV e imprime cada linha separadamente usando pandas.

  Parâmetros:
  nome_arquivo (str): Nome do arquivo CSV a ser lido.

  Retorno:
  None: Apenas imprime as linhas do arquivo.
  '''
  df = pd.read_csv(nome_arquivo) # Lê o arquivo CSV em um DataFrame
  for index, row in df.iterrows():
    print(row.to_dict())
  
ler_csv('dados.csv')

# %% 11
import pandas as pd

def escrever_csv(nome_arquivo, dados):
  ''' 
  Escreve uma lista de dicionários em um arquivo CSV, incluindo os cabeçalhos.

  Parâmetros:
  nome_arquivo (str): Nome do arquivo CSV a ser criado.
  dados (list): Lista de dicionários, onde cada dicionário representa uma linha do arquivo.

  Retorno:
  None: Apenas cria e escreve os dados no arquivo.
  '''
  df = pd.DataFrame(dados)
  df.to_csv(nome_arquivo, index=False, encoding='utf-8') # Salva como CSV sem o índice

dados = [
    {"Nome": "Alice", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Bruno", "Idade": 30, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carlos", "Idade": 22, "Cidade": "Belo Horizonte"}
]

escrever_csv('dados.csv', dados)
# %% 12
import json

def ler_json(nome_arquivo):
  ''' 
  Lê um arquivo JSON e retorna um dicionário representando os dados contidos no arquivo.

  Parâmetros:
  nome_arquivo (str): Nome do arquivo JSON a ser lido.

  Retorno:
  dict: Dicionário com os dados do arquivo JSON.
  '''
  with open(nome_arquivo, 'r', encoding="utf-8") as f:
    return json.load(f)

dados = ler_json('dados.json')
print(dados)

#%% 13
import json

def escrever_json(nome_arquivo, dados):
  ''' 
  Escreve um dicionário em um arquivo JSON.

  Parâmetros:
  nome_arquivo (str): Nome do arquivo JSON a ser salvo.
  dados (dict): Dicionário contendo os dados a serem salvos no arquivo JSON.

  Retorno:
  None: Apenas salva os dados no arquivo JSON.
  '''
  with open(nome_arquivo, 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)
  
dados = [
    {"Nome": "Alice", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Bruno", "Idade": 30, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carlos", "Idade": 22, "Cidade": "Belo Horizonte"}
]

escrever_json('dados.json', dados)
# %% 14
import pandas as pd

def processar_csv(nome_arquivo):
  ''' 
  Processa um arquivo CSV e cria um dicionário onde as chaves são as cidades e os valores são listas contendo os nomes das pessoas que pertencem a cada cidade.

  Parâmetros:
  nome_arquivo (str): Nome do arquivo CSV a ser lido.

  Retorno:
  dict: Dicionário onde as chaves são cidades e os valores são listas de nomes.
  '''
  df = pd.read_csv(nome_arquivo)
  
  resultado = df.groupby('Cidade')['Nome'].apply(list).to_dict()
  return resultado

dados = processar_csv('pessoas.csv')
print(dados) 
# %% 15
import pandas as pd

def criar_conjunto_nomes(nome_arquivo):
  ''' 
  Cria um conjunto a partir de um arquivo de texto contendo uma lista de nomes, um por linha, 
  e retorna um conjunto com apenas os nomes únicos, utilizando pandas.

  Parâmetros:
  nome_arquivo (str): Nome do arquivo de texto a ser lido.

  Retorno:
  set: Conjunto contendo os nomes únicos.
  '''
  df = pd.read_csv('nomes.txt', header=None, names=['Nome'])
  
  nomes_unicos = set(df['Nome'])
  
  return nomes_unicos

nomes_unicos = criar_conjunto_nomes('nomes.txt')
print(nomes_unicos)
# %% 16 
def indice_invertido(nome_arquivo):
  ''' 
  Cria um índice invertido de palavras a partir de um arquivo de texto.
  
  Parâmetros:
  nome_arquivo (str): Nome do arquivo de texto a ser lido.

  Retorno:
  dict: Dicionário onde as chaves são palavras e os valores são conjuntos de números de linha onde cada palavra aparece.
  '''
  indice = {}
  with open(nome_arquivo, encoding='utf-8') as f:
    for num_linha, linha in enumerate(f, start=1):
      palavras = linha.lower().split()
      for palavra in palavras:
        palavra = palavra.strip(".,!?()[]{}\":;")
        if palavra:
          indice.setdefault(palavra, set()).add(num_linha)
  return indice

resultado = indice_invertido('texto.txt')
print(resultado)

# %%
