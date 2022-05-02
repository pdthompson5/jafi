import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from jafi.jafi import Jafi 
 

jafi = Jafi()
jafi.run_file("input.jafi")

print("doubling")
print(jafi.call_function("doubling", [1, 2, 3]))
print(jafi.call_function("doubling", [6, 8, 6, 8, -1]))
print(jafi.call_function("doubling", []))

print("\nsquare")
print(jafi.call_function("square", [1, 2, 3]))
print(jafi.call_function("square", [6, 8, -6, -8, 1]))
print(jafi.call_function("square", []))


print("\nrightDigit")
print(jafi.call_function("rightDigit", [1, 22, 93]))
print(jafi.call_function("rightDigit", [16, 8, 886, 8, 1]))
print(jafi.call_function("rightDigit", [10, 0]))


print("\naddStar")
print(jafi.call_function("addStar", ["a", "bb", "ccc"]))
print(jafi.call_function("addStar", ["hello", "there"]))
print(jafi.call_function("addStar", ["*"]))


print("\nlower")
print(jafi.call_function("lower", ["Hello", "Hi"]))
print(jafi.call_function("lower", ["AAA", "BBB", "ccc"]))
print(jafi.call_function("lower", ["KitteN", "ChocoLaTE"]))


print("\nareIn")
print(jafi.call_function("noX", ["ax", "bb", "cx"]))
print(jafi.call_function("noX", ["xxax", "xbxbx", "xxcx"]))
print(jafi.call_function("noX", ["x"]))
