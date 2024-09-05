# # # a function is a sequence of instruction that performs a task, bundled as unit
# # #when creating a python programm we have to proup everything into file

# # def shake():
# #     print('This is a function')
    
# # shake()

# #def a function to get athe name and location of aperson

# # def my_func(name, location): # name and location are arguments or parameter reguired by our programa
#     # print(f"hello {name}! Hope you are doing great. Tell me, tell me are you from {location}")


# # my_func("bronson", "dee dog land")# Bronson and dee dog land are reffered as positional arguments

# #an argument is a variable ,value or object passeed to a function or a method as input
# #positional argument  are arguments that need to be include in the 
# #using key word arguments

# # my_func(name='bronson', location='dee dog land')

# # example above uses a key word argument (*kwargs*).
# # A key word argument is an argument that is passed to a function or method which is procedeed by a keyword and an equals 
# # sign ( function(keyword=value))

# # create a function to calculate the are of a triangle given the base and heigh of the 2 aguments ,bass and heght


# # def triArea(base, height):
# #     area = 0.5*base*height
# #     return area
# # #define triangle with base of 10 , height of15

# # base=10
# # height=15
# # print(f" the area of the triangle is: {triArea(base,height=15)}")

# #calculate tip and total amount to be paid to a resturant

# # def total_amount(bill_amount, tipPerc = 10): #10 is the default value should there be no
# #     total_amount = bill_amount*(1+0.01*tipPerc)
# #     total_amount = round(total_amount,2)
# #     print(f'please pay ksh{total_amount}')

#     #write a python function show_employee() that 
#     #a. ot should accept the employee name and salary display both 
#     #b.if the salary is missing in the funcion call, then assign
#     # default value of 9000 to salary

# # def show_employee(name, salary=900000):
# #         print("Name:", name, "Salary:", salary)

# # show_employee("mee", 209090)
# # show_employee("Hayan", )

# # write a fumction to sum all the list in alist

# # write a function to check if anumber falls over agiven range.
# # write a function that accepts a string and counts the number of upper and lowercase letters

# # def create_name(first, last):
# #     first = first.capitalize()
# #     last = last.capitalize()
# #     return first + " " + last
# # full_name = create_name("spongebob", "squarepants")

# # print(full_name)

# # def count(first_num, last_num):
# #     first_num = range[1, 100]
# #     last_num = range[101, 200]
# #     guess = input("enter your guess: ")
# #     while guess not in last_num and first_num:
# #         print("number out of range try again??{first_num}:{last_num}")
    
# #     else:
# #         print("number in range welll done??")
     

# # def sum_of_list(list=[1,2,3,4]):
# #     return sum(list)

# # sum_of_list(list=[1, 4 ])


# # def num_in_range(number, range_start, range_end ):

# #     number = input("Enter your guess please:____")
# #     range_start =0
# #     range_end = 50
# #     if number is not (range_start and range_end) :
       
# #        print(f"{number} is within the range of {range_start} and {range_end}")
# #        return True
# #     else:
# #        print(f" {number} is not within the range of {range_start} and {range_end}.")
# #        return False
 

# num = range(1, 100)
# guess = input("Enter your guess?: ")

# if guess is not  num:
#    print(f"{guess} is not in the range please dont be a full!!")
# else:
#    print(f"{guess} is in range well done!!")


def greeting(name):
    def hello():
        return'Hellow, '+name+ "!"
    return hello
greet = greeting("Antony")
print(greet())

def make_pretty(func):
    def inner():
        func()

    return inner
def ordinary():
    print("i am ordinary")

decorated_func = make_pretty(ordinary)#make pretty is a decorated
decorated_func()

#the @symbol with decorator

#decorating functions with parameters

def divide(x,y):
    return x/y
# if we pass y as 0, we get an error.
#make adecorater to check if this is the case
    