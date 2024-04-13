create table equipment (
	equipment_id serial primary key,
	equipment_name text not null,
	maintenance_period int not null,
	last_maintained_date date not null,
	maintenance_overdue boolean not null
);

create table room (
	room_id serial primary key,
	room_num int unique not null,
	booked_today boolean not null
);

create table adminStaff (
	admin_id serial primary key,
	first_name varchar(255) not null,
	last_name varchar(255) not null,
	email varchar(255) unique not null,
	passwd varchar(255) not null
);

create table trainer (
	trainer_id serial primary key,
	first_name varchar(255) not null,
	last_name varchar(255) not null,
	email varchar(255) unique not null,
	passwd varchar(255) not null
);

create table availability (
	availability_id serial primary key,
	trainer_id int not null,
	start_time timestamp not null,
	end_time timestamp not null,
	foreign key (trainer_id) references trainer
		on delete cascade
);

create table member (
	member_id serial primary key,
	email varchar(255) unique not null,
	passwd varchar(255) not null
);

create table memberProfile (
	profile_id serial primary key,
	member_id int not null unique,
	first_name varchar(255) not null,
	last_name varchar(255) not null,
	email varchar(255) unique not null,
	date_joined date default CURRENT_DATE,
	foreign key (member_id) references member
		on delete cascade
);

create table goal (
	goal_id serial primary key,
	profile_id int not null,
	goal_name varchar(255) not null,
	target_value int not null,
	foreign key (profile_id) references memberProfile
		on delete cascade
);

create table healthMetric (
	metric_id serial primary key,
	profile_id int not null,
	metric_name varchar(255) not null,
	metric_value int not null,
	foreign key (profile_id) references memberProfile
		on delete cascade
);

create table schedule (
	schedule_id serial primary key,
	member_id int default NULL,
	trainer_id int default NULL,
	foreign key (member_id) references member
		on delete cascade,
	foreign key (trainer_id) references trainer
		on delete cascade
);

create table session (
	session_id serial primary key,
	schedule_id int not null,
	trainer_id int not null,
	room_id int not null,
	session_name varchar(255) not null,
	start_time timestamp not null,
	end_time timestamp not null,
	foreign key (schedule_id) references schedule
		on delete cascade,
	foreign key (trainer_id) references trainer
		on delete cascade,
	foreign key (room_id) references room
		on delete cascade
);

create table class (
	class_id serial primary key,
	schedule_id int not null,
	room_id int not null,
	class_name varchar(255) not null,
	start_time timestamp not null,
	end_time timestamp not null,
	foreign key (schedule_id) references schedule
		on delete cascade,
	foreign key (room_id) references room
			on delete cascade
);

create table dashboard (
	dashboard_id serial primary key,
	member_id int not null unique,
	foreign key (member_id) references member
		on delete cascade
);

create table exerciseRoutine (
	routine_id serial primary key,
	dashboard_id int not null,
	routine_name varchar(255) not null,
	foreign key (dashboard_id) references dashboard
		on delete cascade
);

create table achievement (
	achievement_id serial primary key,
	dashboard_id int not null,
	achievement_name varchar(255) not null,
	foreign key (dashboard_id) references dashboard
		on delete cascade
);
