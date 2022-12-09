#A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.

def hello():
    print("HEllo, user!")

#A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.

def pack (argument1,argument2,argument3):

#A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.
 
    def eat_lunch(my_list):
        if len(my_list)==0:
            print("my lunchbox is empty!")
        else:
            for i in range(len(my_list)):
                if i ==0:
                    print("first i eat {my_list[0]}")
                else:
                    print("next i eat{my_list[i}")

    hello()
    print(pack(argument1,argument2,argument3))
    print(pack(0,1,2))
    eat_lunch([])
    eat_lunch(["sandwich"])
    eat_lunch(["alcapuria","relleno","mofongo","pie"])