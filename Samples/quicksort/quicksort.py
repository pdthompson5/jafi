import sys, os, random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from jafi.jafi import Jafi 
 
randomlist = [random.randint(1, 100) for x in range(0, 20)]
randomlist2 = [random.randint(1, 10000) for x in range(0, 20)]

jafi = Jafi()
jafi.run_file("input.jafi")


print(jafi.call_function("quicksort", [1, 2, 3]))
print(jafi.call_function("quicksort", [1, 3, 2]))
print(jafi.call_function("quicksort", []))
print(jafi.call_function("quicksort", randomlist))
print(jafi.call_function("quicksort", randomlist2))