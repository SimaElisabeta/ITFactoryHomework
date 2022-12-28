test = 'sdsa123'

nr_count = 0
for i in test:
    if i.isnumeric():
        nr_count = nr_count + 1


assert nr_count >= 3, "the string should contain at least 3 numbers"
print('Am trecut testul')
