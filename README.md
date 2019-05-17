# WeByte
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

WeByte is a programming colosseum that allows programmers to battle against other programmers in competitive programming contests. 
This Flask based website can be used by an individual who wishes to host a competitive coding event in one's locality, school, college or university. Companies can also host this website on their servers and use it for competitive coding tests for hiring purposes, instead of using a middleman to conduct the tests.

## Features
* Webpages designed to be user friendly and intuitive.
* Excellent test coverage.
* Will work on Python 3.6 and above.
* Currently allows execution of only Python programs.
* User's data stored using SHA256 for privacy concerns.
* Authentication of user's email during signup.

## Prerequisites
* Python 3.6 or above installed on server
* A MySQL Server like [Mamp](https://www.mamp.info/en/), [Wamp](http://www.wampserver.com/en/), [Xampp](https://www.apachefriends.org/index.html) etc.

## Installing
```
$ pip install mysql-connector
$ pip install Flask
$ pip install flask-bcrypt
$ pip install Flask-Mail
$ git clone https://github.com/SaberSz/WeByte.git
```
## Usage
* Enter a valid Email ID and it's corresponding Password into the __init__.py file which is located in the __CodeArena__ folder. This is  required to for authentication of the Email entered by the user. 
* Start up your MySQL Server and import the __.sql__ file.

## Running 
Start up your MySQL Server.
```
$ cd WeByte
$ python run.py
```

## Built With
* [Python](https://www.python.org/) - The programming languaged used.
* [Flask](http://flask.pocoo.org/) - Used as a Web Framework.
* [Bootstrap](https://getbootstrap.com/) - Used for designing webpage elements.

## Authors 
* [Dylan Saldanha](https://github.com/SaberSz)
* [Abhishek Varma](https://github.com/abhishekvarma16)

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
