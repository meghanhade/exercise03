def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2 

def divide(num1, num2):
    return num1 / num2

def square(num1):
    return num1 * num1

def cube(num1):
    return num1 * num1 * num1

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2


def main():
    # Your code goes here
    
    print "Please enter equation with operator as prefix and any two numbers"
    Equation = raw_input("> ")
    characters = Equation.split(" ")
    
    #num1 = characters[1]
    
    if len(characters) == 3:
        num1 = characters[1]
        num2 = characters[2]

        try:
            num1 = int(num1)
            num2 = int(num2)
    
        except ValueError:
        
            print "Stop being a jerk and enter a positive integer!"
    
    else:

        num1 = characters[1]

        try:
            num1 = int(num1)
    
        except ValueError:
        
            print "Stop being a jerk and enter a positive integer!"

    if characters[0] == "+":
        print add(num1, num2)
        

    elif characters[0] == "-":

        print subtract(num1, num2)

    elif characters[0] == "*":

        print multiply(num1, num2)


    elif characters[0] == "/":
       
        print divide(num1, num2)

    elif characters[0] == "square":
        
        print square(num1)  

    elif characters[0] == "cube":

        print cube(num1)

    elif characters[0] == "power": 

        print power(num1, num2)

    elif characters[0] == "%":

        print mod(num1, num2)

    else:
        print "Please enter valid operator"

if __name__ == '__main__':
    main()