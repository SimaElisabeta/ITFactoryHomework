print(20 * '-', 'EXAMPLE 1', 20 * '-')
"""1. Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""
# internet solution
def missing_char_i(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back

# my solution
def missing_char(str, n):
    str_list = list(str)
    return str.replace(str_list[n], '')

print(missing_char('kitten', 1))



print(20 * '-', 'EXAMPLE 2', 20 * '-')
"""2. Given a string, return a new string where the first and last chars have been exchanged.
front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""
# my solution + internet
def front_back(str):
    if len(str) <= 1:
        return str
    str_front = str[0]
    str_back = str[len(str) - 1:]
    str_middle = str[1:-1]
    return str_back + str_middle + str_front

print(front_back('code'))



print(20 * '-', 'EXAMPLE 3', 20 * '-')
"""3. Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, 
the front is whatever is there. Return a new string which is 3 copies of the front.
front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""
# my solution
def front3(str):
    str_first_3 = str[0:3]
    if len(str) >= 3:
        str = str_first_3 * 3
        return str
    else:
        return str * 3

print(front3('ab'))

# internet solution
def front3_i(str):
    # Figure the end of the front
    front_end = 3
    if len(str) < front_end:
        front_end = len(str)
    front = str[:front_end]
    return front * 3

    # Could omit the if logic, and write simply front = str[:3]
    # since the slice is silent about out-of-bounds conditions.



print(20 * '-', 'EXAMPLE 4', 20 * '-')
"""4. We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
"""

# my solution
def parrot_trouble(talking, hour):
    if talking and not (7 <= hour < 21):
        trouble = True
    else:
        trouble = False
    return trouble

print(parrot_trouble(True, 20))

# internet solution
def parrot_trouble_i(talking, hour):
  return (talking and (hour < 7 or hour > 20))



print(20 * '-', 'EXAMPLE 5', 20 * '-')
"""5. Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged.
not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""
# my solution
def not_string(str):
    if str.startswith('not'):
        return str
    return 'not ' + str

print(not_string('candy'))

# internet solution
def not_string_i(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3
