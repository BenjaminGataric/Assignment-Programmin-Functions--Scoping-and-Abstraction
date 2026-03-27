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
bookings = []
flightdata = ""

def load_flights():
    '''Doc String: This function loads the flight availability data from a txt file'''   
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

def view_flights(list_flights):
    print("------------------------------------------")
    print("AVAILABLE FLIGHTS")
    print("------------------------------------------")
    print(f"{'Flight':<10}{'From':<7}{'To':<7}{'Seats':<9}{'Price'}")
    print("------------------------------------------")

    for flight in list_flights:
        print(f"{flight['flight_number']:<10}"
              f"{flight['flight_from']:<7}"
              f"{flight['flight_to']:<7}"
              f"{flight['flight_seats']:<9}"
              f"${float(flight['flight_price']):.2f}")

    print("------------------------------------------")



def main_menu():
    print("Welcome to the Flight Booking System!")
    print("1. View Flights")
    print("2. View My Bookings")
    print("3. Book a Flight")
    print("4. Cancel a Booking")
    print("5. Exit")
    input_choice = input("Please enter your choice (1-5): ")
    return input_choice


#Save file
def save_flights(flight_list, filename):
    #Opens and rewrites the text file with new flight information
    with open(filename, "w") as f:
        for f_data in flight_list:
            line = f"{f_data['flight_number']},{f_data['flight_from']},{f_data['flight_to']},{f_data['flight_seats']},{f_data['flight_price']}\n"
            f.write(line)

def book_flight(name, list_flights, bookings, filename):
    #Getting Flight number user wishes to book
    flight_number = input("Enter the flight number to book: ").upper()
    
    #Program runs through list to see if flight is availible
    flight_found = " "
    for flight in list_flights:
        if flight['flight_number'] == flight_number:
            flight_found = flight
            break
    
    if flight_found != " ":
        #If the flight is availble program collects the number of Seats and ask the user for how many seats they wish to book
        number_of_seats = int(input(f"How many seats would you like to book on {flight_number}?: "))
    
        #Program checks to see if the flight has enough seats
        if number_of_seats <= int(flight_found['flight_seats']):
        
            #Program removes the seats from the flight
            new_seats = int(flight_found['flight_seats']) - number_of_seats
            flight_found['flight_seats'] = str(new_seats)
        
            #Creates a booking dictionary with Users name, flight number and the amount of seats they booked
            booking = {
                "name": name,
                "flight number": flight_number,
                "seats": number_of_seats
            }

            #Adds booking dictonary to booking list
            bookings.append(booking)

            #Saves updated data to txt file
            save_flights(list_flights, filename)

            #Prints a message to show a Successful booking with number of seats on the specific flight 
            print(f"Successfully booked {number_of_seats} on flight {flight_number}.")
        else:
            print("Not enough seats")
            
    else:
        print("Flight not found")
        
#View Bookings
def view_bookings(name, bookings):
    '''Doc String: This function shows the bookings of a passenger flight and the seats related to the booking'''   
  #  if bookings == "":
    if not bookings:
        print("You have no bookings.")
    else:
        print("")
        print(f"Bookings for {name}")
    for booking in bookings:
        if booking['name'] == name:
            print(f"Flight No: {booking['flight number']} Seats Booked: {booking['seats']}")
    print("")


#Main Function
def main():
    '''Doc String: This function calls all the other functions of the reservations'''
print("-" * 50)
print(f"Flight Booking System")
print("-" * 50)

load_flights()

passenger_name = input("Enter the passenger name: ")
while passenger_name != "5":
    user_choice = main_menu()

    if user_choice == "1":
        view_flights(list_flights)
    elif user_choice == "2":
        view_bookings(passenger_name, bookings)
    elif user_choice == "3":
        book_flight(passenger_name, list_flights, bookings, flightdata)
    elif user_choice == "4":
        print("Devons part goes here")
    elif user_choice == "5":
        print("Exiting the system. Goodbye!")
        break