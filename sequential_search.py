def sequential_search(list_elements, element):

    i = 0

    while i <= len(list_elements):
        if list_elements[i] == element:
            break
        i += 1
