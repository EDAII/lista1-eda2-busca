from binary_search import binary_search
from quick_sort import quick_sort

list = [1, 2, 3, 5, 4, 6, 13, 7]

element = 10

quick_sort(list, 0, len(list))

if binary_search(list, element):
    print ("O elemento foi encontrado.")
else:
    print ("O elemento {} não está contido no vetor.".format(element))
