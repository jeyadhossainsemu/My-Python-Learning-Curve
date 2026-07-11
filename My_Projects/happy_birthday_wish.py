# happy 20 :)
import string # must for string.capwords()

while True:
    name = input("Write your name: ") 
    if name:
        name = string.capwords(name) # new to me
        print(f" Happy Birthday, {name}")
        break
    else:
        print("Please, provide your name first.")

print("             ^")      
print("         ^   |   ^")        
print("         |   |   |")
print("         |   |   |")
print("       ~~~~~~~~~~~~~~")
print("       |            |")
print("       |            |")
print("     ~~~~~~~~~~~~~~~~~~")
print("     |                |")
print("     |                |")
print("     |                |")
print("   ~~~~~~~~~~~~~~~~~~~~~~")
print("   |                    |")
print("   |                    |")
print("   |                    |")
print("   |                    |")
print("   ——————————————————————")
print("   |   Happy Birthday   |")
print("   ——————————————————————\n\n")
print(" Wish your happy life!")