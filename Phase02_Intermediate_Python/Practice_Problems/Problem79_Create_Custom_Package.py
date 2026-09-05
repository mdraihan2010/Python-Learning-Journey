# একাধিক module নিয়ে একটি custom package তৈরি করো।

# Folder structure:
# my_package/
#     __init__.py
#     math_module.py
#     utility_module.py

# math_module.py
def add(a, b):
    return a + b


# utility_module.py
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# main.py
# from my_package.math_module import add
# from my_package.utility_module import celsius_to_fahrenheit

print("Addition:", add(10, 20))
print("Temperature:", celsius_to_fahrenheit(30))