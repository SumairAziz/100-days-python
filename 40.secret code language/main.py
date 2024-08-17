import string
import random
import time
import os
import sys

# Generate a list of lowercase letters
lowercase_letters = list(string.ascii_lowercase)

def encode(var):
    # print("Encoding the message...")
    # time.sleep(2)
    sys.stdout.write("Encoding the message...")
    sys.stdout.flush()  # Ensure the text is written to the terminal
    time.sleep(2)  # Simulate a delay

    # Overwrite the line with spaces
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()  # Ensure the line is overwritten
    # Continue with the function logic
    if len(var) < 3:
        return var[::-1]
    else:
        var = var[1:] + var[0]
        prefix = "".join(random.choices(lowercase_letters, k=3))
        suffix = "".join(random.choices(lowercase_letters, k=3))
        return prefix + var[::-1] + suffix

def decode(var):
    sys.stdout.write("Encoding the message...")
    sys.stdout.flush()  # Ensure the text is written to the terminal
    time.sleep(2)  # Simulate a delay

    # Overwrite the line with spaces
    sys.stdout.write('\r' + ' ' * 20 + '\r')
    sys.stdout.flush()  # Ensure the line is overwritten
    # Continue with the function logic
    if len(var) < 3:
        return var[::-1]
    else:
        var = var[3:-3]
        var = var[::-1]
        return var[-1] + var[:-1]

while True:
    os.system("cls")
    process = input('Do you want to "code", "c", "decode", "d" or "exit", "e"? ')
    
    if process in ["code", "c", "decode", "d"]:
        var = input("Enter the string: ")
        
        if process in ["code", "c"]:
            coded_string = encode(var)
            print('Coded string is: "', coded_string, '"')
        elif process in ["decode", "d"]:
            decoded_string = decode(var)
            print('Decoded string is: "', decoded_string, '"')
    
    elif process in ["exit", "e"]:
        print("Exiting the program...")
        time.sleep(1)
        os.system('cls')
        break
    
    else:
        print("\nInvalid Input\n")
    
    # Ask if the user wants to continue
    again = input("Do you want to continue? 1 for Yes, 0 for No: ")
    if again != "1":
        print("Exiting the program.")
        break
