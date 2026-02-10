# Create a Flight class with seat booking functionality. 
class Flight:
    def __init__(self,flight_no,seat):
        self.flight_no=flight_no
        self.seat=seat
    def seat_book(self):
        print("Flight_no:",self.flight_no)
        print("Seat_no:",self.seat)
booking=Flight("AB13245","B15")
booking.seat_book()