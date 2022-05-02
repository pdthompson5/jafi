import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from jafi.jafi import Jafi 
 

jafi = Jafi()
jafi.run_file("input.jafi")

print("noYY")
print(jafi.call_function("noYY", ["a", "b", "c"]))
print(jafi.call_function("noYY", ["a", "b", "cy"]))
print(jafi.call_function("noYY", ["xx", "ya", "zz"]))

print("\ntwo2")
print(jafi.call_function("two2", [1, 2, 3]))
print(jafi.call_function("two2", [2, 6, 11]))
print(jafi.call_function("two2", [0]))



print("\nsquare56")
print(jafi.call_function("square56", [3, 1, 4]))
print(jafi.call_function("square56", [1]))
print(jafi.call_function("square56", [2]))

