# File: convert temprature.py
# A program that converts Celcius temprature to fahrenhiet.
# By: Matej Groombridge

def main():
    celcius = eval(input("what is the Celcius temperature?: "))
    fahrenhiet = 9/5 * celcius + 32
    print("the temprature is", fahrenhiet, "degrees fahrenhiet.")

main()
