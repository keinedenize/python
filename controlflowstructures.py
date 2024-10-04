# Control flow structures.
# Determine the order in which programs can be executed basing on loops and conditions

#Conditional statement
# These statements base on a particluar condition e.g elif, if, else
# Write a program that asks a user for the food type bought from the market.
# The program should print, bought chicken if the user enetrs chicken 
#the program should print liver elif if the user bought liver
# esle the program should print fish
food_type = input("Enter the food_type bought:")lower()
if food_type ! =='chicken' or food_type !='fish' or food_type !='liver':
    print("Please chose from chicken,fish,liver")
    
    print(f"You have bought chicken")
elif food_type =='liver':
    print(f"You have bought liver")
else:
    print(f"You bought fish")
            
            
    