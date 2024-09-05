# h_letters = []
# for letter in 'human':
#     h_letters.append(letter)
#     print(h_letters)


# #we can achieve the same i a simpler way 
# # using list comprehemsion

# h_letters = [ letter for letter in 'human']

# print(h_letters)

# # we can archive the same results using lambda expression

# letter = list(map(lambda x: x, 'human'))

# print(letter)

#list comprehension allow you to create a new list by iterating over an existing iterable and applying a condition or transformayion 
#sytax = [expression for item in iterable if condition]

#create a list of square numbers from 1-5sq

# square_num = [x**2 for x in range(1,6)]
# print(square_num)


#create alist of even numbers from an existing list 

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_nums = [x for x in numbers if x%2==0]
# print(even_nums)

#convert the following list into comprehension
fruits = ['Mangos' ,'oranges','pineapples','lemons']
new_fruits = []
for n in fruits:
    new_fruits.append(n)

print(new_fruits)

fruits = ['Mangos' ,'oranges','pineapples','lemons']
new_fruits = [n for n in fruits]
print(new_fruits)

#create a new list fro fruits that starts with m
#hint, use a for loop
fruits = ['Mangos' ,'oranges','pineapples','lemons']
new_fruits = [n for n in fruits if n.startswith("M")]
print(new_fruits)


#dict comprehension allow you to create a new dictionary by iterating over existing specific key-value pairs
#
#sytax = '{key_expression: value_expression for item initerable  if condition}
 

#create a dictionary of square number range 1-5
square_num = [x**2 for x in range(1,6)]
print(square_num)


keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

dictionary = {k: v for k, v in(zip(keys,values))}
print(dictionary)