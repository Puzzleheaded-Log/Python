""" 
Write a Python program that:
  - uses the Rest Countries API
  - takes a country name as input
  - retrieves the country code using the API
  - fetches detailed information using the country code
Displays:
  - official name
  - capital
  - region
  - population
  - currencies
  - official languages
Handles errors using try/except.   """

import requests

BASE_URL = "https://restcountries.com"

def get_country_code(country_name):
    url = f"{BASE_URL}/v3.1/name/{country_name}"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if not data:
        raise ValueError("Country not found")

    return data[0]["cca2"]

def get_country_info(country_code):
    url = f"{BASE_URL}/v3.1/alpha/{country_code}"
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if not data:
        raise ValueError("Country not found")

    return data

def display_country_info(country):
    print("\nCountry information:")
    print("-" * 40)

    for key, value in country.items():
        if key == "currencies":
            for currency in value.values():
                print(f"Currency: {currency['name']}")

        if key == "capital":
            print(f"Capital: {value[0]}")

        if key == "region":
            print(f"Region: {value}")

        if key == "languages":
            for lang in value.values():
                print(f"Official language: {lang}")

        if key == "population":
            print(f"Population: {value}")

if __name__ == "__main__":
    country = input("Enter country name (e.g. Rwanda): ")

    try:
        code = get_country_code(country)
        info = get_country_info(code)

        print(f"Country: {info[0]['name']['official']}")
        display_country_info(info[0])

    except Exception as e:
        print("Error:", e)

  
