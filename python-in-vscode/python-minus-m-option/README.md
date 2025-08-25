### Key functionalities of python -m
```
using python -m to run a Python file, in order to add the current working directory to sys.path 
and enable relative imports.

```

### without -m option
```
Use Conda.
python src/a/b.py

Traceback (most recent call last):
  File "C:\github\python-notes\python-in-vscode\python-minus-m-option\src\a\b.py", line 1, in <module>
    import src.c.d
ModuleNotFoundError: No module named 'src'

When Python tries to import a module, it looks at the paths in sys.path
python src/a/b1.py

The directory containing b.py (the script we run) is added to sys.path. But d.py is not reachable 
from the directory a

1st solution: add project root to sys.path - b2.py
python src/a/b2.py

Relative import - must use the from ..module import something syntax - b3.py
python src/a/b3.py
Traceback (most recent call last):
  File "C:\github\python-notes\python-in-vscode\python-minus-m-option\src\a\b3.py", line 1, in <module>
    from ..c import d
ImportError: attempted relative import with no known parent package
This is not working!
If we import b3.py from another file, everything is fine:
python e.py

```

### 2nd solution: run as a module - adding the -m option
```
python -m src.a.b3  # note that we use . and not / here

With -m option:
* the __package__ variable is filled, enabling relative imports
* the directory from which Python was run (here: python-minus-m-option) is added to sys.path

```
