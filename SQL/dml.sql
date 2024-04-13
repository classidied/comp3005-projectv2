-- populate equipment table
INSERT INTO equipment (equipment_name, maintenance_period, last_maintained_date, maintenance_overdue)
VALUES 
('chest press', 30, '2024-03-21', FALSE),
('treadmills', 15, '2024-04-05', FALSE),
('leg press', 20, '2024-03-27', FALSE),
('rowing machine', 15, '2024-03-17', TRUE),
('lateral pull down', 30, '2024-03-23', FALSE)
;

-- populate room table
INSERT INTO room (room_num, booked_today)
VALUES 
(201, FALSE),
(203, FALSE),
(204, FALSE),
(310, TRUE),
(312, FALSE),
(313, FALSE)
;

-- populate adminStaff table
INSERT INTO adminStaff (first_name, last_name, email, passwd)
VALUES
('admin', 'admin', 'admin@email.com', 'dev')
;

-- populate trainer table
INSERT INTO trainer (first_name, last_name, email, passwd)
VALUES
('Arnold', 'Schwarzenegger', 'as@email.com', 'trainer1'),
('leanbeef', 'patty', 'beef@email.com', 'trainer2'),
('Sigmund', 'Freud', 'sf@email.com', 'trainer3'),
('Alexa', 'Sharp', 'asharp@email.com', 'trainer4')
;

-- populate availability table
INSERT INTO availability(trainer_id, start_time, end_time)
VALUES
(1, '2024-04-14 15:00:00', '2024-04-14 19:00:00'),
(2, '2024-04-14 13:00:00', '2024-04-14 16:00:00'),
(1, '2024-04-15 19:00:00', '2024-04-15 22:00:00'),
(3, '2024-04-14 11:00:00', '2024-04-14 14:00:00'),
(4, '2024-04-14 09:00:00', '2024-04-14 12:00:00'),
(4, '2024-04-16 13:00:00', '2024-04-16 17:00:00'),
(3, '2024-04-15 16:00:00', '2024-04-15 19:00:00')
;
-- populate member table
INSERT INTO member (email, passwd)
VALUES
('emizzi@email.com', 'member1'),
('asharp@email.com', 'member2'),
('cjung@email.com', 'member3'),
('confucius@email.com', 'member4'),
('suntzu@email.com', 'artofwar'),
('olgaofkiev@email.com', 'birds'),
('tamino@email.com', 'sunflower'),
('angele@email.com', 'sempre')
;

-- populate memberProfile table
INSERT INTO memberProfile (first_name, last_name, member_id, email, date_joined)
VALUES
('Emily', 'Mizzi', 1, 'emizzi@email.com', '2024-01-02'),
('Alexa', 'Sharp', 2, 'asharp@email.com', '2022-03-29'),
('Carl', 'Jung', 3, 'cjung@email.com', '2022-05-19'),
('Kong', 'Zi', 4, 'confucius@email.com', '2021-03-02'),
('Sun', 'Tzu', 5, 'suntzu@email.com', '2021-03-02'),
('Olga', 'Kiev', 6, 'olgaofkiev@email.com', '2023-07-13'),
('Tamino', 'Amir', 7, 'tamino@email.com', '2024-03-28'),
('Angele', 'VanLaeken', 8, 'angele@email.com', '2024-04-02')
;

-- populate goal table
INSERT INTO goal (goal_name, target_value, profile_id)
VALUES
('num pushups by end of year', 20, 1),
('weight to bench press', 300, 2),
('dragon squat', 1, 3),
('do a flip', 1, 4),
('do 2 flips', 2, 5),
('10 sets of burning a village down', 10, 6),
('shoulder press (lbs)', 60, 6),
('mile time', 5, 7),
('num pullups by end of year', 5, 8)
;

-- populate healthMetric table
INSERT INTO healthMetric (metric_name, metric_value, profile_id)
VALUES
('height', 152, 1),
('weight', 105, 1),
('bmi', 19, 1),
('height', 160, 2),
('weight', 155, 2),
('height', 172, 3),
('weight', 160, 3),
('height', 170, 4),
('weight', 170, 4),
('bmi', 27, 4),
('height', 169, 5),
('weight', 163, 5),
('height', 167, 6),
('weight', 130, 6),
('height', 175, 7),
('weight', 146, 7),
('height', 167, 8),
('weight', 132, 8)
;
-- populate schedule table
INSERT INTO schedule (member_id, trainer_id)
VALUES
(NULL, 1),
(NULL, 2),
(NULL, 3),
(NULL, 4),
(1, NULL),
(2, NULL),
(3, NULL),
(4, NULL),
(5, NULL),
(6, NULL),
(7, NULL),
(8, NULL)
;

-- populate session table
INSERT INTO session (schedule_id, trainer_id, room_id, session_name, start_time, end_time)
VALUES
(5, 2, 3, 'Personal Training', '2024-04-14 15:00:00', '2024-04-14 16:00:00'),
(12, 2, 1, 'Personal Training', '2024-04-14 13:30:00', '2024-04-14 14:30:00'),
(8, 1, 2, 'Personal Training', '2024-04-15 19:45:00', '2024-04-15 20:45:00'),
(7, 4, 5, 'Personal Training', '2024-04-14 09:00:00', '2024-04-14 11:00:00')
;
-- populate class table
INSERT INTO class (schedule_id, room_id, class_name, start_time, end_time)
VALUES
(6, 6, 'pilates', '2024-04-14 09:00:00', '2024-04-14 10:00:00'),
(10, 6, 'pilates', '2024-04-14 09:00:00', '2024-04-14 10:00:00'),
(11, 2, 'karate', '2024-04-15 15:00:00', '2024-04-14 16:30:00')
;

-- populate dashboard table
INSERT INTO dashboard (member_id)
VALUES
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8)
;

-- populate exercise routine table
INSERT INTO exerciseRoutine (dashboard_id, routine_name)
VALUES
(1, 'ab workout'),
(2, 'dynamic stretching'),
(2, 'full body'),
(4, 'ab workout'),
(5, 'dynamic stretching'),
(6, 'dynamic stretching'),
(6, 'full body'),
(7, 'ab workout'),
(7, 'leg day'),
(8, 'ab workout'),
(8, 'dynamic stretching'),
(4, 'leg day'),
(1, 'dynamic stretching'),
(3, 'ab workout'),
(5, 'full body')
;

-- populate achievement table
INSERT INTO achievement (dashboard_id, achievement_name)
VALUES
(3, 'can bench 225'),
(2, 'can bench 225'),
(4, 'can bench 225'),
(1, '5 minute mile'),
(6, 'can bench 225'),
(5, 'martial arts master'),
(6, 'martial arts master'),
(8, '5 minute mile'),
(7, 'martial arts master')
;
