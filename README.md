<div align="center">
<img src="https://i.imgur.com/RMfRyft.png" alt="simple-rest-api" height="">
</div>

Create a simple REST-API in python using Flask.

We will serve the data from [chinook.db](https://cdn.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip) as an example, and use [sqlitebrowser](https://sqlitebrowser.org/dl/) software to view database in GUI

## 💼 Requirements
- Python
- pip
- npm

## ⚙️ Installation
```py
# Install in Windows
install.bat
```

## 🏃 Run
```py
# nodemon will check for any files changes & auto restart the server
nodemon server.py
```


## 📈 `chinook.db` (sqlite3)

![](https://i.imgur.com/ULWHETj.png)


## Example

http://127.0.0.1:5000/employees/1

<div align="center">
<img src="https://i.imgur.com/ZOkIH1L.png" alt="simple-rest-api-github" height="">
</div>

----

# Methods

### `server.py`
This is the main server application

### `get.py`
Will be used to get data off the server.

### `post.py`
Post new Data to the specific Table

### `update.py`
Update the data of a particular employee

### `delete.py`
Delete the Data of an employee


# ToDo
- authentication
- something more than what it is now