import csv


def addMovie():
    movieList = []
    title = input("Title : ")
    genre = input("Genre : ")
    length = input("Length : ")
    cast = input("Cast : ")
    director = input("Director : ")
    adminRating = input("Admin Rating : ")
    language = input("Language : ")
    timings = input("Timings : ")
    numOfShows = input("Number of shows in a day : ")
    firstShow = input("First Show : ")
    intervalTime = input("Interval Time :")
    gap = input("Gap Between Shows : ")
    capacity = input("Capacity : ")

    movieList.append(title)
    movieList.append(genre)
    movieList.append(length)
    movieList.append(cast)
    movieList.append(director)
    movieList.append(adminRating)
    movieList.append(language)
    movieList.append(timings)
    movieList.append(numOfShows)
    movieList.append(firstShow)
    movieList.append(intervalTime)
    movieList.append(gap)
    movieList.append(capacity)

    with open("MovieDetails.csv", 'a', encoding='UTF8', newline='') as movieDetails:
        writer = csv.writer(movieDetails)
        writer.writerow(movieList)
        writer.writerow("\n")





