import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from jafi.jafi import Jafi 
 

jafi = Jafi()
jafi.run_file("input.jafi")

print("\nisSorted")
print(jafi.call_function("isSorted", [1, 2, 3]))
print(jafi.call_function("isSorted", [1, 3, 2]))
print(jafi.call_function("isSorted", [3, 2, 1]))
print(jafi.call_function("isSorted", []))


print("\nareSorted")
print(jafi.call_function("areSorted", [[1, 2, 3], [], [3, 2, 1]]))
print(jafi.call_function("areSorted", [[45, 26, 1], [78, 23, 43, 76]]))
print(jafi.call_function("areSorted", [[]]))

print("\nisIn")
print(jafi.call_function("isIn", 5, [1, 5, 3, 2]))
print(jafi.call_function("isIn", 0, []))
print(jafi.call_function("isIn", 25, [20, 50 , 234, 24]))

print("\nareIn")
print(jafi.call_function("areIn", [1, 2, 3], [1, 4, 5, 2, 5, 3]))
print(jafi.call_function("areIn", [], []))
print(jafi.call_function("areIn", [1, 2, 3], [4, 5, 2, 5, 3]))