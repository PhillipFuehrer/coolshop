import random
import math

class Product:

    def __init__(self, product_name, price = None, on_sale = False, sale_price = None):
        self.__product_name = product_name
        if price is None:
            self.__price =  random.uniform(0.01, 1000.00)
        else:
            self.__price = price
        self.__prettyPrice = self.calculate_pretty_price()
        self.__on_sale = on_sale
        self.__sale_price = sale_price

    def calculate_pretty_price(self):
        
        nextInt = math.floor(self.__price)   
        fracture = self.__price - nextInt    

        if fracture == 0:
            return nextInt

        elif fracture > 0 and fracture <= 0.50:
            return nextInt+0.5

        elif fracture > 0.50 and fracture <= 0.95:
            return nextInt+0.95

        else:
            nextInt += 1
            return nextInt


    def get_pretty_price(self):
        
        print(f"Internal price: {self.__price}")
        print(f"Public price : The product {self.__product_name} will cost {self.__prettyPrice:.2f}")

    def get_on_sale(self):
        return self.__on_sale

    def get_on_sale_new_price(self):
        return self.__sale_price

    def set_on_sale(self,status):
        self.__on_sale = status


