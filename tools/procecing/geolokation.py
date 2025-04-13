from geopy.geocoders import Nominatim
from pprint import pprint # для удобного вывода 

def coordinatesCity(city): # для определения координат пишешь в city город затем страну через запятую тоесть так "Moscow, Russian"
    nominaltim = Nominatim(user_agent='user')

    location = nominaltim.geocode(city).raw

    pprint(location)

def geograficLocation(cordinates):
    nominaltim = Nominatim(user_agent='user')
    location = nominaltim.reverse(cordinates)

    print(location)