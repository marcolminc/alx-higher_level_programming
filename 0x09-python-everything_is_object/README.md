# 0x09. Python - Everything is an Object

### Tasks
#### 0. Who am I?
Write name of the function used to get the type of an object, without ()

#### 1. Where are you?
Write name of the function that gives the identigier of a variable

#### 2. Right count
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100

#### 3. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89

#### 4. Right count =
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a

#### 5. Right count =+
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1

#### 6. Is equal
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

#### 7. Is the same
What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

#### 8. Is really equal
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

#### 9. Is really the same
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

#### 10. And with a list, is it equal
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

#### 11. And with a list, is it the same
What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

#### 12. And with a list, is it really equal
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)

#### 13. And with a list, is it really the same
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

#### 14. List append
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

#### 15. List add
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

#### 16. Integer incrementation
What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

#### 17. List incrementation
What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

#### 18. List assignment
What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

#### 19. Copy a list object
Write a function `def copy_list(l):` that returns a *copy* of a list.
- the input can contin any type of objects
- file should be maximum 3-lines long (no documentation needed)

#### 20. Tuple or not?
```Python
a = ()
```
Is `a` a tuple? Anser with `Yes` or `No`.

#### 21. Tuple or not?

```Python
a = (1, 2)
```
Is `a` a tuple? Answer with `Yes` or `No`.

#### 22. Tuple or not?
```Python
a = (1)
```
Is `a` a tuple? Answer with `Yes` or `No`.

#### 23. Tuple or not?
```Python
a = (1, )
```
Is `a` a tuple? Answer with `Yes` or `No`.

#### 24. Who I am?
What does this script print?
```Python
a = (1)
b = (1)
a is b
```

#### 25. Tuple or not
What does this script print?
```Python
a = (1, 2)
b = (1, 2)
a is b
```

#### 26. Empty is not empty
What does this script print?
```Python
a = ()
b = ()
a is b
```
#### 27. Still the same?
mandatory
Score: 0.0% (Checks completed: 0.0%)
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)


