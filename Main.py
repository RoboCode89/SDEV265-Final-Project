from newlogin import check_credentials_and_login
from Reservations import Guest, Reservation, get_next_id, get_guest_info, add_guest_reservation, seat_guest
from MainMenu import *
def main():
    while True:
        employee = check_credentials_and_login()
        accessMenu()
#Program is designed to run continuously and continue looping

if __name__ == "__main__":
    main()