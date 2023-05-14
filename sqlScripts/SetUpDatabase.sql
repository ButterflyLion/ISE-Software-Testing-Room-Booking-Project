GRANT UNLIMITED TABLESPACE TO RBS;
GRANT UNLIMITED TABLESPACE TO SYS;

CREATE TABLE Role(
  role_id INT NOT NULL,
  u_role VARCHAR(50) CHECK(u_role IN ('student', 'faculty', 'staff', 'TA', 'admin')) NOT NULL,
  PRIMARY KEY (role_id)
);

CREATE TABLE Users(
  user_id INT NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR (100) NOT NULL,
  phone VARCHAR(50),
  role_id INT NOT NULL,
  PRIMARY KEY (user_id),
  FOREIGN KEY (role_id) REFERENCES Role(role_id)
);

CREATE TABLE RoomType(
  room_type_id INT NOT NULL,
  r_type VARCHAR(50) CHECK(r_type IN ('study desk', 'computer lab desk', 'conference room', 'classroom', 'TA space', 'meeting room')) NOT NULL,
  PRIMARY KEY (room_type_id)
);

CREATE TABLE Room(
  room_id INT NOT NULL,
  room_type INT NOT NULL,
  mincapacity INT NOT NULL,
  maxcapacity INT NOT NULL,
  room_desc VARCHAR(255) NOT NULL,
  PRIMARY KEY (room_id),
  FOREIGN KEY (room_type) REFERENCES RoomType(room_type_id)
);

CREATE TABLE RoomUserRole(
  room_user_role_id INT NOT NULL,
  user_role_id INT NOT NULL,
  room_type_id INT NOT NULL,
  PRIMARY KEY (room_user_role_id),
  FOREIGN KEY (user_role_id) REFERENCES Role(role_id),
  FOREIGN KEY (room_type_id) REFERENCES Room(room_id)
);

CREATE TABLE TimeSlot(
  time_slot_id INT NOT NULL,
  start_time TIMESTAMP NOT NULL,
  end_time TIMESTAMP NOT NULL,
  PRIMARY KEY (time_slot_id)
);

CREATE TABLE Status(
  status_id INT NOT NULL,
  b_status VARCHAR(50) CHECK(b_status IN ('active', 'cancelled')) NOT NULL,
  PRIMARY KEY (status_id)
);


CREATE TABLE Booking(
  booking_id INT NOT NULL,
  user_id INT NOT NULL,
  room INT NOT NULL,
  b_day DATE NOT NULL,
  time_slot INT NOT NULL,
  num_people INT NOT NULL,
  b_status INT NOT NULL,
  --waiting_list_id INT NOT NULL,
  PRIMARY KEY (booking_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id),
  FOREIGN KEY (room) REFERENCES Room(room_id),
  FOREIGN KEY (time_slot) REFERENCES TimeSlot(time_slot_id),
  FOREIGN KEY (b_status) REFERENCES Status(status_id)
  --FOREIGN KEY (waiting_list_id) REFERENCES WaitingList(waiting_list_id)
);