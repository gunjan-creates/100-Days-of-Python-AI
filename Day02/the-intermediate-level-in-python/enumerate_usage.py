"""Uses enumerate to track positions when processing sequences."""

if __name__ == "__main__":
    cities = ["Tokyo", "New York", "Berlin", "Sydney"]
    for index, city in enumerate(cities, start=1):
        print(f"{index}. {city}")
