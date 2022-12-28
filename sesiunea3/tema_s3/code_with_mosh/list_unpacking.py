# ----- list unpacking example -----
print(20 * '-', 'EXEMPLU 1', 20 * '-')  ################## EXEMPLU 1 ##################
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *others, last = numbers

print(first, last)
print(others)


print(20 * '-', 'EXEMPLU 2', 20 * '-')  ################## EXEMPLU 2 ##################
letters = ['a', 'b', 'c']
for letter in letters:
    print(letter)

# ----- get the index of each item -----
# folosind functia enumerate() - ne va returna un obiect enumerate
# obiectul rezultat este iterabil, astfel incat in fiecare iteratie,
# obiectul enumerate ne va returna un tuple (tuple este read only - nu putem adauga noi elemente in el)
# output: (0, 'a')
for letter in enumerate(letters):
    print(letter)

# ----- acces the index and elementof each object -----
# folosind functia enumerate(), facem unpacking la obiect/tuple
# output: 0 a
for index, letter in enumerate(letters):
    print(index, letter)


print(20 * '-', 'EXEMPLU 3', 20 * '-')  ################## EXEMPLU 3 ##################
# Add elements
letters = ['a', 'b', 'c']
letters.append('d')         # adaugm un element la final de lista                           .append(element)
letters.insert(0, '-')      # adagam un element la o pozitie specifica                      .insert(index, element)
print(letters)

# Remove elements
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters.pop()               # elimina mereu ultimul element din lista                       .pop()
letters.pop(0)              # elimina elementul de la un index specific                     .pop(index)
letters.remove('b')         # elimina un obiect/element, atunci cand nu stim                .remove(element)
                            # pozitia lui pe index. Aici remove, va elimina
                            # primul elem din lista care are valoarea specificata ('b')
del letters[0:3]            # eliminam un range de items/elemente                            del list[i_start:i_finish]
letters.clear()             # eliminam toate elementele din lista, golim lista              .clear(index)
print(letters)

# Finding objects in the list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters.index('a'))   # returneaza indexul elementului ('a'), nu schimba lista        .index(element)
print(letters.count('a'))   # returneaza de cate ori apare elementul ('a') in lista         .count(element)

# Sorting a list
numbers = [3, 51, 2, 8, 6]
numbers.sort()              # sorteaza intreaga lista in ordine crescatoare                 .sort()
numbers.sort(reverse=True)  # sorteaza intreaga litsta in ordine descrescatoare             .sort(reverse=True)
print(sorted(numbers))      # sorteaza lista dar nu o modifica ci creeaza una noua           sorted(variabila)
print(sorted(numbers, reverse=True))
print(numbers)
