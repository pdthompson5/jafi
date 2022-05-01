import os, sys
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../jafi/')))

from jafi import Jafi

jafi_instance = Jafi(logging.ERROR)
jafi_instance.run_file("test_python_jafi.jafi")
print(jafi_instance.call_function("foo", 5))