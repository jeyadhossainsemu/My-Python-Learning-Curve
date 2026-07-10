## step—1: Function: print()

```python
print("Hello World!") # output: Hello World
```
## step—2: Variable Types

### 1. String: 

```python
my_name = "Jeyad Hossain"
my_class = "Six"
my_fav_sub = "Physics"
```

`Code:`
```python
print("my_name") # output: my_name  
print(my_name) # output: Jeyad Hossain 
```

`Code:`
```python
print("my_class") # output: my_class   
print(my_class) # output: Six
```

`Code:`
```python
print("my_fav_sub") # output: my_fav_sub  
print(my_fav_sub) # output: Physics
```

`Code:`
```python
print(f"My Name is {my_name}.") # output: My Name is Jeyad Hossain.  
# standard; highly recommended ✔
```

`Code:`
```python
print("I Read in Class", my_class,".") # output: I Read in Class Six .  
# comma (,) use করলে comma(,) এর স্থলে অটোমেটিক space যুক্ত হয়ে যায়
```

`Code:`
```python
print("My Favorite Subject is"+my_fav_sub+".") # output: My Favorite Subject isPhysics.  

print("My Favorite Subject is "+my_fav_sub+".") # output: My Favorite Subject is Physics.  
# plus (+) use করলে plus(+) এর স্থলে অটোমেটিক্যালি কোনো space যুক্ত হয় না, নিজেকে string এর ভিতরে space দিয়ে নিতে হয়।
```

`Code:`
```python
print("My Name is",my_name+". I Read in Class "+my_class+". My Favourite Subject is", my_fav_sub+".") # output: My Name is Jeyad Hossain. I Read in Class Six. My Favorite Subject is Physics.  
# terrible; recommended not to use at all ✘

print(f"My Name is {my_name}. I Read in Class {my_class}. My Favorite Subject is {my_fav_sub}.") # # output: My Name is Jeyad Hossain. I Read in Class Six. My Favorite Subject is Physics.  
# smooth and best practice for all ✔
```

# 2. Integer: 
```python
my_age = 20
my_sallary = 5000
```

`Code:`
```python
print(my_age) # output: 20
print("my_age") # output: my_age
```

`Code:`
```python
print(my_sallary) # output: 5000
print("my_sallary") # output: my_sallary
```

`Code:`
```python
print("I am",my_age,"Years Old and My Sallary is",my_sallary,"Taka.") # output: I am 20 Years Old and My Sallary is 5000 Taka.

print("I am"+my_age+"Years Old and My Sallary is"+my_sallary+".") # Error  
# don't use "+" to add a string with a integer, it's very dangerous! recommended not to use at all ✘

print(f"I am {my_age} Years Old and My Sallary is {my_sallary} Taka.") # output: I am 20 Years Old and My Sallary is 5000 Taka.  
# very best practice; recommended for everytime ✔
```

# 3. Float: 
```python
my_height = 5.6
my_weight = 45.80
```
```python
print(f"My Height is {my_height}m and Weight is {my_weight}kg.") # My Height is 5.6m and Weight is 45.80kg.
```

# 4. Boolean: 
```python
light_on = True
```
`Code:`
```python
if light_on:  
        print("Room Light")  
else:  
        print("Room Dark")

# output: Room Light
```
Again:
```python
light_on = False
```
`Code:`
```python
if light_on:  
        print("Room Light")  
else:  
        print("Room Dark")

# output: Room Dark
```

#### N.B.: only justify 'True'/'False'; no way to justify 'invalid input' using boolean'

---

### ➤ Some Xtra Things:  
```python
is_raining = True

if not is_raining:  # using "not"  
        print("You Can Go Outside...")        
else:  
        print("Don't Go Outside...")  

# output: Don't Go Outside...
```  
Again:
```python 
is_raining = False

if not is_raining:  # using "not"  
        print("You Can Go Outside...")        
else:  
        print("Don't Go Outside...")  

# output: You Can Go Outside...
``` 
Again:  
```python 
is_boy = 1 # '1' refers to 'True'
is_girl = 0 # '0' refers to 'False'

if is_boy:
                print("You are a Boy...")
elif is_girl:
                print("You are a Girl...")
else:
                print("Are You a Robot?...")  

# output: You are a Boy...
```

#### N.B.: 0, 0.0, None— refers to False and 1 to infinity (∞) or anything else refers to True  

---

`'True' standard — best practice ✔:` 
```python 
age = int(input("Your Age: "))        
has_nid = input("Do You Have NID [Yes/No]: ").lower() == "yes"
is_bangladeshi = input("I am a Bangladeshi.[True/False]").lower() == "true"

# make a variable: 
can_vote = (age>=18 and has_nid and is_bangladeshi)

if can_vote:
        print("Congrats...")
else:
        print("Sorry...")
```
Or,  

`'False' standard — not recommended ✘:`
```python
age = int(input("Your Age: "))        
has_nid = input("Do You Have NID [Yes/No]: ").lower() == "no"
is_bangladeshi = input("I am a Bangladeshi.[True/False]").lower() == "false"

# make a variable: 
can_vote = (age<18 or has_nid or is_bangladeshi)

if can_vote:
        print("Sorry...")
else:
        print("Congrats...")
```


###### (end)
