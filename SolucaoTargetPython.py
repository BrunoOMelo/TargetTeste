# %% [markdown]
# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

# %%
print(
    '\n\n2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.\n\n')


# Função que calcula a sequencia de fibonacci utilizando recursão
def fibonacci(x):
    if (x < 2):
        return x
    else:
        return (fibonacci(x - 1) + fibonacci(x - 2))


# definição do numero a ser procurado na sequencia de fibonacci
n = 20
# inicializando a variavel, a fim de evitar resíduos da memoria
i = 0

# loop que consiste em chamar a função de calculo ate que:
# 1: o valor retornado pela função seja maior do que aquele digitado, provando que o número não/
# esta contemplado em fibonacci
# 2:O valor retornado pela função seja igual ao digitado, provando que o número pertence a sequencia
# Note que mesmo ao cair em uma condição de parada, a função é executada mais uma vez, isso foi/
# colocado de proposito, para que o usuário consiga verificar que o próximo número da sequência/
# realmente não é o desejado


while True:
    print(fibonacci(i))
    i = i + 1
    if (fibonacci(i) > n):
        print(fibonacci(i))
        print('O numero {} não pertence a sequencia de Fibonacci!'.format(n))
        break
    else:
        if (fibonacci(i) == n):
            print(fibonacci(i))
            print('O numero {} pertence a sequencia de Fibonacci!'.format(n))
            break

# %% [markdown]
#
#
# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#
#   • O menor valor de faturamento ocorrido em um dia do mês;
#
#
#   • O maior valor de faturamento ocorrido em um dia do mês;
#
#
#   • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

# %%
# UTILIZANDO BIBLIOTECA PANDAS
# Apenas para demonstrar minha familiaridade com ferramentas de analise de dados

# Deixarei comentado para nao interromper o funcionamento, caso o avaliador não tenha a biblioteca 'pandas'
# Apenas para demonstrar minha familiaridade com ferramentas de analise de dados

print(
    '\n\n3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:\n• O menor valor de faturamento ocorrido em um dia do mês;\n• O maior valor de faturamento ocorrido em um dia do mês;\n• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.\nIMPORTANTE:\na) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;\nb) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;\n\n')

'''

#Importando biblioteca
import pandas as pd

#lendo arquivo e tranformando em Data Frame
df_faturamento = pd.read_json('dados.json')
#Limpando dados, ou seja, tirando todos os registros de valor 0
df_faturamento.drop(df_faturamento.loc[df_faturamento['valor']==0].index, inplace=True)
#Configurando a coluna "dia" como indice, para facilitar a leitura
df_faturamento.set_index('dia', inplace=True)
#Retornando o dia e o valor correspondente ao menor faturamento diario
fat_min = df_faturamento.loc[df_faturamento['valor']==df_faturamento['valor'].min()] 
#Retornando o dia e o valor correspondente ao maior faturamento diario
fat_max = df_faturamento.loc[df_faturamento['valor']==df_faturamento['valor'].max()] 
# media mensal
media_mensal = round(df_faturamento['valor'].mean(),4)
#dias em que o faturamento foi acima da media mensal
acima_media_dias = df_faturamento.loc[df_faturamento['valor']>df_faturamento['valor'].mean()] 
#total de dias que o faturamento foi acima da média mensal
acima_media_count = acima_media_dias.shape[0]

print('\nUTILIZANDO BIBLIOTECA PANDAS\n')

print('Menor faturamento no mês fornecido: \n{} '.format(fat_min))
print('\nMaior faturamento no mês fornecido: \n{} '.format(fat_max))
print('\n\nFaturamento acima da média mensal: \n{} \nMédia mensal:{}\nTotal de dias {} '.format(acima_media_dias,media_mensal,acima_media_count))'''

# %%
# METODO MANUAL
# importando o pacote necessario para leitura do arquivo json
import json

# leitura dos dados
with open('dados.json') as arquivo:
    dados_brutos = json.load(arquivo)

# criação de uma nova variavel que recebera somente os dados válidos, aqueles diferentes de 0
dados = []
i = 0
for i in range(len(dados_brutos)):
    if (dados_brutos[i]['valor'] != 0):
        dados.append(dados_brutos[i])


# %%
# função para o menor faturamento

