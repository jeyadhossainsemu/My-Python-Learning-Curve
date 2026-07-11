import math # generally no need for me but...

# intro
print("If you want to determine the area of a rectangle, please type '1'.\nIf you want to determine the area of a circle, please type '2'.\nIf you want to determine the area of a square, please type '3'.")
choose = input("Please choose a number from [1/2/3] to start: ")

# function 
def validation_check(variable):
    while True:
        value = input(f"Input {variable}: ").strip()
        try:
             value = float(value)
             if value>0:
                 return value
             else:
                 print("Invalid input.")
        except ValueError:
             print(f"Invalid {variable}")          
# loop          
while True: # check validation 
    if choose == "1":
        print("Want to determine the area of a rectangle?")

        length = validation_check("length")
        width = validation_check("width")

        area_r = length * width
        print(f"Area of the rectangle is = {area_r:.2f}")
        break   

    elif choose == "2":

        print("Want to determine the area of a circle?")

        radius = validation_check("radius")

        #area_c = math.pi * radius * radius
        #area_c = math.pi * pow(radius, 2)
        area_c = math.pi * radius**2
        area_c = round(area_c, 2) # or can use :.2f
        print(f"Area of the circle is = {area_c}")
        break        

    elif choose == "3":
        print("Want to determine the area of a square?")

        length =  validation_check("length")

        area_s = pow(length, 2)      
        # or, area_s = length * length
        # or, area_s = length ** 2

        print(f"Area of the square is = {area_s:.2f}") # or can use round() function 
        break

    else:
        print("You choose wrong number to input.\n Please, input valid number.")
        choose = input("Please choose a number from [1/2/3] to start: ")