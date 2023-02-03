# UOCIS322 - Project 2 #

Joshua Muzi
jmuzi@uoregon.edu


#This project uses docker flask app in order to run app.py and iterate through server file requests using two port numbers 
#one being run on the docker.
#Given forbidden or file which do not reside in pages/ a error in accordance is given to the server using abort() that sends the @app
#to the next error status that corresponds and executes that error function defined in app.py
#if file is found in /paths it is returned from the hello() func and displays the found file





## Getting started

* **Go to the main directory**, and build the simple flask app image using

  ```
  docker build -t myimage .
  ```

* Run the container using

  ```
  docker run -d -p 5001:5000 myimage
  ```


## Tasks

The goal of this project is to implement a "file checking" logic, while also adding configuration reading to your Python script.

* If a file exists in `web/pages/` (i.e. `trivia.html`, any name, any extention or format) exists, transmit `200/OK` header followed by that file. If the file doesn't exist, transmit an error code in the header along with the appropriate page html in the body. You'll do this by creating error handlers. You'll also create the following two html files with the error messages:
    * `web/pages/404.html` will display "File not found!"
    * `web/pages/403.html` will display "File is forbidden!"

    ⚠️ NOTE: if a request contains illegal characters (`..` or `~`), the response should be 403.

* Update your name and email in `Dockerfile`. Update `README` with your name, info, and a brief description of the project.


## Grading Rubric

* If everything works as expected, 100 will be assigned.
* If existing pages and files are NOT handled correctly, 20 points will be docked.
* For each of the errors not handled correctly (403, and 404), 20 points will be docked.
* For each the two HTML files (`404.html` and `403.html`) not in the appropriate location, 5 points will be docked.
* If `README.md` is not updated with your name and info, 5 points will be docked.
* If `Dockerfile` doesn't contain your name and email, 5 points will be docked.
* If docker builds and runs, but does not have the expected functionalities implemented, or the server is unreachable, 20 will be assigned.
	* ⚠️ NOTE: If `app.py` does not read port number and debug mode from `credentials.ini` (or `default.ini` if not found), autograder will mark this as unreachable, as it cannot look for the correct port number.
* If docker builds, but fails to run, 15 will be assigned.
* If docker fails to build, 5 will be assigned.
* If `credentials.ini` is incorrect or not submitted, 0 will be assigned.

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.
