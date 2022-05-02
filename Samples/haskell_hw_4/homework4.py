import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from jafi.jafi import Jafi 
 

jafi = Jafi()
jafi.run_file("input.jafi")

print("\nnoNeg")
print(jafi.call_function("noNeg", [1, -2]))
print(jafi.call_function("noNeg", [-3, -3, 3, 3]))
print(jafi.call_function("noNeg", [-1, -1, -1]))


print("\nno9")
print(jafi.call_function("no9", [1, 2, 19]))
print(jafi.call_function("no9", [9, 19, 29, 3]))
print(jafi.call_function("no9", [1, 2, 3]))


print("\nnoTeen")
print(jafi.call_function("noTeen", [12, 13, 19, 20]))
print(jafi.call_function("noTeen", [1, 14, 1]))
print(jafi.call_function("noTeen", [15]))

print("\nnoZ")
print(jafi.call_function("noZ", ["aaa", "bbb", "aza"]))
print(jafi.call_function("noZ", ["hziz", "hzello", "hi"]))
print(jafi.call_function("noZ", ["hello", "howz", "are", "youz"]))

print("\nnoLong")
print(jafi.call_function("noLong", ["this", "not", "too", "long"]))
print(jafi.call_function("noLong", ["a", "bbb", "cccc"]))
print(jafi.call_function("noLong", ["cccc", "cccc", "cccc"]))

print("\nno34")
print(jafi.call_function("no34", ["a", "bb", "ccc"]))
print(jafi.call_function("no34", ["a", "bb", "ccc", "dddd"]))
print(jafi.call_function("no34", ["ccc", "dddd", "apple"]))