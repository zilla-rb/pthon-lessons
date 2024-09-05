# data = {"Name": "Brian",
#         "Age": 34,
#         "city": "Mombasa"
#         }

# #updating the dictionary.ei adding new value pair

# data.update({"occupation": "programmer"})
# data.pop("Name") # removes a field
# data["Age"] = 23 #updated the age
# data.popitem()# removevs the laest list added

# # key = data.keys()
# # for key in data.keys(): # itterates in the dictionary to output the key values
# #     print(key) 
# # print(data)

# #items = capitals.items()
# for key,value in data.items():
#     print(f"{key}: {value}") #printing the key and values


menu = {"pizza": 5.88,
        "popcoens": 6.03,
        "rice": 3.40,
        "soda": 1.00,
        "chips": 0.77,
        "lemonade": 0.88,
        "fries": 1.23,
        " pretzel": 5.90,}

cart = []
total = 0
  
print ("--------MENU----")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------")

while True:
   food = input("Select an item (qto quit): ").lower() #changes user input to lowercase
   if food == "q":
       break
   elif menu.get(food)is not None:
       cart.append(food)
print("-----YOUR ORDER----")
for food in cart:
    total += menu.get(food)
    print(food,end=" ") 

print()
print(f"Total is ${total:.2f}")