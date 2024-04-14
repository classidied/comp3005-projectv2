# comp3005-projectv2
An application in python to operate a fitness club model

## Diagrams
- [ERD Diagram](https://github.com/classidied/comp3005-projectv2/blob/main/Diagrams/ERD.svg)  
- [Relational Schema](https://github.com/classidied/comp3005-projectv2/blob/main/Diagrams/Relational%20Schema.svg)  

## Setting up the database
Table creation on database:  
```sql
create table students (
	student_id serial primary key,
	first_name text not null,
	last_name text not null,
	email text unique not null,
	enrollment_date date
)
```  

Inserting data into the database:  
```sql
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
```

## Steps to compile and run the application: 

- run `git clone https://github.com/classidied/comp3005-projectv2.git` in your terminal in a directory you'd like to download the application into
- create a virtual environment for `psycopg2` to run in by running   
1. `python3 -m venv ~/.environments/test`
2. `source ~/.environments/test/bin/activate`  
then install `psycopg2` so we can connect to the library  
3. `pip3 install psycopg2`  
- edit `script.py` to include the correct parameters according to your database (database name, host, user, port)
- to find this info, run `\conninfo` on the psql tool on pgAdmin in your database
- in the virtual environment created through the first two commands, run `python3 script.py` and run any commands you'd like  

Video demo link: https://drive.google.com/file/d/1eWkI7AWk2LUIdS_dCxjUL1Vz2eeyIWW1/view?usp=drive_link 
