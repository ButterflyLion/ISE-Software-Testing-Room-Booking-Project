INSERT INTO Role VALUES (1, 'admin');
INSERT INTO Role VALUES (2, 'staff');
INSERT INTO Role VALUES (3, 'faculty');
INSERT INTO Role VALUES (4, 'student');
INSERT INTO Role VALUES (5, 'TA');

INSERT INTO Users VALUES (1, 'William', 'Walker', '1@studentmail.ul.ie', '+353000000000', 4);
INSERT INTO Users VALUES (2, 'Mary', 'Brown', '2@studentmail.ul.ie', '+353000000001', 5);
INSERT INTO Users VALUES (3, 'James', 'Thompson', '3@staffmail.ul.ie', '+353000000002', 2);
INSERT INTO Users VALUES (4, 'Jane', 'Roberts', '4@facultymail.ul.ie', '+353000000003', 3);
INSERT INTO Users VALUES (5, 'Robert', 'Murphy', '5@adminmail.ul.ie', '+353000000004', 1);
INSERT INTO Users VALUES (6, 'Olivia', 'Johnson', '6@studentmail.ul.ie', '+353000000005', 4);
INSERT INTO Users VALUES (7, 'Michael', 'Jones', '7@studentmail.ul.ie', '+353000000006', 5);
INSERT INTO Users VALUES (8, 'Emma', 'Wilson', '8@staffmail.ul.ie', '+353000000007', 2);
INSERT INTO Users VALUES (9, 'Christopher', 'Robinson', '9@facultymail.ul.ie', '+353000000008', 3);
INSERT INTO Users VALUES (10, 'Lucia', 'Smith', '10@adminmail.ul.ie', '+353000000009', 1);
INSERT INTO Users VALUES (11, 'Luke', 'Jackson', '11@studentmail.ul.ie', '+353000000010', 4);
INSERT INTO Users VALUES (12, 'Percival', 'Connors', '12@studentmail.ul.ie', '+353000000011', 5);
INSERT INTO Users VALUES (13, 'Karol', 'Crowley', '13@staffmail.ul.ie', '+353000000012', 2);
INSERT INTO Users VALUES (14, 'Diana', 'Dunnes', '14@facultymail.ul.ie', '+353000000013', 3);
INSERT INTO Users VALUES (15, 'Ciara', 'Garcia', '15@adminmail.ul.ie', '+353000000014', 1);

INSERT INTO RoomType VALUES (1, 'study desk');
INSERT INTO RoomType VALUES (2, 'computer lab desk');
INSERT INTO RoomType VALUES (3, 'conference room');
INSERT INTO RoomType VALUES (4, 'classroom');
INSERT INTO RoomType VALUES (5, 'TA space');
INSERT INTO RoomType VALUES (6, 'meeting room');

--study desks can be booked by one person only
INSERT INTO Room VALUES (1, 1, 1, 1);
INSERT INTO Room VALUES (2, 1, 1, 1);
--computer lab desk can be booked by one person only
INSERT INTO Room VALUES (3, 2, 1, 1);
--conference room can be booked from 15 to 30 people
INSERT INTO Room VALUES (4, 3, 15, 30);
--classrooms can be booked from 30 to 50 people
INSERT INTO Room VALUES (5, 4, 30, 50);
INSERT INTO Room VALUES (6, 4, 30, 50);
INSERT INTO Room VALUES (7, 4, 30, 50);
INSERT INTO Room VALUES (8, 4, 30, 50);
--TA space can be booked by one person only
INSERT INTO Room VALUES (9, 5, 1, 1);
INSERT INTO Room VALUES (10, 5, 1, 1);
--meeting rooms can be booked from 3 to 15 people
INSERT INTO Room VALUES (11, 6, 3, 15);
INSERT INTO Room VALUES (12, 6, 3, 15);

--students can book: study desk, computer lab desk, meeting room
INSERT INTO RoomUserRole VALUES (1, 4, 1);
INSERT INTO RoomUserRole VALUES (2, 4, 2);
INSERT INTO RoomUserRole VALUES (3, 4, 6);
--TAs can book everything
INSERT INTO RoomUserRole VALUES (4, 5, 1);
INSERT INTO RoomUserRole VALUES (5, 5, 2);
INSERT INTO RoomUserRole VALUES (6, 5, 3);
INSERT INTO RoomUserRole VALUES (7, 5, 4);
INSERT INTO RoomUserRole VALUES (8, 5, 5);
INSERT INTO RoomUserRole VALUES (9, 5, 6);
--faculty can book: conference room, classroom, TA space, meeting room
INSERT INTO RoomUserRole VALUES (10, 3, 3);
INSERT INTO RoomUserRole VALUES (11, 3, 4);
INSERT INTO RoomUserRole VALUES (12, 3, 5);
INSERT INTO RoomUserRole VALUES (13, 3, 6);
--staff can book: conference room, meeting room
INSERT INTO RoomUserRole VALUES (14, 2, 3);
INSERT INTO RoomUserRole VALUES (15, 2, 6);
--admin can book everything
INSERT INTO RoomUserRole VALUES (16, 1, 1);
INSERT INTO RoomUserRole VALUES (17, 1, 2);
INSERT INTO RoomUserRole VALUES (18, 1, 3);
INSERT INTO RoomUserRole VALUES (19, 1, 4);
INSERT INTO RoomUserRole VALUES (20, 1, 5);
INSERT INTO RoomUserRole VALUES (21, 1, 6);

--no bookings yet
--INSERT INTO Booking VALUES ();

INSERT INTO Status VALUES (1, 'active');
INSERT INTO Status VALUES (2, 'cancelled');

--rooms are made available 5 mins after building opens
INSERT INTO TimeSlot VALUES (1, '08:05:00', '09:00:00');
INSERT INTO TimeSlot VALUES (2, '09:00:00', '10:00:00');
INSERT INTO TimeSlot VALUES (3, '10:00:00', '11:00:00');
INSERT INTO TimeSlot VALUES (4, '11:00:00', '12:00:00');
INSERT INTO TimeSlot VALUES (5, '12:00:00', '13:00:00');
INSERT INTO TimeSlot VALUES (6, '13:00:00', '14:00:00');
INSERT INTO TimeSlot VALUES (7, '14:00:00', '15:00:00');
INSERT INTO TimeSlot VALUES (8, '15:00:00', '16:00:00');
INSERT INTO TimeSlot VALUES (9, '16:00:00', '17:00:00');
INSERT INTO TimeSlot VALUES (10, '17:00:00', '18:00:00');
INSERT INTO TimeSlot VALUES (11, '18:00:00', '19:00:00');
INSERT INTO TimeSlot VALUES (12, '19:00:00', '20:00:00');
--rooms have to be vacated 10 mins before building closes
INSERT INTO TimeSlot VALUES (13, '20:00:00', '20:50:00');