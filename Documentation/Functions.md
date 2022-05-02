# Functions 
Functions in Jafi are first-class. They are simply variables. Function objects can be called using the call operator: "(" arguments ")"
## Currying 
Jafi functions use a pseudo-currying process in order to create partially evaluated functions. The way that this works is that when a Jafi function receives arguments in a call expression, if it did not receive all of it's required arguments it will return a new function with the given arguments defined. Put another way, Jafi functions wait for all of their arguments to be passed before fully evaluating.

Examples of currying:
```
#Adds 5 to all elements of the list
def add5List(listA){
    map(+(5), listA) #The function '+' is curried 
}

add5List(list(1, 2, 3)) #6, 7, 8

*(15) #<function *>
```
