class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = []
        self.income = 0

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product")
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Invalid amount")
        product_with_premium = Product(product.type, product.name, product.price * 1.3)
        self.products.append((product_with_premium, amount))

    def set_discount(self, identifier, percent, identifier_type='name'):
        if not isinstance(percent, int) or percent < 0 or percent > 100:
            raise ValueError("Invalid discount percent")
        if identifier_type not in ['type', 'name']:
            raise ValueError("Invalid identifier type")
        for product in self.products:
            if (identifier_type == 'type' and product.type == identifier) or \
                    (identifier_type == 'name' and product.name == identifier):
                product.price *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Invalid amount")
        for i, (product, stock) in enumerate(self.products):
            if product.name == product_name:
                if stock < amount:
                    raise ValueError("Insufficient stock")
                self.products[i] = (product, stock - amount)
                self.income += product.price * amount
                return
        raise ValueError("Product not found")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(product.name, stock) for product, stock in self.products]

    def get_product_info(self, product_name):
        for product, stock in self.products:
            if product.name == product_name:
                return product.name, stock
        raise ValueError("Product not found")


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
