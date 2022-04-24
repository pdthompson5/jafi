import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../jafi/')))
from scanner import Scanner


from pathlib import Path
import logging

def get_relative_path(path: str):
    return Path(__file__).parent.joinpath(path)



def test_all_once():    
    test_file = open(get_relative_path("test_resources/test_all_once.jafi"))
    expected_output_file = open(get_relative_path("test_resources/test_all_once_output.txt"))
    test_scanner = Scanner(test_file.read(), logging.ERROR)

    for token in test_scanner.scan():
        assert expected_output_file.readline() == token.__str__() + "\n"
    
