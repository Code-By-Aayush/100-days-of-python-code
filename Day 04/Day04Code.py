import  random

# random.randint(a,b) --> for random integer.
# random.randint() --> for random floating point number (between 0 and 1)
# random.uniform(a,b) --> for random floating point number (between a and b)

random_number = random.randint(1,10)
print(random_number)

floating_point = round(random.random(),2)
print(floating_point)

number2 = round(random.uniform(0.0,45.0),2)
print(number2)

# #Self Made Module :-
import my_module
variable = my_module.my_fav_number
print(variable)

# # Self Try :-

print("Welcome To Automatic Digital Dice Roll! 🎲🎲🎲")
no_of_die = int(input("Enter Number of Dice You Want to Roll: ")) # Dice = 1 , 2 ,3 ...

for roll in range(1,no_of_die+1):
    number = random.randint(1,6)
    print(f"Dice Number {roll}: {random.randint(1,6)}")

#Heads or Tails Generator:

decision = random.randint(1,2)
if decision == 1:
    print("Heads!")
elif decision == 2:
    print("Tails!")
else:
    print("Input Error!!!")


# Learning About List: 
# Lists :-

fruits = ["apple","mango","banana","coconut","Avocado"]
print(fruits)
numbers = [1,2,3,45,4856,74,23.64,86.889]
print(numbers)
print(fruits[0])
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[3])
print(states_of_america[4])
print(states_of_america[-1])  # <-- last item of the list
print(states_of_america[-2])

# Items modify in list

fruits_new = ["Cherry", "Apple", "Pear","Guava","Chiku","Watermelon"]
print(fruits_new)
fruits_new[0] = "Banana"
print(fruits_new) # <--- After Updation
fruits_new[1] = "Pineapple"
print(fruits_new)

# Add Item in the list

fruits_new.append("Papaya")
print(fruits_new)

# Add Item at specific point

fruits_new.insert(3,"Date") # <-- Insert Date at Index 3
print(fruits_new)

# Extending the list

fruits_new.extend(["Dragon Fruit","Peach","Lychee"])
print(fruits_new)

#Bank roulette :
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_pick = random.randint(1,5)
if random_pick == 1:
    print("Alice")
elif random_pick == 2:
    print("Bob")
elif random_pick == 3:
    print("Charlie")
elif random_pick == 4:
    print("David")
elif random_pick == 5:
    print("Emanuel")
else:
    print("Unknown Error!")

# Easier Way

to_pay = random.choice(friends)
print(to_pay)

# understanding Nested List:
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(len(states_of_america))
num_of_states = len(states_of_america)
print(states_of_america[num_of_states-1])

# Nested List

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Watermelon"]
vegetables = ["Potato", "Tomato", "Carrot", "Onion", "Cabbage", "Spinach"]
together = [fruits,vegetables]
print(together)
print()
print(f"Fruits: {fruits}\nVegetables: {vegetables}")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
