#allows you to create new sets by iterarting over an exsting iterable 
#sytax - '{expression for item in iterable if condition}


nums = [12,2,3,4,4,5,6,7,8,8,9,22,10,22,24]
unique_even = {x for x in nums if x%2==0}
print(unique_even)

#create a set of unique vowels from the string 'hello world'

str = 'Hello, World'
vowels = {char.lower() for char in str if char.lower() in 'aeiou'}

print(vowels)

#CREATE A SET OF PRIME NUMBERS FROM 2 ,20
start = 2
end = 20
prime_num = {num for num in range(start, end+1)
             if all (num% i !=0 for i in range(2,int(num**0.5)+1))}
print(prime_num)