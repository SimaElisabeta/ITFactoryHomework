# 1. Sa se implementeze un decorator care masoara timpul necesar executiei unei functii.
import functools
from time import perf_counter
import csv


def time_execution(func):
    @functools.wraps(func)
    def wrapper(*arg, **kwargs):
        start = perf_counter()
        func_return = func(*arg, **kwargs)
        stop = perf_counter()
        print(f'Total time to execute function {func.__name__}(): {stop - start} seconds')
        print(func_return)
        return stop - start

    return wrapper


@time_execution
def do_some_calc():
    my_list = []
    for i in range(100000):
        x = i * 10 ** 1000
        my_list.append(x)
    return f'I finished execution'


do_some_calc()
print()


# 2.a) Sa se genereze primele 100 de numere prime folosind liste, si apoi folosind generator.
# 2.b) Comparati diferenta de timp necesara generarii.
def is_prime(number):
    if number < 2:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    return True


@time_execution
def first_100_primes_list():
    current_num = 2
    prime_list = []
    while len(prime_list) < 100:
        if is_prime(current_num):
            prime_list.append(current_num)
        current_num += 1
    return prime_list


def generator():
    current_num = 2
    count = 0
    while count < 100:
        if is_prime(current_num):
            count += 1
            yield current_num
        current_num += 1


@time_execution
def first_100_primes_generator():
    return [i for i in generator()]


print('RESULT:',
      'first_100_primes_list() function was more efficient' if first_100_primes_list() < first_100_primes_generator()
      else 'first_100_primes_generator() function was more efficient')


# 3. Scrieti un decorator care primeste ca argument numele unui fisier si pentru orice functie apelata, el va scrie in acel fisier:
#   * numele functiei,
#   * lista de argumente ca si string
#   * si rezultatul apelului.
# Fisierul este de tip csv. Functiile decorate pot primi oricate argumente

def write_func_details_in_CSV(file_name):
    def func_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_return = func(*args, **kwargs)
            func_name = func.__name__
            func_args = str(func.__code__.co_varnames)
            data = [[func_name, func_args, func_return]]
            with open(file_name, "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)

        return wrapper

    return func_decorator


@write_func_details_in_CSV('func_details.csv')
def get_full_name(first_name, last_name):
    return f'{first_name} {last_name}'


@write_func_details_in_CSV('func_details.csv')
def greet(name):
    return f'Hello {name}'


get_full_name('Giulia', 'Smith')
greet('Neighbor')
