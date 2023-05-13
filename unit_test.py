import unittest
from room_booking_system import RoomBookingSystem

class TestRoomBookingSystem(unittest.TestCase):
    def setUp(self):# -> None:
        #return super().setUp()
        self.booking_system = RoomBookingSystem()

    def can_book_random_good_time(self):
        self.assertTrue(booking_system.book_room('user1', '2', 'room1', '17-05-2023', '14'))

    def can_book_l_limit_good_time(self):
        self.assertTrue(booking_system.book_room('user1', '2', 'room1', '17-05-2023', '8'))

    def can_book_u_limit_good_time(self):
        self.assertTrue(booking_system.book_room('user1', '2', 'room1', '17-05-2023', '20'))


    def cannot_book_random_bad_time(self):
        self.assertFalse(booking_system.book_room('user1', '2', 'room1', '17-05-2023', '2'))

    def can_book_l_limit_bad_time(self):
        self.assertFalse(booking_system.book_room('user1', '2', 'room1', '17-05-2023', '21'))

    def can_book_u_limit_bad_time(self):
        self.assertFalse(booking_system.book_room('user1', '2', 'room1', '17-05-2023', '7'))
        
        
    def cannot_book_same_time(self):
        self.booking_system.book_room('user1', '2', 'room1', '17-05-2023', '14')

        self.assertFalse(booking_system.book_room('user1', '2', 'room1', '17-05-2023', '14'))

    def can_book_right_before_time(self):
        self.booking_system.book_room('user1', '2', 'room1', '17-05-2023', '14')

        self.assertTrue(booking_system.book_room('user1', '2', 'room1', '17-05-2023', '13'))

    def can_book_right_after_time(self):
        self.booking_system.book_room('user1', '2', 'room1', '17-05-2023', '14')

        self.assertTrue(booking_system.book_room('user1', '2', 'room1', '17-05-2023', '15'))
