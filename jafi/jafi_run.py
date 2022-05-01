import logging
import sys
from .jafi import jafi



if len(sys.argv) == 2:
    log_map = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "critical" : logging.CRITICAL,
        "error" : logging.ERROR
    }
    try:
        level = log_map[sys.argv[1]]    
    except:
        level = logging.ERROR
    jafi = jafi.Jafi(level)
else:
    jafi = jafi.Jafi(logging.ERROR)
jafi.run_file("test.jafi")

    