#  AirBnB_clone - The console
## Description
### Command interpreter to manage AirBnB objects

This is the first step towards building a first full web application: the AirBnB clone. The command interpreter in this project will be able to manage the objects of the AirBnb clone project:
-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object

The goal of this project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

![alt text](![image](https://user-images.githubusercontent.com/69390957/124124215-cb15dd00-da3d-11eb-975f-ed7789870951.png))

## Environment

This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Installation
-   Clone this repository:  `git clone "https://github.com/faykris/AirBnB_clone.git"`
- Run hbnb(interactively):  `./console`  and enter commands
- Run hbnb(non-interactively):  `echo "<command>" | ./console.py`

## File Descriptions
### `console.py`- Contains the entry point of command interpreter. Commands that this console accepts:

-   `EOF`  - exits console
-   `quit`  - exits console
-   `emptyline`  - overwrites default emptyline method and does nothing
-   `create`  - Creates a new instance of  `BaseModel`, saves it (to the JSON file) and prints the id
-   `destroy`  - Deletes an instance based on the class name and id. Save the change into the JSON file.
-   `show`  - Prints the string representation of an instance based on the class name and id.
-   `all`  - Prints all string representation of all instances based or not on the class name.
-   `update`  - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
-   `count`  - Retrieves the number of instances of a class.
-   `precmd`  - Parse the commad with the format  `<class name>.command`  to send it to the way that methods receive it.

#### `models/`  --- Directory that contains main classes:

[base_model.py]- The BaseModel class is main class where where other classes will be derived. This class gives the main attributes like id, created and updated time when a instance occurs.

Methods inside this class:

-   `def __init__(self, *args, **kwargs)`  - Initialization of the BaseModel class
-   `def __str__(self)`  - String representation of the BaseModel class
-   `def save(self)`  - Updates the attribute  `updated_at`  with the current datetime
-   `def to_dict(self)`  - returns a dictionary containing all keys and values of the instance

Classes inherited from Base Model:

-   [amenity.py]
-   [city.py]
-   [place.py]
-   [review.py]
-   [state.py]
-   [user.py]

#### `/models/engine`  --- Directory that contains File Storage class that manages JSON serialization and deserialization :

[file_storage.py]- serializes instances to a JSON file & deserializes back to instances

-   `def all(self)`  - returns the dictionary __objects
-   `def new(self, obj)`  - sets in __objects the obj with key .id
-   `def save(self)`  - serializes __objects to the JSON file (path: __file_path)
-   `def reload(self)`  - deserializes the JSON file to __objects

## Usage

### Interactive Mode

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
(hbnb)
(hbnb) quit
$

### Interactive Mode

$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) $
$
$ echo "create BaseModel" | ./console.py
(hbnb) f09bfbad-532d-4bbe-a2c1-815b1958f01e
(hbnb) $
$ echo "all" | ./console.py
(hbnb) [[BaseModel] (f09bfbad-532d-4bbe-a2c1-815b1958f01e) {'id': 'f09bfbad-532d-4bbe-a2c1-815b1958f01e', 'updated_at': datetime.datetime(2018, 6, 13, 23, 16, 30, 420332), 'created_at': datetime.datetime(2018, 6, 13, 23, 16, 30, 420300)}]
(hbnb) $
$ echo "destroy BaseModel f09bfbad-532d-4bbe-a2c1-815b1958f01e" | ./console.py
(hbnb) (hbnb) $
$ echo "all" | ./console.py
(hbnb) []
(hbnb) $
$
  
## Authors
-   Paola Carrero
-   Cristian Pinzón Capera
