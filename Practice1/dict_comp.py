""" 
dictionary comprehensions creates dictionaries using expression.
            can replace for loops and certain lambda functions. 
dictionay = {key: expression for (key, value) in iterable}
dictionay = {key: expression for (key, value) in iterable if conditional}
dictionay = {key: if/else for (key, value) in iterable}
dictionay = {key: function(value) for (key, value) in iterable}
"""

# Example

cities_F = {'New York': 32, 'Chicago': 50, "Boston": 75, "Los Angeles": 100, "Houston": 20}

cities_C = {key: round((value - 32) *( 5/9)) for (key, value) in cities_F.items()}
print(cities_C)

# --------------------------------------------------------

weather = {'New York': "SNOWING", 'Chicago': "CLOUDY", "Boston": "SUNNY", "Los Angeles": "SUNNY", "Houston": "SNOWING"}
s_weather = {key: value for (key, value) in weather.items()}
print(s_weather)

weathers = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities_F.items()}
print(weathers)

# ----------------------------------------------------------------

def get_weather(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WORM"
    else:
        return "COLD"

cities_F = {'New York': 32, 'Chicago': 50, "Boston": 75, "Los Angeles": 100, "Houston": 20}
s_weather = {key: get_weather(value) for (key, value) in cities_F.items()}
print(s_weather)