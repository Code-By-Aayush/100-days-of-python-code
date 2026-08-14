import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?: "))
nr_numbers = int(input(f"How many numbers would you like?: "))
nr_symbols = int(input(f"How many symbols would you like?: "))

# Easy Level
decided_letters_list=[]
decided_number_list=[]
decided_symbol_list=[]
for letter_choice in range(1,nr_letters+1):
    decided_letters = random.choice(letters)
    decided_letters_list.append(decided_letters)
for symbol_choice in range(1,nr_symbols+1):
    decided_symbol = random.choice(symbols)
    decided_symbol_list.append(decided_symbol)
for number_choice in range(1,nr_numbers+1):
    decided_number = random.choice(numbers)
    decided_number_list.append(decided_number)

print(f"Decided Letters: {''.join(decided_letters_list)}")
print(f"Decided Numbers: {''.join(decided_number_list)}")
print(f"Decided Symbols: {''.join(decided_symbol_list)}")
final_list = decided_letters_list + decided_number_list + decided_symbol_list
easy_pwd = ''.join(final_list)
print(f"Easy Password: {easy_pwd}")

# Hard Version
final_list_2 = list(easy_pwd)
random.shuffle(final_list_2)
hard_pwd = ''.join(final_list_2)
print(f"Hard Password: {hard_pwd}")
