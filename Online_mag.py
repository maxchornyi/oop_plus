class Shop():
    def __init__(self, shop_name,store_type):
        self.shop_name=shop_name
        self.store_type=store_type
        self.number_of_units=0
    def describe_shop(self):
        print(f"Store name- {self.shop_name}")
        print(f"Type store- {self.store_type}")
    def open_shop(self):
        print( f"{self.shop_name} open")
    def set_number_of_units(self,num):
        self.number_of_units=num
    def increment_number_of_units(self,num):
        self.number_of_units+=num

shop=Shop('Audi','store 1')
shop2=Shop('Porshe','store 2')
shop3=Shop('Honda','store 3')

#A
shop.open_shop()
shop.describe_shop()

#B
shop.describe_shop()
shop2.describe_shop()
shop3.describe_shop()

#C
store=Shop('Maidan','any unit')
print(store.number_of_units)
store.number_of_units=7
print(store.number_of_units)

#D
print(store.number_of_units)
shop.set_number_of_units(7)
print(shop.number_of_units)
shop.increment_number_of_units(77)
print(shop.number_of_units)

#E
class Discount(Shop):
    def __init__(self, shop_name,store_type,discount_products):
        super().__init__(shop_name,store_type)
        self.discount_products=discount_products
    def get_discounts_ptoducts(self):
        print(f'Get discount: {self.discount_products}')
    def describe_shop(self):
        super().describe_shop()
        print(f'Out discount: {self.discount_products}')

store_discount=Discount('Maidan','any unit','clothes,food,entertainment')
store_discount.get_discounts_ptoducts()
