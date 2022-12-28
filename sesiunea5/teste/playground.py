"""
1. Creaza o functie, care ia ca si parametru un numar.
El va analiza numarul si va returna rezultate diferite.
Reguli:
1. Daca numarul este divizibil cu 3 va returna stringul: Fizz
2. Daca numarul e divizibil cu 5, atunci va returna stringul: Buzz
3. Daca numarul e divizibil cu ambele (3 si 5), va returna FizzBuzz
4. Iar pentru orice alte numere, va returna numarul insusi din input
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 1', 20 * '-')

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return 'FuzzBuzz'
    if input % 3 == 0:
        return 'Fuzz'
    if input % 5 == 0:
        return 'Buzz'
    return input

print(fizz_buzz(5))


"""
2. Given a string and a non-negative int n, return a larger string that is n copies of the original string.
Example: 
string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 2', 20 * '-')

def string_times(str, n):
    return str * n

print(string_times('Hi', 4))


"""
3. Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever 
is there if the string is less than length 3. Return n copies of the front;
Example:
front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc
"""
# REZOLVARE:
print(20 * '-', 'EXERCITIUL 3', 20 * '-')

def front_times(str, n):
    first_3 = str[:3]
    if len(str) <= 3:
        return first_3 * n
    return first_3 * n

print(front_times('Abc', 5))


"""
4. Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
Hint (Printeaza din 2 in 2)
Example:
string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""

# REZOLVARE:
print(20 * '-', 'EXERCITIUL 4', 20 * '-')

def string_bits(str):
    return str[::2]

print(string_bits('Heeololeo'))


"""
5. Given a non-empty string like "Code" return a string like "CCoCodCode".
Example:
string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""
print(20 * '-', 'EXERCITIUL 5', 20 * '-')

def string_splosion(str):
    result = ''
    for i in range(len(str)):
        result += str[:i+1]
    return result

print(string_splosion('Code'))


"""
6. Given a string, return the count of the number of times that a substring length 2 appears in the 
string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
Example:
last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""
print(20 * '-', 'EXERCITIUL 6', 20 * '-')

def last2(str):
    if len(str) < 2:
        return 0
    count = 0
    for i in range(1, len(str)-2):
        if (str[i] == str[i+1]) and (str[i] != str[i+2]):
            count += 1
    return count

print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
print(last2('xxxaxaxxaxx'))
