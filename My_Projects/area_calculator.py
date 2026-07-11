import math # no need for me but...
# area: 
print("If you want to determine the area of a rectangle, please type '1'.\nIf you want to determine the area of a circle, please type '2'.\nIf you want to determine the area of a square, please type '3'.")
choose = input("Please choose a number from [1/2/3] to start: ")
while True:
        if choose == "1":
                print("Want to determine the area of a rectangle?")
                length = input("Input the length value: ").strip()
                width = input("Input the width value: ").strip()
                while True:
                        if length and width:
                                try:
                                        length = float(length)
                                        width = float(width)
                                        area_r = length * width
                                        print(f"Area of the rectangle is = {area_r:.2f}")
                                        break
                                except ValueError:
                                        print("Invalid Input.")
                                        break
                        else:
                                print("Please, provide both length and width value.")
                                length = input("Input the length value: ").strip()
                                width = input("Input the width value: ").strip()
                break
        elif choose == "2":

                print("Want to determine the area of a circle?")
                radius = input("Input the radius value: ").strip()

                while True:
                        if radius:
                                try:
                                        radius = float(radius)
                                        area_c = math.pi * radius * radius
                                        area_c = round(area_c, 2) # or can use .2f
                                        print(f"Area of the circle is = {area_c}")
                                        break
                                except ValueError:
                                        print("Invalid Input.")
                                        break
                        else:
                                print("Please, provide the radius value.")
                                radius = input("Input the radius value: ").strip()
                break
        elif choose == "3":
                print("Want to determine the area of a square?")
                length = input("Input at least side length value: ").strip()
                while True:
                        if length:
                                try: 
                                        length = float(length)
                                        area_s = length * length
                                        # or, area_s = length ** 2
                                        print(f"Area of the square is = {area_s:.2f}") # or an use round() function 
                                        break
                                except ValueError:
                                        print("Invalid Input.")
                                        break
                        else:
                                print("Please, provide the length value.")
                                length = input("Input at least one side length value: ").strip()
                break
        else:
                print("You choose wrong numnwr to input.\n Please, input valid number.")
                choose = input("Please choose a number from [1/2/3] to start: ")