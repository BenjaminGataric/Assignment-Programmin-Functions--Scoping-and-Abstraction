'''
Program Name: Flight Booking System
Description: This program allows the user to load a flights list, add a passenger, buy seats, remove seats from user, and shows the information about the passenger, including flight number, seats and time of departure and arrive.
Authors: Ben Gataric, Vincent Ruiyang Li, Lelandi Calil De Assis, Devon Huynh
Date: March 27 2026

'''
import os
#Variables
passenger_name = ""
list_flights = []
bookings = []

#Save file
def save_flights(flight_list, filename="flights.txt"):
    #Opens and rewrites the text file with new fligth information
    with open(filename, "w") as f:
        for f_data in flight_list:
            line = f"{f_data['flight_number']},{f_data['flight_from']},{f_data['flight_to']},{f_data['flight_seats']},{f_data['flight_price']}\n"
            f.write(line)

def book_flight(name, flight_list, bookings, filename="flights.txt"):
    #Getting Flight number user wishes to book
    flight_number = input("Enter the flight number to book: ").upper()

    #Program runs through list to see if flight is availible
    flight_found = " "
    for flight in flight_list:
        if flight['flight_number'] == flight_number:
            flight_found = flight
            break

    if flight_found == flight_number:
        #If the flight is availble program collects the number of Seats and ask the user for how many seats they wish to book
        number_of_seats = int(input(f"How many seats would you like to book on {flight_number}?: "))

        #Program checks to see if the flight has enough seats
        if number_of_seats <= int(flight_found['flight_seats']):

            #Program removes the seats from the flight
            flight_found['flight_seats'] = str(int(flight_found['flight_seats']) - number_of_seats)

            #Creates a booking dictionary with Users name, flight number and the amount of seats they booked
            booking = {
                "Name": name,
                "Flight Number": flight_number,
                "Seats": number_of_seats
            }

            #Adds booking dictonary to booking list
            bookings.append(booking)

            #Saves updated data to txt file
            save_flights(flight_list, filename)

            #Prints a message to show a Successful booking with number of seats on the specific flight
            print(f"Successfully booked {number_of_seats} on flight {flight_number}.")
        else:
            print("Not enough seats")

    else:
        print("Flight not found")

#View Bookings
def view_bookings():
    '''Doc String: This function shows the bookings of a passenger flight and the seats related to the booking'''
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
    '''
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
print(list_flights)
book_flight(passenger_name, list_flights, bookings)
view_bookings()