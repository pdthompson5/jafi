# from: https://stackoverflow.com/questions/5136611/capture-stdout-from-a-script
from contextlib import redirect_stdout
import os, sys
import logging 
from pathlib import Path
import pytest

import io



sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../jafi')))
from jafi.jafi import Jafi 

def get_relative_path(path: str):
    return Path(__file__).parent.joinpath(path)

test_names = os.listdir(get_relative_path("test_resources/"))


@pytest.mark.parametrize("test_name", test_names)
def test_run_file(test_name):
    jafi = Jafi(logging.ERROR, debug=True)
    

    output = io.StringIO()
    with redirect_stdout(output):
        jafi.run_file(get_relative_path(f"test_resources/{test_name}/input.jafi"))
    output_string = output.getvalue()

    expected_output = ""
    with open(get_relative_path(f"test_resources/{test_name}/expected_output.txt")) as f:
        expected_output = f.read()

    assert output_string == expected_output 
# os.listdir()


