# def my_function():
#     test = 1
#     print("this is my function", test)

# test = 0
# my_function()
# print("test for global function", test)

#LEGB = local, enclosing,global,built-in

#if a variable is assigned inside a def, it is local to that function
#if a variable is assigned is an enclosing def, it is nonlocal to nested functions
#if ''is assigned outside all defs, it is global to the current file (module)

# x = 99
# def funcion1():
#     x = 88

def outer():
    test = 1 #outer scope
    def inner():
        test=2 #inner scope
        print("inner",test)

    inner()
    print("outer", test)

test = 0 #global scope
outer()
print('global',test)    

# global and nonlocal statements

def out():
    test = 1 #outer scope
    def inner():
        nonlocal test
        test=2 #inner scope
        print("inner",test)

    inner()
    print("outer", test)

test = 0 #global scope
outer()
print('global',test)    

def lib():
    lib_Name = "Bronson's Library"
    #create a sectionn for books eg action books

    def section():
        # enclosing scope
        section_name = 'action'
        #function to hold the book details
        def book():
            book_tittle = 'Maze runner'
            print(f'Book tittle: {book_tittle}')
            print(f'Section: {section_name}')
            print(f'Library: {lib_Name}')
        book()    
    section()
lib()


