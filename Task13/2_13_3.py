# Task 3. Product Store
class Product:

    def __init__(self, type_, name, price):
        self.type_ = type_
        self.name = name
        self.price = price
        self.amount = 0

    # def __repr__(self):
    #     return f"{self.type_}---{self.name}----{self.price}"


class ProductStore:
    revenue = []
    profit = []

    def __init__(self):
        self.dict_of_product = {}
        self.dict_price = {}

    def add_prod(self, new_prod, amount):
        self.dict_price.update({new_prod.name:new_prod.price})
        new_prod.price = new_prod.price * 1.3
        self.dict_of_product.update({f" {new_prod.type_} {new_prod.name}": [new_prod.price, amount]})

    def set_discount(self, identifier, percent):
        for key, value in self.dict_of_product.items():
            if identifier in key:
                value[0] = value[0] - (value[0] * percent) / 100
        return self.dict_of_product

    def sell_product(self, product_name, amount):
        for key, value in self.dict_of_product.items():
            if product_name in key:
                if value[1] <= 0 or amount > value[1]:
                    print(f"Not enough goods in stock. You can sell not more {value[1]}")
                    break
                else:
                    purhase = value[0] * amount
                    balance = value[1] - amount
                    value[1] = balance
                    ProductStore.revenue.append(purhase)
                for key4, val4 in self.dict_price.items():
                    if product_name ==key4:
                        zero_purhase = val4*amount
                ProductStore.profit.append(zero_purhase)

        return self.dict_of_product

    def get_income(self):
        print(f" OUR PROFIT = {sum(self.revenue)-sum(self.profit) } USD")

    def show_all_product(self):
        print("Our SHOP"'\n', "-----------------------")
        for key, val in self.dict_of_product.items():
            print(f" type, name | {key} | price- q-ty {val}")
        print("-----------------------")


    def get_product_info(self, product_name):
        for key, value in self.dict_of_product.items():
            if product_name in key:
                res = key.split()
                res.clear()
                res.append(product_name)
                res = ''.join(res)
                print(f"Name <{res}> Q-ty <{value[1]} pcs>")


p1 = Product('Sport', 'T-shirt', 100)
p2 = Product('Sport', 'Shorts', 50)
p3 = Product('Sport', 'Swimming trunks ', 20)
p4 = Product('Clothes', 'Adidas', 20)
p1_1 = Product('Game', 'NFS', 80)

ps = ProductStore()
ps.add_prod(p1, 10)
ps.add_prod(p2, 40)
ps.add_prod(p3, 70)
ps.add_prod(p4, 200)
ps.add_prod(p1_1, 1000)

ps.set_discount('T-shirt', 10)
ps.sell_product('Shorts', 1)
ps.sell_product('NFS', 1)
ps.sell_product('NFS', 1)

ps.show_all_product()
ps.get_product_info('NFS')
# ps.get_product_info('T-shirt')
ps.get_income()
