# function1
def validation_check(from_unit):
    while True:
        weight = input(f"What is your weight (in {from_unit}): ").strip()

        try:
            weight = float(weight)            
            return weight

        except ValueError:
            print("Invalid weight.\nPlease, enter valid weight to continue.")

# function2            
def output(result, to_unit):
    print(f"Your weight in {to_unit} is {result:.3f}")

# intro
print("Do you want to convert your weight from one to another unit?\nIf 'yes', that is the right place to do so.\nLet's start!\n")
print("There are some options:\n     1. Convert M.K.S to C.G.S\n     2. Convert C.G.S to M.K.S\n     3. Convert C.G.S to F.P.S\n     4. Convert F.P.S to C.G.S\n     5. Convert F.P.S to M.K.S\n     6. Convert M.K.S to F.P.S")
select = input("Please, select an option to continue: ")

# loop
while not select in  ["1", "2", "3", "4", "5", "6"]:

    select = input("Invalid selection. Please, select a valid option to continue: ")         

if select == "1":
    from_unit = "kg"
    to_unit = "gram"
    weight = validation_check(from_unit)
    result = weight * 1000
    output(result, to_unit)

elif select == "2":
    from_unit = "gram"
    to_unit = "kg"
    weight = validation_check(from_unit)
    result = weight * 0.001
    output(result, to_unit)        

elif select == "3":
    from_unit = "gram"
    to_unit = "pound"
    weight = validation_check(from_unit)
    result = weight * 0.00220462     
    output(result, to_unit)        

elif select == "4":
    from_unit = "pound"
    to_unit = "gram"
    weight = validation_check(from_unit)        
    result = weight * 453.592   
    output(result, to_unit)

elif select == "5":
    from_unit = "pound"
    to_unit = "kg"
    weight = validation_check(from_unit)
    result = weight * 0.453592
    output(result, to_unit)

elif select == "6":
    from_unit = "kg"
    to_unit = "pound"
    weight = validation_check(from_unit)  
    result = weight * 2.20462
    output(result, to_unit)