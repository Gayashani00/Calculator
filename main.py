#TODO: Write the functions for arithmatic operations here
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Check for division by zero
    if b == 0:
        print("float division by zero")
        return None
    return a / b

def power(a, b):
    return a ** b

def reminder(a, b):
    return a % b
#These functions should cover Task 2


#-------------------------------------
#TODO: Write the select_op(choice) function here
def select_op(choice):
    if choice == '#':
        return -1  # Terminate
    elif choice == '$':
        return 0   # Reset
    elif choice in ('+', '-', '*', '/', '^', '%'):
        a = int(input("Enter first number: "))
        print(a)
        b = int(input("Enter second number: "))
        print(b)
        
        # Call the corresponding arithmetic function
        if choice == '+':
            result = add(a, b)
        elif choice == '-':
            result = subtract(a, b)
        elif choice == '*':
            result = multiply(a, b)
        elif choice == '/':
            result = divide(a, b)
        elif choice == '^':
            result = power(a, b)
        elif choice == '%':
            result = reminder(a, b)
        
        print(f"{float(a)} {choice} {float(b)} = {float(result)}")
        return 0  # Reset
    else:
        print("Unrecognized operation")
        return 0  # Reset

#This function sould cover Task 1 (Section 2) and Task 3
#End the select_op(choice) function here
#-------------------------------------
    
#This is the main loop. It covers Task 1 (Section 1)
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()