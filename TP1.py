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
# %%
