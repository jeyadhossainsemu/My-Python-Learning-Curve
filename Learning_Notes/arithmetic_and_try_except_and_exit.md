## step—5: Arithmetic
```python
value = 14
```
### 1. Addition
```python
value = value +1
print(value) # output 15
```
Or, 
```python
value += 1
print(value) # output: 15
```

### 2. Substitution
```python
value = value-1
print(value) # output: 13
```
Or,
```python
value -= 1
print(value) # output: 13
```

### 3. Multiplication 
```python
value = value * 2
print(value) # output: 28
```
Or, 
```python
value *= 2
print(value) # output: 28
```

### 4. Division 
```python
value = value/2
print(value) # output: 7.0
```
Or, 
```python
value /= 2
print(value) # output: 7.0
```

## step—6: try-except
```python
try:
    value = int(value)
except ValueError/TypeError/ZeroDivisionError:
    print("Invalid Message...")
```

## step—7: How to Exit the Code
`✘ Not Recommended:`
```python
exit()  
```
Or,
```python
quit()  
```
`✔ Recommended:`  
```python
import sys # important!...  
sys.exit() # best practice for 'production code'
```

***বি.দ্র.: আমরা যখন এডিটরে কোড লিখি ও রান করি, তখন সেই কোডটাকে বলে ডেভেলপমেন্ট কোড। আর যখন কোড ফাইনাল করি এবং হোস্ট করার জন্য রেডি করি তখন সেই কোডটাকে বলে প্রোডাকশন কোড।***

###### (End)