# coding: utf-8 

# Começando com os imports
import csv
import matplotlib.pyplot as plt
from collections import Counter # importando para checagem extra

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Só pra eu garantir que veio linhas corretamente (TB)
print(data_list[0:10])

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.

def imprimir_primeiras_20_linhas(data_list):
    for i in range(min(20, len(data_list))):  # Como queria pegar uma quantidade determinada de linhas, setamos aqui o range
        print(data_list[i])


print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras\n")
imprimir_primeiras_20_linhas(data_list)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

def imprimir_coluna_6(data_list):
    for i in range(min(20, len(data_list))):  
        print(data_list[i][6]) # Imprime o elemento da sétima coluna para cada linha

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
imprimir_coluna_6(data_list)


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

def column_to_list(data_list, index):
    column_list = []
    # Verifica se a lista não está vazia
    if not data_list:
        return column_list

    # Obtendo o numero de colunas checando a primeira linha
    num_colunas = len(data_list[0])

    # Itera sobre cada linha da lista de dados
    for linha in data_list:
        # Verifica se a linha possui colunas suficientes
        if len(linha) > index:
            # Adiciona o elemento da coluna à nova lista
            column_list.append(linha[index])
        else:
            column_list.append(None)  # Garantindo valor nulo se a coluna não exister na linha 

    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1048575, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.

# Aqui supus que eu não precisasse criar uma função que conta, dado que faremos isso mais embaixo
# Por isso usei uma biblioteca que faz isso de forma muito rápida e eficaz (https://docs.python.org/3/library/collections.html#collections.Counter)

generos = Counter(column_to_list(data_list, -2))
print(generos)
male = generos['Male']
female = generos['Female']


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 665437 and female == 198247, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

def count_gender(data_list):
    male = 0
    female = 0

    for row in data_list:
        #Acessando o item desejado pelo index para cada linha
        gender = row[-2]
        #Itera sobre a lista contando cada tipo de genero apresentado
        if gender == 'Male':
            male += 1
        elif gender == 'Female':
            female += 1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 665437 and count_gender(data_list)[1] == 198247, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.

# Criei duas funções aqui: uma que usa a função criada acima e outra pra checar usando a biblitoeca importada 

# Usando a funcao count_gender

def most_popular_gender(data_list):

    # Uando a função criada na tarefa 05
    male_count, female_count = count_gender(data_list)

    # Comparando os resultados pra saber qual é mais comum
    if male_count > female_count:
        return "Male"
    elif female_count > male_count:
        return "Female"
    else:
        return "Equal"

# Usando a bilbioteca

def most_popular_gender(data_list):
    # Tô usando a biblioteca acima apresentada para retornar os mesmos valores da tarefa 5
    genders = Counter(column_to_list(data_list, -2))
    most_common_gender, count = genders.most_common(1)[0]
    # Checando se os retornos são iguais
    if genders['Male'] == genders['Female']:
        return "Equal"
    else:
        return most_common_gender

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.

# Para criar o gráfico eu precisei checar algumas coisas

# Checando os retornos das colunas
user_types = Counter(column_to_list(data_list, -3))
print(user_types)

# Criando uma função que retorna as quantidades usando o mesmo padrao da count_gender
def count_user(data_list):
    Subscriber = 0
    Customer = 0
    Dependent = 0

    for row in data_list:
        user_type= row[-3]
        
        if user_type == 'Subscriber':
            Subscriber += 1
        if user_type == 'Customer':
            Customer += 1
        elif user_type == 'Dependent':
            Dependent += 1

    return [Subscriber, Customer, Dependent]

print("\nTAREFA 7: Verifique o gráfico!")
user_types = Counter(column_to_list(data_list, -3))
types = ["Subscriber", "Customer","Dependent"]
quantity = count_user(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuario')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipos de usuário')
plt.show(block=True)


# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Pois temos 184891 registros sem a informação de genero."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9

# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
#  Você não deve usar funções prontas para isso, como max() e min().

# Armazenando todas durações das viagens registradas em uma variável
trip_duration_list = column_to_list(data_list, 2)

def calcular_estatisticas(trip_duration_list):
    # Convertendo os campos para inteiro
    trip_duration_list = [int(item) for item in trip_duration_list]

    min_trip = float('inf')  # Atribuindo um valor gigante, ou seja infinito
    max_trip = float('-inf') # Atribuindo um valor minusculo, ou seja menos infinito
    soma = 0
    n = len(trip_duration_list)

    # Iterando sobre a lista para calcular mínimo, máximo e soma
    for numero in trip_duration_list:
        if numero < min_trip:
            min_trip = numero
        if numero > max_trip:
            max_trip = numero
        soma += numero

    # Calculando a média, que nada mais é que a soma dos valores dividido pela quantidade de iterações que tivemos
    mean_trip = soma / n

    # Calculando a mediana
    # Para isso precisamos ordenar os dados, usei a função sorted que já existe (pega uma lista e retorna uma nova lista os elementos em ordem classificada)
    lista_ordenada = sorted(trip_duration_list)
    if n % 2 == 0:
        mean_trip = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        median_trip = lista_ordenada[n // 2]
    return min_trip, max_trip, mean_trip, median_trip

resultado = calcular_estatisticas(trip_duration_list)
min_trip, max_trip, mean_trip, median_trip = resultado  
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)


# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 885, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 624, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()

# o set basicamente remove duplicadas e nos informaquais registros exclusivos
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 578, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.

print("Você vai encarar o desafio? (yes ou no)")

def count_items(column_list):
    item_types = set() # usando set para pegarmos os itens unicos de cada index
    item_counts = [] # usando lista para armazernarmos as quantidades

    for item in column_list:
        item_types.add(item)  # Adicionando cada iteracao no item_types
    
    for item_type in item_types:
        item_counts.append(column_list.count(item_type)) # Contando as recorrencias dos itens acima iterados
    
    return list(item_types), item_counts

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
column_list = column_to_list(data_list, -2)
types, counts = count_items(column_list)
print("\nTAREFA 12: Imprimindo resultados para count_items()")
print("Tipos:", types, "Counts:", counts)
assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
assert sum(counts) == 1048575, "TAREFA 12: Resultado de retorno incorreto!"
# -----------------------------------------------------