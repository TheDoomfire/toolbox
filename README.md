# Toolbox Python Project

This project is a toolbox for Python.
It is a collection of functions, classes, decorators, etc.
That I can use in all my current and future projects.
The point is this place being well organized and have easy to understand names and code.
And having as little inputs needed as possible.
But also being really easy to add/remove/change things without destroying all my other projects from working.


## My current projects.

I have a lot of projects.
I for example regularly get data from a API url, clean it, perhaps format something to look nicer or be more machine readable.


How should I organize my folders/classes/functions etc?
## How I the project to work

I want easy ways to use everything I need in all my future projects. 
That is well organized so I can easy add/remove/change things.
It must also be easy to know what it is for.
The inputs needed for them to work must work for as much as possible.
I was thinking about having dynamic inputs and perhaps have ways to force it like using file="" etc

I currently thinking about having classes for each module.

For example I was thinking about starting off by having a Get/Reader, Cleaner, Exporter, Sorter, Time, Formatter. Classes, functions, decorators for them.

I will have a utils/config folder with a main_config.py file which I store all the settings in.
All these must work with any kind of files types, lists, objects, strings, etc. Which I will add working in time.
I want to easy use them and don't have to worry about typing in which type of data/file I have since all this information should be inside of the input used to call the class/function etc.

Get/Reader should be able to read from files, or perhaps noticing if a url is given then use a API function to get/read the data, .
Cleaner should I use to remove things from data, or add things to it.
Exporter should be able to export data to files/whatever.
Sorter should be able to sort data/other.
Time should be able to return time/date in any format. And track time for functions decorators.
Formatter should make things look nicer, like adding commas to numbers, make strings have a certain format, etc.

I want to start off by working on a function/class or whatever that can determine what the input is, that is used in all the other and future function/classes.
To make it so I only have to input whatever and the function/class will figure out what the input is and because of that how to use it.
Maybe by first by seeing what type the input is.
Then if its for example a list, then it will also see what the type is inside the list. And maybe continue doing it.
If its a string maybe see if its a path, filetype, url, python code, javascript code, a object, a list, json, csv etc.

Depending on the type, it will then perhaps return what the input is so I can use it in all my future functions/classes/decorators or whatever.

I want to then work on my Exporter that will use this inputDeterminator or whatever it should be called.
If you just give it one input like a string it understands is a JSON that it will export it as a JSON file. With perhaps a default filename and path since they have not been given.
If you give it two inputs, one is for example this string with JSON data, and the other is a path, then it will export it there as a JSON file.
If you instead choose a path and a filename, then it will export it there as a JSON file with that filename.


## TODO

Unzip files, add to strings.

**ReadData**
To read the data from a: 
- File
- URL

**Cleaner**
To remove data from:
- Strings
- Lists
- Objects

**Exporter**
To create any files

**Sorter**
To sort data.
- Example: ake a list with objects and sort them by date.
- Take a list of objects and sort them by date.

**Time**
Get time/date in any formats.
Tracking time for functions etc.


**Time Tracking Decorator**
To be used like this:
@timer
def my_function():
    time.sleep(2)  # Simulate work

my_function()  # Output: "my_function took 2.000456 seconds to run."

@timer is the name of the Time Tracking Decorator.


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