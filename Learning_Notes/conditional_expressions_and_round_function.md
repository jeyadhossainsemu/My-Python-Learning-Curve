## step—8: Conditional Expressions
```python
age = 20

can_vote = "yes" if age>=18 else "no" # if-else in one line

print(can_vote)
```
But,
```python
age = 20

# can_vote =....  if....  elif.... elif.... else.... #terrible; recommended not to use at all ✘

print(can_vote)
```

## step—9: Function: round()
```python
value = 2.4 # less than 2.5
value_r = round(value) 
print(value_r) # output 2 (the previous integer number)
# x.5 theory


value = 2.6 # more than 2.5
value_r = round(value) 
print(value_r)# output 3 (the next integer number)
# x.5 theory


value = 3.5 # exact 3.5
value_r = round(value) 
print(value_r) # output 4 (the 'nearest'  even number)
# x.5 theory


value = 4.5 # exact 4.5
value_r = round(value) 
print(value_r) # output 4 (the 'nearest' even number)
# x.5 theory
```


###### (End)