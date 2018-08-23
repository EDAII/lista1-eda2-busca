def binary_search(list_elements, element):
    inicio = 0
    fim = len(list_elements)
    pivo = int((inicio+fim)/2)

    while inicio+1 != fim:

        if(element < list_elements[pivo]):
            fim = pivo
            pivo = int((inicio+fim)/2)
        elif(element > list_elements[pivo]):
            inicio = pivo
            pivo = int((inicio+fim)/2)
        else:
            return True
