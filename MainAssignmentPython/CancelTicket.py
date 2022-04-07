import csv


class CancelTicket:
    pass

def cancel(Movie, Name):
    with open("MovieDetails.csv") as movieDetail:
        read = csv.DictReader(movieDetail)

        for row in read:
            if row ['Title'] == Movie:
                availableSeats = int(row['Capacity'])

    cancelSeats = int(input("Enter the number of seats tob be cancelled : "))
    if availableSeats > cancelSeats:
        seatLeft = availableSeats + cancelSeats
        remainingSeats = str(seatLeft)
        with open("MovieDetails.csv") as movieDetail:
            read = csv.DictReader(movieDetail)
            for row in read:
                if row['Title'] == Movie:
                    row['Capacity'] = remainingSeats
                    break

        print("Booking Cancelled Successfully!!!")

    else:
        print("Invalid Cancellation!!")


