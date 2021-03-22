import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# importing specific functions
# from module_name import function_name
# from module_name import funtion_0, function_1, function_2
# with this syntax you only need to type make_pizza instead of pizza.make_pizza

# using as to give a function an alias
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')

# using as to give a module an alias
# import pizza as p
# p.make_pizza(...)

# importing all funcions of a module
# from pizza import *
# make_pizza(...)

