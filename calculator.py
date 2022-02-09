"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_input = input("Enter your equation > ")
    tokens = user_input.split(" ")

    if "q" in tokens:
        print("You will exit.")
        break

    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue
    
