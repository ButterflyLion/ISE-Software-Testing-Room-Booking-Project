INSERT INTO RBS.Role VALUES (1, 'admin');
INSERT INTO RBS.Role VALUES (2, 'staff');
INSERT INTO RBS.Role VALUES (3, 'faculty');
INSERT INTO RBS.Role VALUES (4, 'student');
INSERT INTO RBS.Role VALUES (5, 'TA');

INSERT INTO RBS.Users VALUES (1, 'William', 'Walker', '1@studentmail.ul.ie','12345', '+353000000000', 4);
INSERT INTO RBS.Users VALUES (2, 'Mary', 'Brown', '2@studentmail.ul.ie','12345' , '+353000000001', 5);
INSERT INTO RBS.Users VALUES (3, 'James', 'Thompson', '3@staffmail.ul.ie','12345' , '+353000000002', 2);
INSERT INTO RBS.Users VALUES (4, 'Jane', 'Roberts', '4@facultymail.ul.ie','12345' , '+353000000003', 3);
INSERT INTO RBS.Users VALUES (5, 'Robert', 'Murphy', '5@adminmail.ul.ie','12345' , '+353000000004', 1);
INSERT INTO RBS.Users VALUES (6, 'Olivia', 'Johnson', '6@studentmail.ul.ie','12345' , '+353000000005', 4);
INSERT INTO RBS.Users VALUES (7, 'Michael', 'Jones', '7@studentmail.ul.ie','12345' , '+353000000006', 5);
INSERT INTO RBS.Users VALUES (8, 'Emma', 'Wilson', '8@staffmail.ul.ie','12345' , '+353000000007', 2);
INSERT INTO RBS.Users VALUES (9, 'Christopher', 'Robinson', '9@facultymail.ul.ie','12345' , '+353000000008', 3);
INSERT INTO RBS.Users VALUES (10, 'Lucia', 'Smith', '10@adminmail.ul.ie','12345' , '+353000000009', 1);
INSERT INTO RBS.Users VALUES (11, 'Luke', 'Jackson', '11@studentmail.ul.ie','12345' , '+353000000010', 4);
INSERT INTO RBS.Users VALUES (12, 'Percival', 'Connors', '12@studentmail.ul.ie','12345' , '+353000000011', 5);
INSERT INTO RBS.Users VALUES (13, 'Karol', 'Crowley', '13@staffmail.ul.ie','12345' , '+353000000012', 2);
INSERT INTO RBS.Users VALUES (14, 'Diana', 'Dunnes', '14@facultymail.ul.ie','12345' , '+353000000013', 3);
INSERT INTO RBS.Users VALUES (15, 'Ciara', 'Garcia', '15@adminmail.ul.ie','12345' , '+353000000014', 1);

INSERT INTO RBS.RoomType VALUES (1, 'study desk');
INSERT INTO RBS.RoomType VALUES (2, 'computer lab desk');
INSERT INTO RBS.RoomType VALUES (3, 'conference room');
INSERT INTO RBS.RoomType VALUES (4, 'classroom');
INSERT INTO RBS.RoomType VALUES (5, 'TA space');
INSERT INTO RBS.RoomType VALUES (6, 'meeting room');

--study desks can be booked by one person only
INSERT INTO RBS.Room VALUES (1, 1, 1, 1);
INSERT INTO RBS.Room VALUES (2, 1, 1, 1);
--computer lab desk can be booked by one person only
INSERT INTO RBS.Room VALUES (3, 2, 1, 1);
--conference room can be booked from 15 to 30 people
INSERT INTO RBS.Room VALUES (4, 3, 15, 30);
--classrooms can be booked from 30 to 50 people
INSERT INTO RBS.Room VALUES (5, 4, 30, 50);
INSERT INTO RBS.Room VALUES (6, 4, 30, 50);
INSERT INTO RBS.Room VALUES (7, 4, 30, 50);
INSERT INTO RBS.Room VALUES (8, 4, 30, 50);
--TA space can be booked by one person only
INSERT INTO RBS.Room VALUES (9, 5, 1, 1);
INSERT INTO RBS.Room VALUES (10, 5, 1, 1);
--meeting rooms can be booked from 3 to 15 people
INSERT INTO RBS.Room VALUES (11, 6, 3, 15);
INSERT INTO RBS.Room VALUES (12, 6, 3, 15);

