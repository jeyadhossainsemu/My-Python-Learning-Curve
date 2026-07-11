# function 
def float_convert():
    while True:
        num1 = input("Enter the 1st number: ")
        try:
            num1 = float(num1)    
            break

        except ValueError:
            print("Invalid number.")
            continue 

    while True:
        method = input("Enter the method [addition, subtraction, multiplication, division]: ").lower().strip()
        if method in ["addition", "subtraction", "multiplication", "division"]:
            break
        else:
            print("Invalid method!")
            continue

    while True:
        num2 = input("Enter the 2nd number: ")
        try:
            num2 = float(num2)            
            break

        except ValueError:
            print("Invalid number.")

    return num1, method, num2     

#start                      
print("Let's start...")
num1, method, num2 = float_convert()

if method == "addition":
    result = num1 + num2

elif method == "subtraction":
    result = num1 - num2

elif method == "multiplication":
    result = num1 * num2

elif method == "division":
    if num2 == 0:
        result = "∞"
        #print(f"The result of {method} is: {result}")
        #exit()
    else:
        result = num1 / num2

if isinstance(result, float):
    print(f"The result of {method} is: {result:.2f}")
else:
    print(f"The result of {method} is: {result}")