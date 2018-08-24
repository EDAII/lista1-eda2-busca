def indexed_search(list_elements, element):

    list_sequences = [100, 1000, 10000, 100000]
    result_indexed = []

    for l in list_sequences:
        lista_indexada = criar_lista_indexada(list_elements, l)
        realiza_busca(lista_indexada, list_elements)
        # Lembra de dar o append no tempo na lista result_indexed

"""
Tabela com 5 elementos

[3, 10, 27, 38, 40]

alvo = 18

inicio =
fim =

"""

def criar_lista_indexada(list_elements, quantidade):

    lista_indexada = []
    index_counter = 0
    valor = quantidade/10

    lista_indexada.append(index_counter)

    while index_counter != quantidade:
        index_counter += valor
        lista_indexada.append(index_counter)

    return lista_indexada

#    100 1000 10000 100000

def realiza_busca(lista_indexada, list_elements):
    inicio = 0
    fim = len(list_elements)

    for i in lista_indexada:
        if element > list_elements[i]:
            inicio = i
        elif element < list_elements[i]:
            fim = i
            break
        else:
            inicio = i
            fim = i
            break

    was_found = False

    while inicio != fim:
        if element == list_elements[inicio]:
            was_found = True
            break
        inicio += 1
