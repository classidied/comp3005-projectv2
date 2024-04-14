import psycopg2

# set up the connection to the database
connection = psycopg2.connect(
    dbname="fitnessClub",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5433"
)

cursor = connection.cursor()

# helper functions
def register_new_user():
    # ask for email and password and add them to the member database
    first_name = input("Please enter your first name: \n>> ").strip()
    last_name = input("Please enter your last name: \n>> ").strip()
    email = input("Please enter your email: \n>> ").strip()
    passwd = input("Please set a password:\n>> ").strip()
    cursor.execute("INSERT INTO member (email, passwd) VALUES ('{}', '{}');".format(email, passwd))
    # get member id
    cursor.execute("select * from member where email='{}' and passwd='{}'".format(email, passwd))
    member_record = cursor.fetchall()

    # get current date
    cursor.execute("select current_date;")
    curr_date = cursor.fetchall()

    # insert new profile record
    cursor.execute("INSERT INTO memberProfile (first_name, last_name, member_id, email, date_joined) VALUES ('{}', '{}',{}, '{}', '{}');".format(first_name, last_name, member_record[0], email, curr_date))

    print("You have been successfully registered! Please login as a member-- redirecting you to the home page...\n")

def login(table):
    email = input("Please enter your email: \n>> ").strip()
    passwd = input("Please enter your password:\n>> ").strip()
    result = ""
    cursor.execute("select * from {} where email='{}' and passwd='{}'".format(table, email, passwd))
    result = cursor.fetchall()
    if (len(result) < 1): 
        print("Something went wrong with your login. Redirecting to home...\n")
        return
    else:
        print("Logged in as {}!".format(email))
        return result[0]

def member_manage_profile(member_id, profile_info):
    print("PROFILE: \nFirst Name: {}\nLast Name: {}\nEmail: {}\nDate Joined: {}\n".format(profile_info[2], profile_info[3], profile_info[4], profile_info[5]))

    print("Please choose an option to proceed: \n")
    print("1. Update profile\n")
    print("2. Update fitness goals\n")
    print("3. Update health metrics\n")
    print("4. Go back\n")
    update_choice = input(">> ").strip()
    if (update_choice == "1"):
        member_update_profile(member_id)
    elif (update_choice == "2"):
        member_update_goals(profile_info[0])
    elif (update_choice == "3"):
        member_update_metrics(profile_info[0])
    else:
        return

def member_update_profile(member_id):
    print("Choose the field to update: \n")
    print("1. First name")
    print("2. Last name")
    print("3. Email")
    choice = input(">> ").strip()
    field = ""
    if (choice == "1"):
        field = 'first_name'
    elif (choice == "2"):
        field = 'last_name'
    else:
        field = 'email'
    print("Please enter the new value: \n")
    value = input(">> ").strip()
    if (field == 'email'):
        cursor.execute("update member set {}='{}' where member_id={};".format(field, value, member_id))
    cursor.execute("update memberProfile set {}='{}' where member_id={};".format(field, value, member_id))
    print("Successfully updated!")

def member_update_goals(profile_id):
    cursor.execute("select * from goal where profile_id={};".format(profile_id))
    goals = parse_info(cursor.fetchall())
    print("Current goals:\n")
    print(goals[2] + ": " + str(goals[3]) + "\n")
    goal_id = goals[1]

    print("Please choose an option to proceed: \n")
    print("1. Update goals\n")
    print("2. Go back\n")

    update_choice = input(">> ").strip()
    if (update_choice == "1"):
        name = input("Enter the new name for your goal: \n>> ").strip()
        val = input("Enter the new value for your goal: \n>> ").strip()
        cursor.execute("update goal set target_value={} where goal_id={};".format(val, goal_id))
        cursor.execute("update goal set goal_name='{}' where goal_id={};".format(name, goal_id))
        print("Successfully updated goals!")
    return

