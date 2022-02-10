"""CLI application for a prefix-notation calculator."""

#wish list

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
                        
print("Welcome to the calculator! This calculator uses prefix notation. Type the operator first, and the operand(s) second.")
print("Operator options are: +, -, *, /, pow, mod, square, cube.")
print("Press q to quit.")
possible_operations_single_arg = ['square', 'cube']
possible_operations_multiple_arg = ['+', '-', 'pow', '*', '/', 'mod']


# while true, keep runnning condition in the while loop:
while True:
    user_input = input("Enter your equation > ")
    tokens = user_input.split(" ")
    
    #check for user wanting to quit first
    if "q" in tokens:
        print("You will exit.")
        break

    #if user chooses a random operator that doesn't exist
    if tokens[0] not in possible_operations_multiple_arg and tokens[0] not in possible_operations_single_arg:
        print("Not a valid operation, please choose from operator options.")
        continue
    
    # if tokens length is less than 2, return an error
    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue

    #if operator is not square or cube, need more operands
    elif tokens[0] not in possible_operations_single_arg and len(tokens) < 3:
        print("Need more operands, please try again")
        continue
    
    else:
        try:
            # if user inputs add operator, call add function
            if tokens[0] == '+':
                print(add(float(tokens[1]), float(tokens[2])))
            
            # if user inputs subtract operator, call subtract function
            elif tokens[0] == '-':
                print(subtract(float(tokens[1]), float(tokens[2])))
            
            # if user inputs multiply operator, call multiply function
            elif tokens[0] == '*':
                print(multiply(float(tokens[1]), float(tokens[2])))
            
            # if user inputs divide operator, call divide function
            elif tokens[0] == '/':
                print(divide(float(tokens[1]), float(tokens[2])))
            
            # if user inputs modulo operator, call mod function
            elif tokens[0] == 'mod':
                print(mod(float(tokens[1]), float(tokens[2])))

            # if user inputs square operator, call square function
            elif tokens[0] == 'square':
                print(square(float(tokens[1])))

            # if user inputs cube operator, call cube function
            elif tokens[0] == 'cube':
                print(cube(float(tokens[1])))

            # if user inputs pow operator, call power function
            elif tokens[0] == 'pow':
                print(power(float(tokens[1]), float(tokens[2])))
                
        #will only trigger if they try to put anything not convertible to a number in the operands      
        except ValueError:
            print("Please check your operands. They must be numbers.")
            continue
