import time

def indexed_search(list_elements, element, list_size):

    start = time.time()

    result_indexed = []

    lista_indexada = criar_lista_indexada(list_elements, list_size)
    realiza_busca(lista_indexada, list_elements, element)

    stop = time.time()

    elapsed = stop - start
    elapsed = elapsed*1000

    result_indexed.append(elapsed)

    imprime_lista(result_indexed)

def criar_lista_indexada(list_elements, quantidade):

    lista_indexada = []
    index_counter = 0
    valor = int(quantidade/10)

    lista_indexada.append(index_counter)

    while index_counter <= quantidade:
        index_counter += valor

        if index_counter <= quantidade:
            lista_indexada.append(index_counter-1)

    return lista_indexada

#    100 1000 10000 100000

def realiza_busca(lista_indexada, list_elements, element):
    inicio = 0
    fim = len(list_elements)-1

    for i in lista_indexada:
        if element  > list_elements[i]:
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

def imprime_lista(result_indexed):
    for value in result_indexed:
        print(value)
