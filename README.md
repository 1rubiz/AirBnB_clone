# AirBnB clone - The console
A command interpreter that serves as a backend endpoint similar to a shell using python CMD class

  - We’ll manipulate data with JSON serialization/Deserialization (First DB engine).
  - Manipulate Python packages
  - uses cmd module
  - uses the uuid module
  - args/kwargs
  - uses the datetime module

## Install

```
git clone https://github.com/1rubiz/AirBnB_clone.git

cd AirBnb_clone

```

## CMD Commands

| Command | Description | Sample Usage
| --- | --- | --- |
| Help | Show all available commands | help  |
| Quit | Exit to the prompt | quit |
| Create | Create a new object | create class |
| Show | Retrieve an object from a file | show class name id |
| All | Display all objects in class | all class |
| Update | Update objects and attributes | update class id name key |
| Destroy | Destroy specified object | destroy class |
| Count | Retrieve the number of instances of a class | class.count |


## Usage of command interpreter
Interactive Mode:
1. Run program and show prompt with help command.
```
PROMPT~> ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb)
(hbnb) quit
PROMPT~>
```
## Usage Create:
With the create command, a new instance is created

```sh
(hbnb) create BaseModel
<model id>
(hbnb)
```

## Usage All:
With the all command, all instances are displayed, returning a serialized json (string).

```sh
(hbnb) all BaseModel <model id>
["[BaseModel] (<model id>) {'id': '<model id>', 'created_at': datetime.datetime(2020, 2, 20, 9, 33, 40, 732983), 'updated_at': datetime.dat>
(hbnb)

```
 ## Usage Show:
With the show command, the instance is displayed, returning a dictionary of the id instance.

```sh
(hbnb) show BaseModel a45ac806-1c59-4392-99a4-b15327584938
[BaseModel] (<model id>) {'id': '<model id>', 'created_at': datetime.datetime(2020, 2, 20, 9, 33, 40, 732983), 'updated_at': datetime.datet>
(hbnb)

 ```
## Usage Update:
With the update command, the attributes of the instances are updated.

```sh
(hbnb) update BaseModel <model id> first_name "Emmanuel"
(hbnb) show BaseModel <model id>
[BaseModel] (<model id>) {'id': '<model id>', 'created_at': datetime.datetime(2020, 2, 20, 9, 33, 40, 732983), 'updated_at': datetime.datet>
(hbnb)

## Usage Count:
With the count command, count the number of instances.

```sh
(hbnb) BaseModel.count()
2
(hbnb)
```

## Usage Destroy:
With the Destroy command, instances are destroyed.

```sh
(hbnb) destroy BaseModel <model id>
(hbnb) show BaseModel <model id>
** no instance found **
(hbnb)

```

## non-interactive mode
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
PROMPT~>
PROMPT~> cat test_help
help
PROMPT~>
PROMPT~> cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
PROMPT~>

## Authors:
Izekor ruby - https://github.com/1rubiz
