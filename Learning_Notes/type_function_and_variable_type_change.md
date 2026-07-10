## step—3: Function: type()  
```python
name = "jeyad" # string (str)
age = 20 # integer
gpa = 4.79 # float
is_student = True # boolean
```
#### N.B.: use 'type()' function to see the data type of variable(s)

```python
print(name) # output: jeyad
print(type(name)) # output: <class 'str'>
```

Or,  

```python
data_type = type(name)
print(data_type) # output: <class 'str'>
```

```python
print(age) # output: 20
print(type(age)) # output: <class 'int'>
```

```python
print(gpa) # output: 4.79
print(type(gpa)) # output: <class 'float'>
```

```python
print(is_student) # output: True
print(type(is_student)) # output: <class 'bool'>
```

## Step–4: Variable Type Change
### 1. integer to float
```python
age_f = float(age)  
print(age_f) # output: 20.0  
print(type(age_f))  
```

### 2. integer to string
```python
age_s = str(age)
print(age_s) # output: 20
print(type(age_s))
```

### 3. integer to boolean
```python
age_b = bool(age)
print(age_b) # output: True
print(type(age_b))
```

### 4. float to integer 
```python
gpa_i = int(gpa)
print(gpa_i) # output: 4
print(type(gpa_i))
```

### 5. float to string
```python
gpa_s = str(gpa)
print(gpa_s) # output: 4.79
print(type(gpa_s))
```

### 6. float to boolean
```python
gpa_b = bool(gpa)
print(gpa_b) # output: True
print(type(gpa_b))
```

### 7. string to boolean
```python
name_b = bool(name)
print(name_b) # output: True
print(type(name_b))
```

### 8. string to integer
```python
username = "1234" # important!...
print(type(username)) # output: <class 'str'>
username_i = int(username)
print(username_i) # output: 1234
print(type(username_i))
```
But,
```python
name_i = int(name) # Error
```

### 9. string to float
```python
username = "1234" # important!...
print(type(username)) # output: <class 'str'>
username_f = float(username)
print(username_f) # output: 1234.0
print(type(username_f))
```
But,
```python
name_f = float(name) # Error
```

### 10. boolean to string
```python
is_student_s = str(is_student)
print(is_student_s) # output: True
print(type(is_student_s))
```

### 11. boolean to int
```python
is_student_i = int(is_student)
print(is_student_i) # output: 1
print(type(is_student_i))
```

### 12. boolean to float
```python
is_student = False
is_student_f = float(is_student)
print(is_student_f) # output: 0.0
print(type(is_student_f))
```


###### (End)