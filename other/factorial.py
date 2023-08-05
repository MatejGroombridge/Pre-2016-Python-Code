# File: factorial.py
# A program to compute the factorial of a number.
# Illustrates: for loop with accumulator.

def main():
    print("This program calculates the factorial of a number")
    
    n = eval(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
    print("the factorial of", n, "is", fact)

main()