def member_update_metrics(profile_id):
    cursor.execute("select * from healthMetric where profile_id={};".format(profile_id))
    metrics = cursor.fetchall()
    metrics_arr = []
    for i in range(0, len(metrics)):
        metrics_arr.append(parse_info(metrics[i]))
    for m in metrics_arr:
        print(m[2] + ": " + m[3] + "\n")
    
    print("Please choose an option to proceed: \n")
    print("1. Update metrics\n")
    print("2. Go back\n")

    update_choice = input(">> ").strip()
    if (update_choice == "1"):
        metric_id = input("Enter the number of the metric you want to update: \n>> ")
        val = input("Enter the new value for your metric: \n>> ").strip()
        cursor.execute("update healthMetric set metric_value={} where metric_id={};".format(val, metric_id))
        print("Successfully updated metrics!")
    return

def member_view_dashboard(member_id, profile_id):
    dashboard_info = ""
    cursor.execute("select dashboard_id from dashboard where member_id={};".format(member_id))
    dashboard_info = parse_info(cursor.fetchall()[0])
    dashboard_id = dashboard_info[0]

    # get info from routines
    routines = ""
    cursor.execute("select routine_name from exerciseRoutine where dashboard_id={};".format(dashboard_id))
    routines = cursor.fetchall()

    # get info from achievements
    achievements = ""
    cursor.execute("select achievement_name from achievement where dashboard_id={};".format(dashboard_id))
    achievements = cursor.fetchall()

    # get info from metrics
    metrics = ""
    cursor.execute("select metric_name, metric_value from healthMetric where profile_id={};".format(profile_id))
    metrics = cursor.fetchall()

    print("DASHBOARD: \n")
    print("-> Exercise routines:\n")
    if (len(routines) < 1):
        print("No routines added!")
    else:
        for routine in routines:
            print("--> " + str(routine) + "\n")
    print("-> Achievements:\n")
    if (len(achievements) < 1):
        print("No achievements added!")
    else:
        for a in achievements:
            print("--> " + str(a) + "\n")
    print("-> Health Metrics:\n")
    if (len(metrics) < 1):
        print("No metrics added!")
    else:
        for m in metrics:
            print("--> " + str(m) + "\n")

def member_manage_schedule(member_id):
    schedule_info = ""
    cursor.execute("select schedule_id from schedule where member_id={};".format(member_id))
    schedule_info = parse_info(cursor.fetchall()[0])
    schedule_id = schedule_info[0]

    # get info from sessions
    sessions_info = ""
    cursor.execute("select session_name, trainer_id, start_time, end_time from session where schedule_id={};".format(schedule_id))
    sessions_info = parse_info(cursor.fetchall())
    trainer_name = get_trainer_name(sessions_info[1])

    # get info from classes
    classes_info = ""
    cursor.execute("select class_name, start_time, end_time from class where schedule_id={};".format(schedule_id))
    classes_info = cursor.fetchall()

    print("SCHEDULE: \n")
    print("-> Sessions:\n")
    if (len(sessions_info) < 1):
        print("No sessions added!")
    else:
        print("--> " + str(sessions_info[0]) + " led by " + trainer_name + "\n")
    print("-> Classes:\n")
    if (len(classes_info) < 1):
        print("No classes added!")
    else:
        for c in classes_info:
            print("--> " + str(c) + "\n")

def get_trainer_name(trainer_id):
    cursor.execute("select first_name, last_name from trainer where trainer_id={};".format(trainer_id))
    trainer_info = parse_info(cursor.fetchall())
    return trainer_info[0] + trainer_info[1]

def parse_info(tuple):
    # converts tuple
    str_info = str(tuple)
    # remove brackets and whitespace
    str_info = str_info.replace('(', '')
    str_info = str_info.replace(')', '')
    # strip whitespace
    str_info = str_info.strip()
    # split string to get array
    return str_info.split(",")

def trainer_view_schedule(trainer_id):
    schedule_info = ""
    cursor.execute("select schedule_id from schedule where trainer_id={};".format(trainer_id))
    schedule_info = parse_info(cursor.fetchall()[0])
    schedule_id = schedule_info[0]

    # get info from sessions
    sessions_info = ""
    cursor.execute("select session_name, trainer_id, start_time, end_time from session where schedule_id={};".format(schedule_id))
    sessions_info = parse_info(cursor.fetchall())

    print("SCHEDULE: \n")
    print("-> Sessions:\n")
    if (len(sessions_info) < 1):
        print("No sessions added!")
    else:
        print("--> " + str(sessions_info[0]) + " led by " + get_trainer_name(trainer_id) + "\n")

