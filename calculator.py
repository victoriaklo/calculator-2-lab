"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
#print explicit description of how to notate the operations
#possible_operations = ['+', '-', 'pow', etc...]
#if tokens[0] not in possible_operations:
    #try again

# Replace this with your code
while True:
    user_input = input("Enter your equation > ")
    tokens = user_input.split(" ")

    if "q" in tokens:
        print("You will exit.")
        break

    # elif len(tokens) < 2:
    #     print("Not enough inputs.")
    #     continue
    
    elif tokens[0] == '+':
        print(add(float(tokens[1]), float(tokens[2])))
    
    elif tokens[0] == '-':
        print(subtract(float(tokens[1]), float(tokens[2])))

    elif tokens[0] == '*':
        print(multiply(float(tokens[1]), float(tokens[2])))
    
    elif tokens[0] == '/':
        print(divide(float(tokens[1]), float(tokens[2])))
    
    elif tokens[0] == 'mod':
        print(mod(float(tokens[1]), float(tokens[2])))

    elif tokens[0] == 'square':
        print(square(float(tokens[1])))

    elif tokens[0] == 'cube':
        print(cube(float(tokens[1])))

    elif tokens[0] == 'pow':
        print(power(float(tokens[1]), float(tokens[2])))

