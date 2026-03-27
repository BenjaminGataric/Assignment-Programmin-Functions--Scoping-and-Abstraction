'''
Program Name: 
Description: 
Authors: Ben Gataric, Vincent Ruiyang Li, Lelandi Calil De Assis, Devon Huynh 
Date: 

'''
import os

def load_flights(filename):
    '''Doc String: This function loads the flight availability data from a txt file'''   
    #Open Flight Data File and show the contents
    with open(filename) as f:
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
        return list_flights

def view_flights(list_flights):
    print("-" * 43)
    print(f"{'AVAILABLE FLIGHTS':^43}")
    print("-" * 43)
    print(f"{'Flight':<10}{'From':<7}{'To':<7}{'Seats':<9}{'Price'}")
    print("-" * 43)

    for flight in list_flights:
        print(f"{flight['flight_number']:<10}"
              f"{flight['flight_from']:<7}"
              f"{flight['flight_to']:<7}"
              f"{flight['flight_seats']:<9}"
              f"${float(flight['flight_price']):.2f}")

    print("-" * 43)



def main_menu():
    #display selection menu 
    print("\n1. View Available Flights")
    print("2. View My Bookings")
    print("3. Book a Flight")
    print("4. Cancel a Booking")
    print("5. Exit")
    #asks the user for their item seclection
    input_choice = input("Please enter your choice (1-5): ")
    #returns the user selection for main function
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
    print(f"\nBookings for {name}")
    if not bookings:
        print("You have no bookings.")
    for booking in bookings:
        if booking['name'] == name:
            print(f"Flight No: {booking['flight number']} Seats Booked: {booking['seats']}")
    return bookings

#Booking Cancellation
def cancel_booking(passenger_name, bookings, flight_list, filename):
    flight_number = input("Enter the flight number to cancel: ").upper()

    for booking in bookings:
        if booking["name"] == passenger_name:
            if booking["flight number"] == flight_number:
                cancelled_seats = booking["seats"]
                for flight in flight_list:
                    if flight["flight_number"] == flight_number:
                        new_seats = int(flight["flight_seats"]) + cancelled_seats
                        flight["flight_seats"] = str(new_seats)
                        
                    
                save_flights(flight_list, filename)
                bookings.remove(booking)
            
                print(f"Successfully cancelled booking for flight {flight_number}\n")
                
    else:
        print(f"No booking found for the given flight number.\n")

#Main Function
def main():
    '''Doc String: This function calls all the other functions of the reservations'''

#Variables
passenger_name = ""
list_flights = []
bookings = []

print("-" * 50)
print(f"{'Flight Booking System':^50}")
print("-" * 50)
flightdata = ""
while flightdata == "":
        flightdata = input(f"Enter the flight data file name (e.g., flights.txt): ")
        if os.path.exists(flightdata):
            load_flights(flightdata)
            print(f"Loaded {len(list_flights)} flights successfully.")

        else:
            print(f'{flightdata} file is not found.')
            flightdata = ""

#input passenger name to store in bookings
passenger_name = input("Enter the passenger name: ")
#Decides what function to call based of user input
#calls main menu function
user_choice = main_menu()
while user_choice != "5":
    if user_choice == "1":
        view_flights(list_flights)
        user_choice = main_menu()
    elif user_choice == "2":
        view_bookings(passenger_name, bookings)
        user_choice = main_menu()
    elif user_choice == "3":
        book_flight(passenger_name, list_flights, bookings, flightdata)
        user_choice = main_menu()
    elif user_choice == "4":
        cancel_booking(passenger_name, bookings, list_flights, flightdata)
        user_choice = main_menu()
    elif user_choice == "5":
        print("Exiting the system. Goodbye!")
    else:
        print("Invalid option. Please try again")
        user_choice = main_menu()