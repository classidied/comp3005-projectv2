# comp3005-projectv2
An application in python to operate a fitness club model

## Diagrams
- [ERD Diagram](https://github.com/classidied/comp3005-projectv2/blob/main/Diagrams/ERD.svg)  
- [Relational Schema](https://github.com/classidied/comp3005-projectv2/blob/main/Diagrams/Relational%20Schema.svg)  

## Setting up the database
- Execute the `ddl.sql` file in the SQL folder to create the database
- Execute the `dml.sql` file in the SQL folder to populate the database

## Steps to compile and run the application: 

- run `git clone https://github.com/classidied/comp3005-projectv2.git` in your terminal in a directory you'd like to download the application into
- create a virtual environment for `psycopg2` to run in by running   
1. `python3 -m venv ~/.environments/test`
2. `source ~/.environments/test/bin/activate`  
then install `psycopg2` so we can connect to the library  
3. `pip3 install psycopg2`  
- edit `main.py` to include the correct parameters according to your database (database name, host, user, port)
- to find this info, run `\conninfo` on the psql tool on pgAdmin in your database
- in the virtual environment created through the first two commands, run `python3 script.py` and run any commands you'd like  

Video demo link: https://youtu.be/8l4JVFZv0o4 
