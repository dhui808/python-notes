### Add Python to path
```
C:\Users\<USER>\AppData\Local\Programs\Python\Python313
C:\Users\<USER>\AppData\Local\Programs\Python\Python313\Scripts
```

### Create and activate a virtual environment:
```
cd Project2dh
python -m venv .venv
.venv\Scripts\activate

```
### Install dependencies
```
pip install -e ../Project1dh
or
pip install -r requirements.txt

✔ This links Project1dh into Project2dh’s environment.
```

### Run Project2dh
```
python -m project2dh.main
Success!
```

### How to make Project1dh pip-installable as a wheel/distribution
```
cd Project2dh

If .venv is not created yet:
python -m venv .venv

.venv\Scripts\activate
pip install build

cd ../Project1dh
python -m build
Successfully built project1dh-0.1.0.tar.gz and project1dh-0.1.0-py3-none-any.whl

Install into another project (Project2dh)
cd ../Project2dh
pip install ../Project1dh/dist/project1dh-0.1.0-py3-none-any.whl

Run
python -m project2dh.main

```

### Using TestPyPI - distribution tool for sharing Python libraries
```
https://test.pypi.org/account/register/ to register your account
pip install twine
cd ../Project1dh

Publish (upload) project1dh to testpypi
twine upload --repository testpypi dist/*
https://test.pypi.org/project/project1dh/0.1.0/

Install (downloaf) project1dh in Project2dh
pip install -i https://test.pypi.org/simple/ project1dh

cd ../Project2dh

Run
python -m project2dh.main

```
