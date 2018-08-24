# from binary_search import binary_search
from quick_sort import quick_sort
# from transposition_sequencial import transposition_sequential
# from sentinel_sequential import sentinel_sequential
from indexed_search import indexed_search
import random

list = [1, 2, 3, 5, 4, 6, 13, 7]

element = 10

# quick_sort(list, 0, len(list))

# if binary_search(list, element):
#     print ("O elemento foi encontrado.")
# else:
#     print ("O elemento {} não está contido no vetor.".format(element))

def insere_elementos_desordenados(number_of_elements, list_elements, limit):
    for x in range(number_of_elements):
        value = random.randint(0, limit)

        while(value in list_elements):
            value = random.randint(0, limit)

        list_elements.append(value)


list_sequences = [100, 1000, 10000, 100000]

for e in list_sequences:
    lista = []
    insere_elementos_desordenados(e, lista, e**3)
    quick_sort(lista, 0, len(lista))
    indexed_search(lista, element, e)
