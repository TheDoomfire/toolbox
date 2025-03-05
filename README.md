# template-python
Template for python projects. Not completed


## Installations
Installing the project. Everything you need here.

### Template TODO

Create my own libraries and import them.
Make a utils folder with a config.py.


Perhaps looks for other ways to do a virtual enviroment + requirements file.

1. Create automatic .venv activation.
1. Create automatic requirements file.
1. Create a default module. So it's easier to understand how a module works.
1. Create a setup.py

1. If folder is empty, create a __init__.py file.
1. Automatically add inside __all__ = ['module1', 'module2'] for every file inside the folder.

### Virtual environment 
1. Create a venv `python -m venv .venv` <!-- Name the folder whatever you want. -->
1. Activate it
- **Win**: `source .venv/Scripts/activate`
- **Mac**: `source .venv/bin/activate`

### Requirements

`pip freeze > requirements.txt` - Create the requirements.txt
`pip install -r requirements.txt` - Installs it.