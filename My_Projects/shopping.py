import sys 
age = "N/A"
age_value = "N/A"
# function 1
def age_validation():
	while True:
		age = input("*Please insert your age: ")
		try:
			age = int(age)
			if 0<age < 18:
			    return age, "Child"
			elif 18<=age<=59:
			  	return age, "Adult"
			elif 60<=age<99:
				return age, "Sexagenarian"
			else:
				print(f"Really, You are {age} y/o!\nPlease contact here: 01900000000 (WhatsApp), to verify your age.")
				
		except ValueError:
			print("Invalid entry. Please try again.")


# function 2	
def product_validation():		        		
	while True:
		try:
			product = int(input("Please select one: "))
			if 1<=product<=5:
				if product == 1:
					price = 70
					product_name = "Cocacola*"
				elif product == 2:
					price = 20
					product_name = "Juice"
				elif product == 3:
					price = 10
					product_name = "Chips"
				elif product == 4:
					price = 50
					product_name = "Bread"
				elif product == 5:
					price = 100
					product_name = "Note Books"
				return product, price, product_name
				
			else:
				print("Invalid choice. Please try again with right one.")
			
		except ValueError:
			print("Invalid input. Try again with valid input")


# function 3
def next_step_validation():
	while True:
		try:
			next_step = int(input("press 1 to go next shipping page"))
			if next_step == 1:
				return next_step
			else:
				print("Please select right one.")
		except ValueError:
			print("Invalid choice. Retry.")
			
# function 4

def pay_validation(): 
		while True:
			pay_method = input("Select any one to start pay.")
			try:
				pay_method = int(pay_method)
				if pay_method == 1:
					pay_method_name = "bKash"
					return pay_method_name
				elif pay_method == 2:
					pay_method_name = "Nagad"
					return pay_method_name
				elif pay_method == 3:
					pay_method_name = "Rocket"
					return pay_method_name
				elif pay_method == 4:
					pay_method_name = "Upay"
					return pay_method_name
				else:
					print("invalid pay method selected. Please retry.")
								
			except ValueError:
				print("Wrong input. Try again.")
		
# function 5
def mobile_validation(pay_method_name):
	while True:
		method_mobile = input(f"Provide your {pay_method_name} acc numner [with 11 digit]: ")
		try:
			mobile_isdigit = method_mobile.isdigit()
			if mobile_isdigit:
				length = len(method_mobile)
				if length == 11:
					return method_mobile
				else:
					print("Invalid mobile number. Try again with valid number, please.")
					
			else:
				print("Wrong number. Please, provide right one.")
					
		except ValueError:
			print("Provide right number to go ahead.")
				
#function 6
def amount_validation(amount):
	while True:
		
		try:
			amount = int(amount)
			if 1<=amount<=10:
				return amount
			else:
				print("If you are a businessman, please contact our sell point (01700000000) to get product with cheap rate, or input again.")
				amount = input("Which amount of product(s) do you want to buy? Please write the number: [(max: 10; min: 1 (at once)]")
		except ValueError:
			print("Invalid input. Please retry.")
			amount = input("Which amount of product(s) do you want to buy? Please write the number:")
				
# func. 7
def giving_limit_check(total):
	while True:
		giving = input("How much do you want to give? [max limit 9999.99 tk]:")
		try:
			giving = float(giving)
			if 0.00<=giving <=9999.99 and giving>=total:
				
				return giving
			elif giving<=total:
				print(f"You paid less money than your total. Please try again with more money [your total is ৳{total}] :)")
		
			else:
				print("Your money crossed max limit. Please try again with less money. :)")
		except ValueError:
			print("Invalid input. Try again.")
			

# main code

print("""Hello!
Welcome to our shop!
Please start buying what you need...""")
		
		
while True: 
	is_start = input("Input '0' to 'Start' buying or input any other thing/nothing and submit to exit: ").upper().strip() == "0" 
	
	if is_start:
		print("""Which product do you want to buy:
		 1. Cocacola*
		 2. Juice 
		 3. Chips
		 4. Bread
		 5. Books
* indicates age restriction applicable""")
		while True:
			product, price, product_name = product_validation()
			if product == 1:
				age, age_value = age_validation()
				if product == 1 and age_value == "Child":
					print(" Sorry, this is not available for chlid user(s).")
					print("Please, select again.")
				else:
					print(f"You should pay {price} tk/per product") 
					next_step = next_step_validation()
					break
			else:
				print(f"You should pay {price} tk/per product")
				next_step = next_step_validation()
				break
		break									
												
	else:
		while True:
			is_exit = input("Are you sure, you want to exit this app?[Y/N]: ").lower().strip()
			if is_exit == "y":
				print("We're sorry to see you go. :(")
				sys.exit() 
			elif is_exit == "n":
				print("Ok, ensure us again please.")
				break
			else:
				print("Invalid input. Please clear your mind whether you want to exit or not.\n")

if next_step == 1:
	 amount = input("Which amount of product(s) do you want to buy? Please write the number: ")
	 amount = amount_validation(amount)
	 subtotal = price * amount
	 print (f"Your total = ৳{subtotal}")
	 deliverycharge = 50 
	 print(f"Delivery charge and website fee = ৳{deliverycharge}")
	 total = subtotal + deliverycharge
	 print (f"Your should pay total = ৳{total}")
	 print("""Let's pay. Whice way do you love to use:
		1. bKash
		2. Nagad
		3. Rocket
		4. Upay
select one pls...""")
	 pay_method_name = pay_validation()
	 mobile = mobile_validation(pay_method_name)
	 giving = giving_limit_check(total)
	 change = giving - total
	 
	 
# payment receipt 
	 print("Pay receipt: ")
	 print(f"Age: {age} y/o ({age_value})")
	 print(f"Subtotal : ৳{subtotal}")
	 print(f"Delivery charge and website fee : ৳{deliverycharge}")
	 print(f"Total: ৳{total}")
	 print(f"Paid : ৳{giving} [pay method : {pay_method_name}({mobile})]")
	 print(f"Change: ৳{change}")
	 print(f"Thanks for staying with us...")
	 
	 
	 print("*indicates age restrictions applicable.")
		