import sys
sys.path.append("../../jafi")
from jafi.scanner import Scanner

from pathlib import Path
import logging

def get_relative_path(path: str):
    return Path(__file__).parent.joinpath(path)



def test_all_once():    
    test_file = open(get_relative_path("test_resources/test_all_once.jafi"))
    expected_output_file = open(get_relative_path("test_resources/test_all_once_output.txt"))
    scanner = Scanner(test_file.read(), logging.ERROR)

    output = ""
    for token in scanner.scan():
        assert expected_output_file.readline() == token.__str__() + "\n"
    
