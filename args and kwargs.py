def func(**kwargs):
    print(kwargs)

#all calls equivalent. they print out a:1, b:42
func(a=1, b=42)
func(**{'a':1, 'b':42})
func(**dict (a=1, b=42))

#  all the above do the same value.
# adding ** infront of the parameter name in the function definition tells
# python to use that name to colect a valriable number of keyword parameters.



# def shipping_lable(*args, **kwargs):

#     for arg in args:
#         print(args, end=" ")

#     print()

#     for value in kwargs.values(): 
        

#         print(value, end=" ")
# shipping_lable("Dr.", "sponge man", "Squarepants", "111",
#                street="123 Fake st.",
#                apt="100",
#                city="Detroit",
#                stake="M1",
#                zip="54321")
# 1