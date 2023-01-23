from sesiunea9.marketplace.marketplace_repository import CSVMarketplaceRepository, JSONMarketplaceRepository
from pprint import pprint


def choose_db():
    db_menu = """
        DB MENU
    1. CSV
    2. JSON
    """
    print(db_menu)
    cmd = int(input("Enter DB type: "))
    file_type = 'csv' if cmd == 1 else 'json'
    file_name = f'Products.{file_type}'
    return (
               CSVMarketplaceRepository(file_name) if file_type == 'csv'
               else JSONMarketplaceRepository(file_name)
           ), file_type


def print_menu():
    menu = """
        MENU
    1. ADD Product
    2. DELETE Product
    3. SHOW Products
    4. EXIT MENU
    """
    print(menu)


def add_product(repository, repo_type):
    name = input('Enter product name: ')
    price = float(input('Enter product price: '))
    product_id = abs(hash(name) + hash(price))
    if repo_type == 'csv':
        repository.add([product_id, name, price])
    else:
        repository.add({'ID': product_id, 'name': name, 'price': price})


def delete_product(repository):
    product_id = input('Enter the product ID to be deleted: ')
    repository.delete(product_id)


def show_product(repository):
    pprint(repository.read())


def run():
    repo, repo_type = choose_db()
    while True:
        print("*" * 50)
        print_menu()
        product_input = int(input(f"Please enter your choose: "))
        if product_input == 1:
            add_product(repo, repo_type)
        elif product_input == 2:
            delete_product(repo)
        elif product_input == 3:
            show_product(repo)
        elif product_input == 4:
            exit(0)
        else:
            print('Comanda invalida!')


run()
