"""
1.Funcție care primește 2 liste de numere (numerele pot fi dublate).
Returnați numerele comune.
Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 1', 20 * '-')

def get_intersections(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return set1 & set2

print(get_intersections([1, 1, 2, 3], [2, 2, 3, 4]))


"""
2. Funcție care să aplice o reducere de preț. 
- Dacă produsul costă 100 lei și aplicăm reducere de 10%. Pretul va fi 90 de lei.
Tratează cazurile în care reducerea e invalidă. De exemplu o reducere de 110% e invalidă.
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 2', 20 * '-')

def get_discount(price, discount):
    if discount < 0 or discount > 100:
        raise Exception(f'Invalid discount, the discount "{discount}" has to be between 0 and 100')
    return int(price - (price * (discount / 100)))

print(get_discount(100, 10), 'RON')
