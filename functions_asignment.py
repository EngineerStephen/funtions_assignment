#Task 1: Create functions for each arithmetic operation, with parameters for two numbers to be used in the operation.
print()
user_input = input("Please enter two of your favorite numbers, separated by a comma: ")
num1, num2 = map(float, user_input.split(",")) # map function to convert the input to float, had  to do some external studying here
user_operation = input("would you like to add, subtract, multiply, or divide these numbers? ")
print()
print("Your answer is: ")


def add_nums(num1, num2):
     return num1 + num2
    
def subtract_nums(num1, num2):
  return num1 - num2

def multiply_nums(num1, num2):
    return num1 * num2

def divide_nums(num1, num2):
    return num1/num2

if user_operation == "add":
    print(add_nums(num1, num2))
elif user_operation == "subtract":
    print(subtract_nums(num1, num2))
       
elif user_operation == "multiply":
    print(multiply_nums(num1, num2))
elif user_operation == "divide":
    print(divide_nums(num1, num2))
else:
    print("Invalid input, please try again.")
   

    

# Task 1: Write a function that lets the user add items to a list, 
# make sure you ask the user what they would like to add 
# (reminder: ensure the function has a parameter to receive the list). 
# Task 2: Include a feature to remove items from the list. 
# Task 3: Add a function that prints out the entire list.

items = []
def add_item(items):
    print()
    print("Welcome to the shopping list app!")
    item = input("Which item would you like to add?")
    print()
    items.append(item) 
    while True:
        add_more = input("Would you like to add another item? (yes/no)")
        if add_more == "no":
            print()
            remove_item = input("Ok. But would you like to remove an item? (yes/no)")    
            if remove_item == "no":
                break
            elif remove_item == "yes":
                remove_item = input("Which item would you like to remove?")
                if remove_item in items:
                        items.remove(item)
                else:
                    print("Item not found.")
            else:
                print("Invalid input, please try again.")
                
        elif add_more == "yes":
            print()
            item = input("Which item would you like to add?")
            items.append(item)          
        else:
            print("Invalid input, please try again.")
    
    print()
    print("Here is your list of items, thank you for shopping:   ")
    print(items)
    
add_item(items)