# 0x08. Python - More Classes and Objects

### Tasks:
#### 0. Simple rectangle
An empty class `Rectangle` that defines a rectangle

#### 1. Real definition of a rectangle
A class `Rectangle` that defines a rectangle by: (based on 0-rectangle)
- private instance attr: `width`:
  - property `deef width(self):` to retrieve it
  - property setter `def width(self, value)`: to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
- private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`

#### 2. Area and Perimeter
A class `Rectangle` that defines a rectangle by: (based on 1-rectangle)
- Private instance attribute:`width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - width must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to 0, perimeter is equal to 0

#### 3. String representation
A class `Rectangle` that defines a rectangle by: (based on 2-rectangle)
- Private instance attribute:`width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - width must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to 0, perimeter is equal to 0
- `print()` and `str()` should print the rectangle with the character `#`:
  - if `width` or `height` is equal to 0, return an empty string

#### 4. Eval is magic
A class `Rectangle` that defines a rectangle by: (based on 3-rectangle)
- Private instance attribute:`width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - width must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to 0, perimeter is equal to 0
- `print()` and `str()` should print the rectangle with the character `#`:
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using eval()

#### 5. Detect instance deletion
A class `Rectangle` that defines a rectangle by: (based on 4-rectangle)
- Private instance attribute:`width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - width must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to 0, perimeter is equal to 0
- `print()` and `str()` should print the rectangle with the character `#`:
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using eval()
- Print the message `Bye rectangle...` (`...` being three dots not ellipsis) when an instance of `Rectangle` is deleted

#### 6. How many instances
A class `Rectangle` that defines a rectangle by: (based on 5-rectangle)
- Private instance attribute:`width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - width must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
  - Initialized to 0
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to 0, perimeter is equal to 0
- `print()` and `str()` should print the rectangle with the character `#`:
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using eval()
- Print the message `Bye rectangle...` (`...` being three dots not ellipsis) when an instance of `Rectangle` is deleted

#### 7. Change representation
A class `Rectangle` that defines a rectangle by: (based on 6-rectangle)
- Private instance attribute:`width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - width must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
  - Initialized to 0
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion
- Public class attribute `print_symbol`:
  - Initialized to `#`
  - used as symbol for string representation
  - can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to 0, perimeter is equal to 0
- `print()` and `str()` should print the rectangle with the character `#`:
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using eval()
- Print the message `Bye rectangle...` (`...` being three dots not ellipsis) when an instance of `Rectangle` is deleted


