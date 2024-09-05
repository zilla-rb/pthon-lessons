# # print accepts five parameters
# #name = "bronson"
# #print("name is: ", name)
# # flow control the order in which program should be executed
# #decision making condition programing (branching ) or looping
# #condition statement is if-else
# #if test expression
#  # statement

# grade = 65
# if (grade>65):
#      print("pass")   
# else:
#      print("fail")
 
# #if we have more than one condition we use the elif ....else
#  #if(conditionA),
#      #value if true
#      #elif (if conditionA is false)
#      #value if true
#      #else   value if false

#log in check up system
#check username and passward correction

username = input("Enter username")
passward = input ("Enter passward")

#condition to change for username/pass

if username == 'admin':
    if passward == 1234:
        print("logging sucessfull")
        #check for aweak passward

    elif passward == 1234:
         print("Weak password")


    else:
        print("Wrong password: please check and correct") 

else:
    if username == "guest":
        if passward == "guest":
            print("Login Succesful")
        else:
            print("incorrect username/ password combination")

# what if our user does not exist in the system

    else:
       print("Unknown user!")

#create a new file for registration validation usig elif
       # if the email does not contain an @symbol, return invalid email
       #if username field is empty, return an error that the field cannot be empy
       #if password length is lesss than 8, notify user that password must be more than 8 characters

       #otherwise reegister the user.


 