def trainer_add_availability(trainer_id):
    print("Here's your current availability:\n")
    availability_info = ""
    cursor.execute("select start_time, end_time from session where trainer_id={};".format(trainer_id))
    availability_info = parse_info(cursor.fetchall())

    for i in range(0, len(availability_info), 2):
        print("Available from " + availability_info[i] + " until " + availability_info[i+1] + "\n")

    print("Please choose an option to proceed: \n")
    print("1. Add availability\n")
    print("2. Go back\n")

    add_choice = input(">> ").strip()
    if (add_choice == "1"):
        start_time = input("Enter the start time for your new availability: \n>> ").strip()
        end_time = input("Enter the end time for your new availability: \n>> ").strip()
        cursor.execute("INSERT INTO availability (trainer_id, start_time, end_time) VALUES ({}, '{}', '{}');".format(trainer_id, start_time, end_time))

        print("Successfully added availability!")
    return

def trainer_view_user_profiles():
    search_name = input("Enter a name: \n>> ").strip()
    cursor.execute("select * from memberProfile where first_name='{}';".format(search_name))
    results = parse_info(cursor.fetchall()[0])
    print("PROFILE: \nFirst Name: {}\nLast Name: {}\nEmail: {}\nDate Joined: {}\n".format(results[2], results[3], results[4], results[5]))

def admin_manage_room_bookings():
    print()

def admin_manage_equipment():
    print()

def admin_update_classes():
    print()

def admin_manage_bills():
    print()

while (1):
    # greet user + ask them to enter which type of user they are for login
    print("Welcome to Movati Athletics!\n Please enter an option (1, 2, 3, 4, 5) to proceed: \n")
    print("1. Register as a new member")
    print("2. Existing Member Login")
    print("3. Trainer Login")
    print("4. Admin Login")
    print("5. Exit system")

    login_req = input(">> ").strip()

    if (login_req == "5"):
        print("Thanks for stopping by!\n")
        break
    elif (login_req == "1"):
        register_new_user()
        continue
    elif (login_req == "2"):
        member_info = login('member')
        member_arr = parse_info(member_info)
        member_id = int(member_arr[0])
        result = ""
        cursor.execute("select * from memberProfile where member_id={};".format(member_id))
        result = cursor.fetchall()
        profile_info = parse_info(result[0])
        profile_id = profile_info[0]
        while (1):
            print("Please choose from the following options (1, 2, 3, 4): \n")
            print("1. Manage Profile")
            print("2. Display Dashboard")
            print("3. Manage Schedule")
            print("4. Exit system")

            req = input(">> ").strip()

            if (req == "1"):
                member_manage_profile(member_id, profile_info)
            elif (req == "2"):
                member_view_dashboard(member_id, profile_id)
            elif (req == "3"):
                member_manage_schedule(member_id)
            else:
                break
    elif (login_req == "3"):
        trainer_info = login('trainer')
        print("trainer_info " + str(trainer_info))
        trainer_arr = parse_info(trainer_info)
        print("trainer_arr: " + str(trainer_arr))
        trainer_id = int(trainer_arr[0])
        while (1):
            print("Please choose from the following options (1, 2, 3, 4): \n")
            print("1. View Schedule")
            print("2. Add Availability Times")
            print("3. View Member Profiles")
            print("4. Exit system")

            req = input(">> ").strip()

            if (req == "1"):
                trainer_view_schedule(trainer_id)
            elif (req == "2"):
                trainer_add_availability(trainer_id)
            elif (req == "3"):
                trainer_view_user_profiles()
            else:
                break
    elif (login_req == "4"):
        admin_info = login('adminStaff')
        admin_arr = parse_info(str(admin_info))
        while (1):
            print("Please choose from the following options (1, 2, 3, 4, 5): \n")
            print("1. Manage Room Booking")
            print("2. Manage Equipment")
            print("3. Update Classes")
            print("4. Manage Billing")
            print("5. Exit system")

            req = input(">> ").strip()

            if (req == "1"):
                admin_manage_room_bookings()
            elif (req == "2"):
                admin_manage_equipment()
            elif (req == "3"):
                admin_update_classes()
            elif (req == "4"):
                admin_manage_bills()
            else:
                break
    else:
        print("Invalid input, please try again\n")

cursor.close()
connection.close()

