import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from jafi.jafi import Jafi 
 

jafi = Jafi()
jafi.run_file("input.jafi")

print("\nmath1")
print(jafi.call_function("math1", [1, 2, 3]))
print(jafi.call_function("math1", [6, 8, 6, 8, 1]))
print(jafi.call_function("math1", [10]))

print("\nmoreY")
print(jafi.call_function("moreY", ["a", "b", "c"]))
print(jafi.call_function("moreY", ["hello", "there"]))
print(jafi.call_function("moreY", ["yay"]))

print("\ncopies4")
print(jafi.call_function("copies4", ["a", "bb", "ccc"]))
print(jafi.call_function("copies4", ["24", "a", ""]))
print(jafi.call_function("copies4", ["hello", "there"]))