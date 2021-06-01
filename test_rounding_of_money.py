import pytest
import product_class

def test_get_pretty_price():

    product1 = product_class.Product("Kartoffler", 9) 
    assert product1.calculate_pretty_price() == 9

    product2 = product_class.Product("Beans", 6.0000) 
    assert product2.calculate_pretty_price() == 6

    product3 = product_class.Product("Cola", 9.4231) 
    assert product3.calculate_pretty_price() == 9.5

    product4 = product_class.Product("Snikkers", 5.5) 
    assert product4.calculate_pretty_price() == 5.5

    product5 = product_class.Product("Nudler", 15.7) 
    assert product5.calculate_pretty_price() == 15.95

    product6 = product_class.Product("Penne", 8.99) 
    assert product6.calculate_pretty_price() == 9.