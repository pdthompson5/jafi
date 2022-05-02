# Arithmetic 
| Function     | Description | Return Value|
| ----------- | ----------- | -----------|
| +(a, b)      | Addition       | a + b|
| -(a, b)   | Subtraction       | a - b|
| *(a, b)      | Multiplication       | a * b|
| /(a, b)  | Division        | a / b|
| %(a, b)      | Remainder       | a % b|

# Comparisons
| Function     | Description | Return Value|
| ----------- | ----------- | -----------|
| >(a, b)  | Greater Than        | a > b|
| >=(a, b)    | Greater Than Equal      | a >= b|
| <(a, b)   | Less Than        | a < b|
| <=(a, b)     | Less Than Equal        | a <= b|
| eq(a, b)   | Equal         | a == b|
| not_eq(a, b)     | Not Equal       | a != b|

# Logical Operators
| Function     | Description | Return Value|
| ----------- | ----------- | -----------|
| not(a)   | Not        | !a |
| and(a, b)      | And       | a and b|
| or(a, b)   | Or     | a or b|

# Data structure constructors
| Function     | Description | Return Value|
| ----------- | ----------- | -----------|
| list(a...z)      | Creates list out of arguments       | list of arguments  |
| tuple(a...z)   | Creates tuple out of arguments        | tuple of arguments|
| dict(a: tuple ...z)     |  Takes pairs(tuples of length 2)      | dict of {a[0]: a[1]...}|

# Data structure management 
| Function     | Description | Return Value|
| ----------- | ----------- | -----------|
| head(a)   |         | First Element of list|
| tail(a)      |       | List with first element removed|
| index(a : list/tuple, b)  |   Get element at index      | a[b]|
| look_up(a : dict, b)      | Get value for key b       | a[b]|
| cons(a, b : list)   | Prepend to list        | [a] + b|
| elem(a, b)     | Determine if a is in b      | a in b|
| len(a: List/Tuple)   | Get length of List        | len(a)|

# Higher Order Functions
For examples of these functions in use please see the haskell homework tests
| Function     | Description | Return Value|
| ----------- | ----------- | -----------|
| map(a: function, b: List)      | Creates a new list by applying a to every element of the list       | New list|
| filter(a: function, b: List)   | Creates a new list including elements that satisfy a        | Filtered list|
| reduce(a, b: function, c: List)      | Iterate through list applying b to each element and add output to a       | Reduce Value|
| compose(a: function...z: function)   | Combines the given functions as in compose(f, g) -> f(g)         | Composite Function|

# Misc
| Function     | Description | Return Value|
| ----------- | ----------- | -----------|
| to_lower(a: Char)      | Converts to lower case      | Lower-case char|
| Paragraph   | Text        | |
| Header      | Title       | |
| Paragraph   | Text        | |
| Header      | Title       | |
| Paragraph   | Text        | |
| Header      | Title       | |
| Paragraph   | Text        | |
| Header      | Title       | |
| Paragraph   | Text        | |