--students can book: study desk, computer lab desk, meeting room
INSERT INTO RBS.RoomUserRole VALUES (1, 4, 1);
INSERT INTO RBS.RoomUserRole VALUES (2, 4, 2);
INSERT INTO RBS.RoomUserRole VALUES (3, 4, 6);
--TAs can book everything
INSERT INTO RBS.RoomUserRole VALUES (4, 5, 1);
INSERT INTO RBS.RoomUserRole VALUES (5, 5, 2);
INSERT INTO RBS.RoomUserRole VALUES (6, 5, 3);
INSERT INTO RBS.RoomUserRole VALUES (7, 5, 4);
INSERT INTO RBS.RoomUserRole VALUES (8, 5, 5);
INSERT INTO RBS.RoomUserRole VALUES (9, 5, 6);
--faculty can book: conference room, classroom, TA space, meeting room
INSERT INTO RBS.RoomUserRole VALUES (10, 3, 3);
INSERT INTO RBS.RoomUserRole VALUES (11, 3, 4);
INSERT INTO RBS.RoomUserRole VALUES (12, 3, 5);
INSERT INTO RBS.RoomUserRole VALUES (13, 3, 6);
--staff can book: conference room, meeting room
INSERT INTO RBS.RoomUserRole VALUES (14, 2, 3);
INSERT INTO RBS.RoomUserRole VALUES (15, 2, 6);
--admin can book everything
INSERT INTO RBS.RoomUserRole VALUES (16, 1, 1);
INSERT INTO RBS.RoomUserRole VALUES (17, 1, 2);
INSERT INTO RBS.RoomUserRole VALUES (18, 1, 3);
INSERT INTO RBS.RoomUserRole VALUES (19, 1, 4);
INSERT INTO RBS.RoomUserRole VALUES (20, 1, 5);
INSERT INTO RBS.RoomUserRole VALUES (21, 1, 6);

--no bookings yet
--INSERT INTO Booking VALUES ();

INSERT INTO RBS.Status VALUES (1, 'active');
INSERT INTO RBS.Status VALUES (2, 'cancelled');

--rooms are made available 5 mins after building opens
INSERT INTO RBS.TimeSlot VALUES (1, TO_TIMESTAMP('08:00', 'HH24:MI'), TO_TIMESTAMP('09:00', 'HH24:MI'));
INSERT INTO RBS.TimeSlot VALUES (2, TO_TIMESTAMP('09:00', 'HH24:MI'), TO_TIMESTAMP('10:00', 'HH24:MI'));
INSERT INTO RBS.TimeSlot VALUES (3, TO_TIMESTAMP('10:00', 'HH24:MI'), TO_TIMESTAMP('11:00', 'HH24:MI'));
INSERT INTO RBS.TimeSlot VALUES (4, TO_TIMESTAMP('11:00', 'HH24:MI'), TO_TIMESTAMP('12:00', 'HH24:MI'));
INSERT INTO RBS.TimeSlot VALUES (5, TO_TIMESTAMP('12:00', 'HH24:MI'), TO_TIMESTAMP('13:00', 'HH24:MI'));
INSERT INTO RBS.TimeSlot VALUES (6, TO_TIMESTAMP('13:00', 'HH24:MI'), TO_TIMESTAMP('14:00', 'HH24:MI'));
INSERT INTO RBS.TimeSlot VALUES (7, TO_TIMESTAMP('14:00', 'HH24:MI'), TO_TIMESTAMP('15:00', 'HH24:MI'));
INSERT INTO RBS.TimeSlot VALUES (8, TO_TIMESTAMP('15:00', 'HH24:MI'), TO_TIMESTAMP('16:00', 'HH24:MI'));
INSERT INTO RBS.TimeSlot VALUES (9, TO_TIMESTAMP('16:00', 'HH24:MI'), TO_TIMESTAMP('17:00', 'HH24:MI'));
INSERT INTO RBS.TimeSlot VALUES (10, TO_TIMESTAMP('17:00', 'HH24:MI'), TO_TIMESTAMP('18:00', 'HH24:MI'));
INSERT INTO RBS.TimeSlot VALUES (11, TO_TIMESTAMP('18:00', 'HH24:MI'), TO_TIMESTAMP('19:00', 'HH24:MI'));
INSERT INTO RBS.TimeSlot VALUES (12, TO_TIMESTAMP('19:00', 'HH24:MI'), TO_TIMESTAMP('20:00', 'HH24:MI'));
--rooms have to be vacated 10 mins before building closes
INSERT INTO RBS.TimeSlot VALUES (13, TO_TIMESTAMP('20:00', 'HH24:MI'), TO_TIMESTAMP('21:00', 'HH24:MI'));