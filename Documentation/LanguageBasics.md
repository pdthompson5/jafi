

# Expression Types


| Expression  | Description | Return Value| 
| ----------- | ----------- | ----------|
| FunctionDeclaration   | Defines the function in the current environment      | Declared function value
| Lambda | Creates an anonymous function| Function value
| VariableDeclaration   | Defines the function in the current environment         | Declared variable value 
| If-Expression   | If the condition is met, evaluates 'then' clause else it evaluates 'else' clause (None by default) |  Branch Taken
| FunctionCall   |   Calls the given function object with the given arguments    | Result of call to given function object
| Variable   |   Attempts to get the name in the current environment   | Result of environment look-up
| Literal | Evaluates the literal| Literal value  
| Grouping | Parenthesized Expression | Evaluation of inner expression


Examples:
```
#Function declaration
def foo(a){
    a
}
def bar(a, b, c){
    +(a, b)
}

#Lambda 
\x : `(x + 5)(6) #11
\x, y : `(x / y)(25, 5) #5
\z : z #<function \>

#Variable declaration
set varA = 20
set string = "this"
set function = foo

#If-Expression
if `(5 > 4)
    then "5 is greater"
    else "5 is lesser"

if True 
    then "True"

#Function Call

#declaration for clarity
def add5(a){ 
    +(a, 5)
}
add5(6) #11
set adder = add5
adder(20) #25

#Variable 

#declarations for clarity
set a = 20
set b = 60

a #20
b #60


#Literal
12 #Number
-20 
False #Bool
"This" #String 
't' #Char 

```

## Infix Function Calls
Infix function calls are not true expressions as they are de-sugared to normal FunctionCalls in the parser. Functions must have exactly two parameters to be used in an infix function call.

```
#Infix function calls
`(1 + 2)
`(200 % 10)
`(20 elem list(1, 2, 3, 20))
```



# Types
To maintain Jafi's compatibility with Python Jafi's types are nearly a subset of Python's with Some small changes 

* Number 
  * All numbers in jafi are python floats
* String (List[Char])
  * Strings in jafi are lists of characters
* Char
  * single character 
* Bool, None, List, Tuple, Dict 
  * Identical to python
* JafiFunction
  * User defined function 
* NativeFunction
  * Function built-into the language 

Examples:
```
#Number 
12 #Treated as 12.0 in the Interpreter 
-20

#String 
"string" #aka ['s', 't', 'r', 'i', 'n', 'g'] 
"" #This is an empty list, and technically also a String

#Char
'a'
'z'

# Bool
True
False

#None 
None 

#Lists, Tuples and Dicts are defined using standard-library functions
list(1, 2, 3) #[1, 2, 3]
tuple(1, 2, 3) #(1, 2, 3)
dict(tuple(1, 2), tuple(3, 4)) #{1 : 2, 3 : 4}

def foo(a){
    a 
} #<function foo>

list #<function list>

```

# Environment 
Jafi is a Lisp-1 language so functions and variables are kept in the same namespace. This was done primarily to show that functions are first-class. 

Jafi is lexically scoped with each function having its own environment with access to its enclosing environments. 