def menor_venda(dados):
    # inicializamos a variavel menor com algum valor da lista, o primeiro como exemplo
    menor = dados[0]['valor']
    # loop para percorrer todos os dados
    for i in range(len(dados)):
        # estrtura de verificação: caso o dado na posição do iterador seja menor do que o atual/
        # este é guardado como o "novo menor", ao final, apenas o menor valor estará nesta variavel
        if (dados[i]['valor'] < menor):
            # limpando a variavel menor para que não ocorra erros na sobrescrita
            del menor
            menor = dados[i]['valor']
    return menor


print('Menor venda no mês fornecido: {}'.format(menor_venda(dados)))


# %%
# função para o maior faturamento
# exatamente a mesmo lógica anterior, com pequenas modificações para que retorne o maior valor

def maior_venda(dados):
    maior = dados[0]['valor']
    for i in range(len(dados)):

        if (dados[i]['valor'] > maior):
            del maior
            maior = dados[i]['valor']
    return maior


print('Maior venda no mês fornecido: {}'.format(maior_venda(dados)))


# %%
# função para contar os dias que ultrapassaram a media de faturamento mensal
def media_faturamento(dados):
    # inicilização da variavel que conterá a soma dos faturamentos
    soma = 0
    # estrutura de repetição
    for i in range(len(dados)):
        # obtendo a soma de todos os valores da chave 'valor'
        soma += dados[i]['valor']
    # após obter a soma, calcula-se a média destes dados, com arredondamento de 4 casas,/
    # assim como a base de dados
    media = round(soma / len(dados), 4)
    # inicialização da variavel que irá receber a quantidade de dias acima da média
    cont = 0
    # estrutura de repetição para percorrer os dados
    for i in range(len(dados)):
        # estrutura de condição: se o dado na posição do iterador estiver com o valor/
        # maior que "media", acumula-se uma unidade no conta
        if (dados[i]['valor'] > media):
            cont += 1
    return cont


print('Número de dias com faturamento acima da media mensal: {}'.format(media_faturamento(dados)))


# %% [markdown]
# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#
# SP – R$67.836,43
#
#
# RJ – R$36.678,66
#
#
# MG – R$29.229,88
#
#
# ES – R$27.165,48
#
#
# Outros – R$19.849,53
#
#
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

# %%
# função para calculo da representaçaõ de cada estado
# como parametro temos o 'estado' como o faturamento do determinado estado, e total/
# que indica o montante do faturamento dos estados em conjunto
def representacao(estado, total):
    # um calculo simples que retorna a porcentagem da participação, com duas casas decimais
    return round(estado * 100 / total, 2)


# faturamento de cada estado
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

# faturamento total conjunto
total = sp + rj + mg + es + outros

print(
    '\n\n4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado: \nSP – R$67.836,43 \nRJ – R$36.678,66\nMG – R$29.229,88\nES – R$27.165,48\nOutros – R$19.849,53\nEscreva um programa na linguagem que desejar onde calcule o percentual de representação\n que cada estado teve dentro do valor total mensal da distribuidora.\n\n')

print('Representação de SP: {}%'.format(representacao(sp, total)))
print('Representação de RJ: {}%'.format(representacao(rj, total)))
print('Representação de MG: {}%'.format(representacao(mg, total)))
print('Representação de ES: {}%'.format(representacao(es, total)))
print('Representação de Outros: {}%'.format(representacao(outros, total)))
print('Faturamento total: {}'.format(total))


# %% [markdown]
# 5) Escreva um programa que inverta os caracteres de um string.
#
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse

# %%
# função para inverter string
def inverter(palavra):
    # converter uma string em uma lista permite a facil minupulação
    lista = list(palavra)
    # inicializando a variavel auxiliar na permutação
    aux = 0
    # extraindo o tamanho da string
    tamanho = len(palavra)
    # extraindo o numero de posições
    fim = tamanho - 1
    # loop for que aplica o algoritmo de permutação nas posições da lista
    # de modo que ocorra a troca com a posição oposta, exemplo, a primeira posição troca com a ultima
    for i in range(int((tamanho / 2))):
        aux = lista[i]
        lista[i] = lista[fim]
        lista[fim] = aux
        fim -= 1
    return lista


# string a ser invertida
palavra = "cachorro"

print(
    '\n\n5) Escreva um programa que inverta os caracteres de um string.\nIMPORTANTE:\na) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;\nb) Evite usar funções prontas, como, por exemplo, reverse\n\n')

print('Invertendo a palavra "{}": {} '.format(palavra, inverter(palavra)))

# %%
