from __future__ import annotations


# REAL LIFE example - exercise 1
class CustomerServideFacade:
    def __init__(self):
        self._order_ready = OrderReady()
        self._billing = Billing()
        self._shipping = Shipping()

    def new_order(self) -> None:
        print('Your order is being processed:')
        self._order_ready.products_in_stock()
        self._order_ready.payment_validation()
        self._order_ready.pack()
        self._billing.bill()
        self._shipping.ship()


class OrderReady:
    def products_in_stock(self):
        print('Checking stock...')
        print('All products available!')

    def payment_validation(self):
        print('Your payment was validated!')

    def pack(self):
        print('Packing your products...\n')


class Billing:
    def bill(self):
        print('Billing your order...\n')


class Shipping:
    def ship(self):
        print('Shipping order...\n')
        return True


order = CustomerServideFacade()
order.new_order()
