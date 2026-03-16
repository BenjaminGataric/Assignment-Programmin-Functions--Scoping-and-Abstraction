'''
Program Name: 
Description: 
Authors: Ben Gataric, Vincent Ruiyang Li, Lelandi Calil De Assis, Devon Huynh 
Date: 

'''


def view_bookings():
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
    # Example implementation (assuming bookings is a list of dictionaries)
    bookings = [
        {"name": "Ben Gataric", "flight": "AA4565", "seats": "44f"},
        {"name": "Vincent Ruiyang Li", "flight": "BB7890", "seats": "22b"},
        {"name": "Devon Huynh", "flight": "CC1234", "seats": "33c"}
    ]
    
    if not bookings:
        print("No bookings found.")
        return
    
    print("Current Bookings:")
    for booking in bookings:
        print(f"Name: {booking['name']}\t Flight: {booking['flight']}\t Seats: {booking['seats']}")

view_bookings()