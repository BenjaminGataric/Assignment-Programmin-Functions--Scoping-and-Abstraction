'''
Program Name: 
Description: 
Authors: Ben Gataric, Vincent Ruiyang Li, Lelandi Calil De Assis, Devon Huynh 
Date: 

'''
import os
#Variables
passenger_name = ""
list_flights = []
bookings = [{"name": "Ben Gataric", "flight": "AA455", "seats": 4},{"name": "Mario Luigi", "flight": "BB789", "seats": 99}] 

#View Bookings
def view_bookings():
    '''Doc String: This function shows the bookings of a passenger flight and the seats related to the booking'''
    '''
    This function will display the current bookings in a user-friendly format.
    It will iterate through the list of bookings and print out the details of each booking.

    Displays all bookings for the current passenger.  
• It performs the following steps: 
• Iterate through each booking in the bookings list. 
• Process each booking string to extract booking information. 
• Check if the provided passenger has a booking. 
• If a booking is found for this passenger: 
    o  Prints the flight number and seats booked for that booking. 
    •  If no matching bookings are found, prints “You have no bookings.” 
• Parameter(s): passenger name, and bookings list. 
• The function does not return any value including None. 

    '''
   
  #  if bookings == "":
    if not bookings:
        print("No bookings found.")
        
    for booking in bookings:
        if booking['name'] == passenger_name:
            print(f"Bookings for {passenger_name}")
            print(f"Flight No: {booking['flight']} Seats Booked: {booking['seats']}")
  


#view_bookings()

#Main Function
def main():
    '''Doc String: This function calls all the other functions of the reservations'''
    '''•	It is the main entry point and control function for the flight booking system.  
OK -    It displays a welcome banner. 
OK -    It prompts the user for a flight data filename (e.g., flights.txt) and checks if the file exists. 
OK -	If the file is not found, it displays an error message and prompts again. 
OK -	If the file is found, it loads the flights data from the file and stores the 
flights data in a list. 
OK -	It asks for the passenger's name. 
•	It continuously displays the main menu until the user chooses to exit (option 5). 
•	It calls corresponding functions based on user selection 
•	It displays an invalid input message if the user selects an invalid option 
'''
print("-" * 50)
print(f"Flight Booking System")
print("-" * 50)
flightdata = ""
#Open Flight Data File and show the contents
while flightdata == "":
    flightdata = input(f"Enter the flight data file name (e.g., flights.txt):  ")
    if os.path.exists(flightdata):
        with open(flightdata) as f:
            print("Loading flight data...")
            for line in f:
                items = line.rstrip().split(',')
                list_flight = {
                    "flight_number": items[0],
                    "flight_from": items[1],
                    "flight_to": items[2],
                    "flight_seats": items[3],
                    "flight_price": items[4]
                }
                list_flights.append(list_flight)
            print(f"Loaded {len(list_flights)} flights successfully.")

    else:
        print(f'{flightdata} file is not found.')
        flightdata = ""

passenger_name = input("Enter the passenger name: ")

view_bookings()