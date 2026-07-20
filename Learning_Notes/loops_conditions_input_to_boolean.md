## step—10: for loop  
```Structure: ```
```python
for i in range(5):   # when variable 'i' need to use later

    print(f"Output ({i+1}): Hello World!")  # here we need 'i' to print
```
```
# output: 
Output (1): Hello World!
Output (2): Hello World!
Output (3): Hello World!
Output (4): Hello World!
Output (5): Hello World!
```
Again,
```python
for _ in range(5):   # when variable 'i'/anything don't need to use later, then you can use '_'(underscore)

    print("Hello World!")  # here we don't need 'i'/any variable to print/use
```
```
# output:
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
```

## step—11: while loop  
```python
age = int(input("How old are you: "))
while age < 18:
    print("You are under 18.")
    age = int(input("How old are you: "))
```
Or,
```python
while True:
    age = int(input("How old are you: "))
    if age < 18:
         print("You are under 18.")
         break
```

## step—12: if-elif-else
```python
age = int(input("How old are you: "))
if age < 18:
    print("You are under 18.")
elif age == 18:
    print("You are 18.")
elif 18 < age < 60:
    print("You are over 18 and under 60.")
else:
    print("You are 60 or older.")
```

## step—13: input to boolean
```python
has_nid = input("Do You Have NID?").lower().strip() == "yes" # if user(s) input 'yes', has_nid = True; otherwise, has_nid = False
```
Or,
```python
# creat a temporary variable named userinput
userinput = input("Do You Have NID?").lower().strip()
has_nid = userinput in ["yes", "y", "true","t"]
# if userinput is among ["yes", "y", "true", " t"], has_nid = True; otherwise, has_nid = False
```
Or, 
```python
has_nid = input("Do You Have NID?").lower().strip() in ["yes", "y", "true","t"] 
# 'in' use to test from a group of inputs; if user(s) input any of [" yes", "y", " true", "t"], then has_nid = True; otherwise,  has_nid = False
```


###### (End)