# import example_utility
from example_utility import multiply, add

# import shopping.shopping_cart
from shopping.shopping_cart import buy

# print(example_utility)
print(multiply(2, 3))
print(add(2, 3))

# print(shopping.shopping_cart)
# print(shopping.shopping_cart.buy("shoes"))
print(buy("shoes"))

# print(__name__)

if __name__ == "__main__":
    print("This is the main file - example_main.py")
