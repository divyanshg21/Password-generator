#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input(f"How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pass_letters=[]
for i in range(0,nr_letters):
    random_letter = random.randint(0,len(letters)-1)
    pass_letters.append(letters[random_letter])
# print(pass_letters)


pass_symbols=[]
for i in range(0,nr_symbols):
   random_symbol = random.randint(0,len(symbols)-1)
   pass_symbols.append(symbols[random_symbol])
# print(pass_symbols)


pass_numbers=[]
for i in range(0,nr_numbers):
    random_number = random.randint(0,len(numbers)-1)
    pass_numbers.append(numbers[random_number])
# print(pass_numbers)


final_password=pass_letters+pass_symbols+pass_numbers
print(f"Generated password:")
print(*final_password,sep='')
      



