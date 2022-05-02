

# What is Jafi?
Jafi is a purely functional programming language that is deeply integrated with Python. Jafi files are intended to be run directly from Python.
Jafi files can be run independently; however, there would be little purpose in doing so since Jafi does not contain I/O operations. 

## Name 
Jafi -> Just a Functional Interpreter
Pronounced : "Jah Fee"


# Justification 
Jafi arose from the following factors:
* Purely functional programming languages like Haskell have incredible advantages
  * One that I sought to capture is that a function call given a specific value will always return the same value regardless of program state
* Dealing with I/O in Haskell can be quite difficult 
* Python is an exceptionally flexible tool that be used to quickly construct high-quality user interfaces 
* Python's flexibility can be a pain when trying to understand how the state of the program affects a given operation

Jafi allows for seamless interaction between Python and a purely functional programming language to capitalize on the advantages of using either approach. 

In Haskell, managing which functions are pure or impure can be difficult. With Jafi and Python, the distinction is quite simple: All Jafi programs are pure, all Python programs are impure. 

Another advantage of integrating with Python is that the Jafi language does not need to implement any I/O operations. This, in a way, allows Jafi to have less side-effects than even Haskell.

# Design Goals
Everything is a function
* My experience with writing a Lisp interpreter led me to question if nearly every aspect of a programming language could be implemented as a function
  * It turns out that it is possible, but there are reasons to implement some operations as expressions 
* An additional benefit of this is that functions such as `+` and `>` can be used with higher order functions like `map` and `filter`

Simple grammar 
* This mostly coincides with the previous design goal
  * Using functions for operations as simple as addition and subtraction leads to a small grammar 
* Smaller grammar are generally easier for users understand  

Pythonic
* Due to Jafi's close connection with Python, I endeavored to make the languages syntax similar
  * Specifically this can be seen in Lambda functions. They are virtually identical.

Pure 
* No side-effects 



# Repository structure
Jafi interpreter source code can be found at `jafi/`
`gen_ast/gen_ast.py` is a script to generate `jafi/visitor.py` and `jafi/expr.py`
All test code can be found at `tests/`
* Project tests are the following: For every directory in `tests/whole_project_tests/test_resources` execute `{test_name}/input.jafi` and ensure that the output is the same as `{test_name}/expected_output.jafi`


# Shortcomings 
Unfortunately due to a time crunch on this project a few planned aspects of the language were not thoroughly implemented 

Static Typing 
* Jafi is currently dynamically typed
* Static typing would make sense for this project as provable correctness is an intended benefit of using Jafi

Error Handling
* There is some rudimentary error handling implemented but it is not up to snuff
  * There is always an error reported when one occurs, but the description of the error may be misleading 
* There is no guarantee that the user will not receive an unhandled Python exception 