#function1
def choose_validation_check(user_choose):

    while not user_choose in ["1", "2", "3", "4", "5", "6"]:
        user_choose = input("Invalid input!\nPlease, choose a valid option: ")

    #while  user_choose in ["1", "2", "3", "4", "5", "6"]:
        #return user_choose
        # or
    return user_choose

# function2
def input_validation_check(temp_type):
    while True:
       if temp_type == "K":
           temp = input(f"Enter a temperature in {temp_type}: ")

       else:
           temp = input(f"Enter a temperature in °{temp_type}: ")

       try:
           temp = float(temp)
           return temp
       except ValueError:
           print("Invalid Temperature.")

# function3
def output_show(temp_type, result):
    if temp_type == "K":
        print(f"Result: {result:.2f} {temp_type}")
    else:
        print(f"Result: {result:.2f} °{temp_type}")

# intro
print("1. Celsius to Fahrenheit\n2. Fahrenheit to Kelvin\n3. Kelvin to Celsius\n4. Celsius to Kelvin\n5. Kelvin to Fahrenheit\n6. Fahrenheit to Celsius\n")
choose = input("Choose an option: ")

choose = choose_validation_check(choose)

if choose == "1":
    from_temp = "C"
    to_temp = "F"    
    C = input_validation_check(from_temp)
    F = (C * 1.8) + 32
    result = F
    output_show(to_temp, result)
elif choose == "2":
    from_temp = "F"
    to_temp = "K"    
    F = input_validation_check(from_temp)
    K = ((F-32) * (5/9)) + 273.15
    result = K
    output_show(to_temp, result)
elif choose == "3":
    from_temp = "K"
    to_temp = "C"
    K = input_validation_check(from_temp)
    C = K - 273.15
    result = C
    output_show(to_temp, result)
elif choose == "4":
    from_temp = "C"
    to_temp = "K"    
    C = input_validation_check(from_temp)
    K = C + 273.15
    result = K
    output_show(to_temp, result)
elif choose == "5":
    from_temp = "K"
    to_temp = "F"    
    K = input_validation_check(from_temp)
    F = ((K - 273.15) * 1.8) + 32
    result = F
    output_show(to_temp, result)
elif choose == "6":
    from_temp = "F"
    to_temp = "C"
    F = input_validation_check(from_temp)
    C = (F - 32) / 1.8
    result = C
    output_show(to_temp, result)