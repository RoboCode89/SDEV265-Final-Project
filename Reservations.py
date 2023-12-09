import sqlite3

# Guest class with last name, party size, phone number, and seated status.
class Guest:
    def __init__(self, last_name, party_size, phone_number, seated=''):
        self.last_name = last_name
        self.party_size = party_size
        self.phone_number = phone_number
        self.seated = seated

# Reservation class for guest reservation
class Reservation:
    def __init__(self, Guest):
        self.Guest = Guest
        self.db_conn = sqlite3.connect('reservation.db')
        self.db_cur = self.db_conn.cursor()
        self.db_cur.execute('''CREATE TABLE IF NOT EXISTS guests
                               (ID integer PRIMARY KEY, Last_Name text, Party_Size integer, Phone_Number text, Seated text)''')
        self.db_conn.commit()

    # Method to add a new guest reservation
    def add_reservation(self, guest_id): # connect this to Add reservation button
        self.db_cur.execute('INSERT INTO guests (ID, Last_Name, Party_Size, Phone_Number, Seated) VALUES (?, ?, ?, ?, ?)',
                            (guest_id, self.Guest.last_name, self.Guest.party_size, self.Guest.phone_number, self.Guest.seated))
        self.db_conn.commit()
    
    # Method to update the status of the party from empty string to seated.
    def update_seated_status(self, guest_id, seated): #connect this to Seat Guest button
        seated_col = 'Seated' if seated else ''
        self.db_cur.execute('UPDATE guests SET Seated = ? WHERE ID = ?', (seated_col, guest_id))
        self.db_conn.commit()

# Function to get the next available ID
def get_next_id(cursor):
    cursor.execute('SELECT MAX(ID) FROM guests')
    max_id = cursor.fetchone()[0]
    return 1 if max_id is None else max_id + 1

# Input validation for guest information
def get_guest_info(): # attach this to a button so the information can be entered in the UI
    while True:
        last_name = input("Party's last name: ")
        if not last_name.isalpha():
            print("Invalid last name! Please enter alphabetic characters only.") # make this UI element
        else:
            break

    while True:
        try:
            party_size = int(input("Party size: "))
            if party_size <= 0:
                print("Please enter a valid party size!") # make UI element
            else:
                break
        except ValueError:
            print("Incorrect input, please enter numbers only") #make UI element

    phone_number = input("Phone number: ")
    return last_name, party_size, phone_number

# Collect guest info and add a reservation
def add_guest_reservation(): # attach this function to be called when Add Reservation button is clicked
    last_name, party_size, phone_number = get_guest_info()
    guest = Guest(last_name, party_size, phone_number)
    reservation = Reservation(guest)
    
    # Get the next available ID
    next_id = get_next_id(reservation.db_cur)
    
    # Add a reservation for the guest
    reservation.add_reservation(next_id)
    print(f"Reservation added for {last_name} (Party of {party_size}).") #for testing can delete or comment out when UI implemented

    return reservation
# function to seat guest
def seat_guest(reservation): # link this function to a seat guest button when it is clicked
    while True:
        try:
            guest_id = int(input("Enter the ID of the guest to be seated: "))
            break
        except ValueError:
            print("Invalid entry, please enter a valid ID number!")
    reservation.update_seated_status(guest_id, True)
    print(f"Guest {guest_id} has been seated.")
# Call the function to start the reservation process and seat guest
reservation = add_guest_reservation() #should be activated by button click in the UI
seat_guest(reservation) #should be activated by button click in the UI
