import csv

class BookingTickets:
    pass

def book(Movie, Name):
    with open("MovieDetails.csv") as movieDetail:
        read = csv.DictReader(movieDetail)

        for row in read:
            if row ['Title'] == Movie:
                timing = row['Timings']
                break

        timingList = timing.split(",")
        for time in range (len(timingList)):
            print("Press ", time + 1, " for selecting time slot of", timingList[time])

        selectTime = int (input("Enter value for choosing the time : "))

        for time in range(len(timingList)):
            if time == selectTime:
                print("Timing : ", timingList[time])

        remainingSeat = int(row['Capacity'])
        print("Remaining Seat : ", remainingSeat)

        numOfSeats = int(input("Enter the number of seats you want to book : "))

        if remainingSeat >= numOfSeats:
            saetLeft = remainingSeat - numOfSeats
            seatRemain = str(saetLeft)
            with open("MovieDetails.csv") as movieDetail:
                read = csv.DictReader(movieDetail)
                for row in read :
                    if row['Title'] == Movie:
                        row['Capacity'] =seatRemain
                        break


            print("Booking Successfull ! Thanks for Booking through BookMyShow")

        else:
            print("Seats Unavailable!!!")



