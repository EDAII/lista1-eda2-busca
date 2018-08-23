def transposition_sequential(list_elements):
    while(True):
        print("Selecione uma opção:")

        print("(1) - Buscar elemento")
        print("(2) - Inserir elemento")
        print("(3) - Excluir elemento")
        print("(4) - Listar elemento")
        print("(0) - Sair do algoritmo")

        option = input()

        if option != '0':
            menu[option](list_elements)
        else:
            return

def buscar_elemento(list_elements):

    print("Digite um elemento para buscar na lista:")
    element = int(input())

    counter = 0

    for e in list_elements:
        if(e == element):
            print("O elemento está contido na lista")
            transposiciona_elemento(list_elements, e, counter)
            break
        counter += 1

    if counter == len(list_elements):
        print("O elemento não está contido na lista.")

def inserir_elemento(list_elements):

    print("Digite um elemento para inserir na lista:")
    element = input()

    if not list_elements.contains(element):
        list_elements.append(element)
    else:
        print("Este elemento já pertence à lista.")

def excluir_elemento(list_elements):

    print("Digite um elemento para excluir da lista:")
    element = input()

    if list_elements.contains(element):
        list_elements.remove(element)
    else:
        print("Este elemento não está contido na lista.")

def listar_elementos(list_elements):
    print("Lista de registro")
    print("{")
    for registro in list_elements:
        imprimir_registro(registro)
    print("}")

def transposiciona_elemento(list_elements, element, counter):
    list_elements[counter] = list_elements[counter-1]
    list_elements[counter-1] = element

def imprimir_registro(registro):
    print(registro)

menu = {
    '1': buscar_elemento,
    '2': inserir_elemento,
    '3': excluir_elemento,
    '4': listar_elementos
}
