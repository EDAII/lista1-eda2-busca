def sentinel_sequential(list_elements, element):

    counter = 0

    while list_elements[counter] != element:
        counter += 1

    # if counter < len(list_elements):
    #     print("O elemento {} está contido no vetor.".format(element))
    # else:
    #     print("O elemento {} não está contido no vetor.".format(element))
