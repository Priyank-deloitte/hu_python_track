import csv

import pandas as pd




class Edit:
    pass


def editMovie():
    movieName = input("Enter movie name which has to be updated : ")
    df = pd.read_csv('MovieDetails.csv')
    df.set_index("Title", inplace=True)
    df.loc[movieName]

    while True:
        print("1. Title")
        print("2. Genre")
        print("3. Length")
        print("4. Cast")
        print("5. director")
        print("6. Admin Rating")
        print("7. Language")
        print("8. Timings")
        print("9. Number of Shows")
        print("10. First Show")
        print("11. Interval Time")
        print("12. Gap Between Shows")
        print("13. Capacity")
        print("14. Nothing to update")

        choice = int(input("Enter the updation choice : "))

        if choice == 1:
            newMovieName = input("Enter new movie name : ")
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] == movieName:
                        row['Title']== newMovieName
                        break

        elif choice == 2:
            newGenre = input("Enter New Genre : ")
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] == movieName:
                        row['Genre'] == newGenre
                        break

        elif choice == 3:
            newLength = input("Enter New Length : ")
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] == movieName:
                        row['Length'] == newLength
                        break

        elif choice == 4:
            newCast = input("Enter New Cast : ")
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] == movieName:
                        row['Cast'] == newCast
                        break

        elif choice == 5:
            newDir = input("Enter New Director : ")
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] == movieName:
                        row['Director'] == newDir
                        break

        elif choice == 6:
            newAdminRating = input("Enter New Rating : ")
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] == movieName:
                        row['Admin Rating'] == newAdminRating
                        break

        elif choice == 7:
            newLanguage = input("Enter New Language : ")
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] == movieName:
                        row['Language'] == newLanguage
                        break

        elif choice == 8:
            newTiming = input("Enter New Timing : ")
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] == movieName:
                        row['Timings'] == newTiming
                        break

        elif choice == 9:
            newNum = input("Enter Number of Shows : ")
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] == movieName:
                        row['Number of Shows'] == newNum
                        break

        elif choice == 10:
            newFirstShow = input("Enter New time of the First Show : ")
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] == movieName:
                        row['First Show'] == newFirstShow
                        break

        elif choice == 11:
            newIntervalTime = input("Enter New Interval Time : ")
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] == movieName:
                        row['Interval Time'] == newIntervalTime
                        break

        elif choice == 12:
            newGap = input("Enter New Gap time : ")
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] == movieName:
                        row['Gap Between Shows'] == newGap
                        break

        elif choice == 13:
            newCapacity = input("Enter New Capacity : ")
            with open('MovieDetails.csv') as movieDetails:
                read = csv.DictReader(movieDetails)
                for row in read:
                    if row['Title'] == movieName:
                        row['Capacity'] == newCapacity
                        break

        elif choice == 14:
            break

        else:
            print("Enter a valid Choice!")
