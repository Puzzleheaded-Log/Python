""" 
Write a Python program that:
  - uses the OMDb API
  - takes a movie title or keyword as input
Allows two options:
  - get full details for a specific movie
  - search for multiple movies by keyword (max 10 results)
Displays movie information in a clean format.
Uses functions to structure the logic.
Handles errors using try/except.   """


import requests

BASE_URL = "https://www.omdbapi.com/"
API_KEY = "your_api_key_here"


def get_movie_details_exact(title):
    params = {
        "apikey": API_KEY,
        "t": title,
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()

    if data["Response"] == "False":
        raise ValueError("Movie not found!")

    return data


def search_movies(keyword):
    params = {
        "apikey": API_KEY,
        "s": keyword,
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()

    if data["Response"] == "False":
        raise ValueError("Movie not found!")

    movies = []
    for movie in data["Search"]:
        movies.append(movie)

    return movies[:10]


def display_movie_details(movie):
    print("\nMovie information:")
    print("-" * 40)

    print("Title:", movie["Title"])
    print("Year:", movie["Year"])
    print("Genre:", movie.get("Genre", "N/A"))
    print("Director:", movie.get("Director", "N/A"))
    print("Actors:", movie.get("Actors", "N/A"))
    print("IMDB Rating:", movie.get("imdbRating", "N/A"))
    print("\nPlot:", movie.get("Plot", "N/A"))


def display_movie_list(movies):
    print("\nMovie list:")
    print("-" * 40)

    for movie in movies:
        print("\nTitle:", movie["Title"])
        print("Year:", movie["Year"])
        print("Type:", movie["Type"])


def main():
    while True:
        print("\n1. Search movie by title")
        print("2. Search movies by keyword")
        print("3. Exit")

        option = input("\nChoose option: ")

        if option == "1":
            try:
                title = input("Enter movie title: ")
                movie = get_movie_details_exact(title)
                display_movie_details(movie)
            except Exception as e:
                print("Error:", e)
            continue

        if option == "2":
            try:
                keyword = input("Enter keyword: ")
                movies = search_movies(keyword)
                display_movie_list(movies)
            except Exception as e:
                print("Error:", e)
            continue

        if option == "3":
            print("Finished search!")
            break


if __name__ == "__main__":
    main()

