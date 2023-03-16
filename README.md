# login-flask
Made a simple login system with validation using Flask as a framework in python 
# Working of these files

Install flask in a directory named my_flask_app steps given in the official documentation of flask : https://flask.palletsprojects.com/en/1.1.x/installation/

Create a virtual environment to run the flask 

# Storing data in mysql 
Once the virtual environment is created install flask_mysqldb pip in the flask directory itself
Change the username with the user
Create the database name as login 
Create a table named account in the database 'login'
* Run the query below to create the table
CREATE TABLE account(id int(50) NOT NULL PRIMARY AUTO_INCREMENT,Name VARCHAR(255) NOT NULL,age INT(10),username VARCHAR(255) NOT NULL,password VARCHAR(255)NOT NULL) 
