"""
We want to show prices as ending in either .50, .95, or .00. We always round up to the nearest of these. Implement the function

show_pretty_price(value: decimal) -> decimal
As an example, 99.01 becomes 99.50, and 5.50 becomes 5.50, 99.51 becomes 99.95, and 99.96 becomes 100.00.
"""

import product_class

def mainCode():

    print("")

    product1 = product_class.Product("Cola")
    product1.get_pretty_price()

    print("")

    product2 = product_class.Product("Snikkers", 5.55)
    product2.get_pretty_price()

if __name__ == '__main__':
    mainCode()