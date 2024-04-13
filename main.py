import psycopg2

# set up the connection to the database
connection = psycopg2.connect(
    dbname="assignment3q1",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5433"
)

cursor = connection.cursor()

# greet user + show commands they can use
print("Welcome to another generic PostgresSQL database requester(?)!\n The application functions are as follows: \n")
print("-> getAllStudents()")
print("-> addStudent(first_name, last_name, email, enrollment_date)")
print("-> updateStudentEmail(student_id, new_email)")
print("-> deleteStudent(student_id)")
print("-> exit(): leave the program\n")

while (1):
    request = input(">> ").strip()
    split_req = request.replace(")", "").split("(")
    command = split_req[0]
    
    # addStudent(c, w, a, 2023-01-10)
    args = []
    if (len(split_req) > 1):
        args = split_req[1].replace(" ", "").split(",")

    results = ""
    # execute the proper SQL query given the function
    if (request == "getAllStudents()"):
        cursor.execute("select * from students;")
        results = cursor.fetchall()
    elif (command == "addStudent"):
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{}', '{}', '{}', '{}');".format(args[0], args[1], args[2], args[3]))
    elif (command == "updateStudentEmail"):
        cursor.execute("update students set email='{}' where student_id={};".format(args[1], int(args[0])))
    elif (command == "deleteStudent"):
        cursor.execute("delete from students where student_id = {};".format(int(args[0])))
    elif (request == "exit()"):
        print("Bye!!")
        break
    else:
        print("Invalid command")

    # printing results
    if (results != ""):
        for record in results:
            print(record)
    else:
        print("No records returned")    

cursor.close()
connection.close()