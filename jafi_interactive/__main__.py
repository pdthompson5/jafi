import sys
sys.path.append("../jafi")
import jafi
import os




a = 20
# https://stackoverflow.com/questions/1395913/how-to-drop-into-repl-read-eval-print-loop-from-python-code
def interact():
    import code
    code.InteractiveConsole(locals=globals()).interact()



interact()