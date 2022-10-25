![image](https://user-images.githubusercontent.com/95341497/197728282-7deb3050-83ed-48e2-a76f-bd17f7cfdf3d.png)


# 0x00. AirBnB clone - The console

> This repository contains the tasks for `AirBnB clone - The console` project and a description of what each program or function does:

## Description:

This is the first step towards building a full web application: the AirBnB clone. This project lays the foundation for up-coming projects: HTML/CSS templating, database storage, API, front-end integration.
In this project, we will implement a command interpreter to manage our AirBnB objects.

The tasks help to: 
* put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (`User, State, City, Place`…) that inherit from `BaseModel`
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

### Command interpreter:
This command line program (shell) will enable us to manage the objects of the project by allowing us to:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

## Execution
The shell should work as below in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`










