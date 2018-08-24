from binary_search import binary_search
from quick_sort import quick_sort
from transposition_sequencial import transposition_sequential
from sentinel_sequential import sentinel_sequential
from indexed_search import indexed_search
from sequential_search import sequential_search
from plot_graphics import plota_grafico
import random
import time

def main():
    opcao = 'x'

    menu_inicial = {
        '1': analisa_tempo,
        '2': transposition_sequential
    }

    print("Escolha uma das opções abaixo para escolher um contexto:")
    print("(1) - Análise de duração de algoritmos")
    print("(2) - Acompanhamento de números mais pesquisados")
    print("(0) - Sair")

    print("Escolha um valor válido:")
    opcao = input()

    if opcao == '1':
        menu_inicial[opcao]()
    elif opcao == '2':
        lista = []
        size_list = 15
        insere_elementos_desordenados(size_list, lista, size_list**3)

        menu_inicial[opcao](lista)

def insere_elementos_desordenados(number_of_elements, list_elements, limit):
    for x in range(number_of_elements):
        value = random.randint(0, limit)

        while(value in list_elements):
            value = random.randint(0, limit)

        list_elements.append(value)


def analisa_tempo():

    size_list = 10000

    result_binary = []
    result_indexed = []
    result_sentinel = []
    result_simple = []

    i = 0

    while i <= 50:

        lista = []
        insere_elementos_desordenados(size_list, lista, size_list**2)
        quick_sort(lista, 0, len(lista))

        # element = random.randint(0, size_list**2)
        element = lista[-1]

        # ord_start = time.time()
        # ord_stop = time.time()
        #
        # ord_res = ord_stop - ord_start

        start = time.time()
        binary_search(lista, element)
        stop = time.time()

        elapsed = stop - start # + ord_res

        result_binary.append(elapsed)

        start = time.time()
        indexed_search(lista, element, size_list)
        stop = time.time()

        elapsed = stop - start# + ord_res

        result_indexed.append(elapsed)

        list = lista
        list.append(element)

        start = time.time()
        sentinel_sequential(list, element)
        stop = time.time()

        elapsed = stop - start

        result_sentinel.append(elapsed)

        start = time.time()
        sequential_search(lista, element)
        stop = time.time()

        elapsed = stop - start

        result_simple.append(elapsed)

        i += 1

    plota_grafico(result_binary, result_indexed, result_sentinel, result_simple)

    return
main()
