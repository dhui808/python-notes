# my-first-py-app

A simple Python script project. This project is set up for development in Visual Studio Code.

## Execute this Python applcation from VS Code


## Execute this Python applcation from commandline
python my_firs_py_app/main.py

## Packaging the Python code as a reusable library
```
https://packaging.python.org/en/latest/guides/writing-pyproject-toml
The most common tool for this is setuptools, which works with pip to manage packages.

Step 1: Project Structure
my-awesome-package/
├── my_awesome_package/
│   ├── __init__.py
│   └── my_module.py
├── tests/
│   └── test_my_module.py
├── setup.py
└── README.md

* my-awesome-package/: This is your project's root directory.

* my_awesome_package/: This is the actual Python package directory. The name of this directory should be a valid Python identifier and what users will type in their import statement.

* __init__.py: This file makes the directory a Python package. It can be empty, but it's also a good place to expose your public API.

* setup.py: This file contains the instructions for setuptools to build and package your library.

Step 2: Create setup.py
* name: The name of your package as it will appear on PyPI.

* version: The version number of your package. Use semantic versioning (e.g., MAJOR.MINOR.PATCH).

* packages=find_packages(): This is a powerful command that automatically finds all the packages (directories with an __init__.py file) in your project.

* install_requires: A list of external libraries your package depends on.

Step 3: Create a pyproject.toml file

Step 4: Build the Package
* Install the build package: pip install build.
* pip shown build
* Install Python's package installer: pip install setuptools
* Generate a source distribution (sdist) and a wheel (bdist_wheel).

    ** python -m build --sdist creates a source distribution, which is a compressed archive of your source code.
    ** python -m build --wheel creates a wheel, which is a pre-built distribution that can be installed directly without a build step. 
    ** python -m build

These commands will create a dist/ directory containing the sdist and wheel files.

To clear previous buil:
python setup.py clean --all

Step 5: Install and Use - install your package locally to test it.
pip install dist/my_first_py_app-0.1.0-py3-none-any.whl

```

## Automated Unit Testing
```
* unittest Module: Python's built-in unittest module.
** Create test files (e.g., test_my_module.py) containing test classes that inherit from unittest.TestCase.
** Define test methods within these classes, using assert statements to check for expected outcomes.
** Run tests from the command line:
        python -m unittest discover <test_directory>
        Or:
        python -m unittest tests/test_my_module.py
```

## Run Tests from VS Code
```
Select a Test Framework:

    Open the Command Palette (Ctrl+Shift+P).
    Search for "Python: Configure Tests" and select it.
	Select a workspace
    Choose your preferred test framework (e.g., Pytest, Unittest).
    Specify the folder containing your tests.
    Select the pattern to identify test files.
```

## Publish to PyPI
```
* Create an account on PyPI (Python Package Index).
* Install twine: pip install twine.
* Upload your package using twine upload dist/*. This makes your package available for others to install via pip install your_package_name.
```

## How to use it in any Python environment
```
# In a different directory or project
import my_awesome_package

# Now you can use the functions and classes from your library

```