## Pip 
To install this project via pip simply execute `pip install .` in the root directory of the repository. Executing this command in a virtual environment is recommended. The following pip dependencies are required if using this method:
* wheel
* importlib-metadata
## Running locally 
Execute `make jafi` to execute the jafi file `test.jafi`
Execute `make test` to execute the project tests 

## Executing from python
If you have pip installed jafi or just have the package added to you python import path you can execute jafi files using the following format:

test_jafi.py:
```Python
from jafi.jafi import Jafi

jafi_instance = Jafi()
jafi_instance.run_file("python_jafi.jafi")
print(jafi_instance.call_function("foo", 5))
```

python_jafi.jafi:
```
def foo(a){
    +(a, 5)
}
```


Please see `Samples/` for more detailed examples on using Jafi with Python