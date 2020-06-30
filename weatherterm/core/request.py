import requests
from bs4 import BeautifulSoup
import json
import os.path
import pathlib
from .forecast import Forecast
from difflib import get_close_matches

weatherBaseURL = "https://weather.com/weather/today/l/"
weatherCodesURL = "https://weather.codes/united-states-of-america/"


#Request all city weather code of a given state and save it as a json file
def requestCodes(state):
    state = state

    #Weather Codes Request
    codesRequest = requests.get(weatherCodesURL + state)
    codesContent = codesRequest.content
    codesSoup = BeautifulSoup(codesContent, "html.parser")
    codes = codesSoup.find_all("div", class_="country__codes__letter")

    codesDict = {}

    for i in range(len(codes)):
        for code in codes[i].find_all("li"):
            codesDict[code.strong.contents[0]] = code.span.contents[0]

    with open(str(pathlib.Path().absolute()) + '\\weatherterm\\core\\state_codes\\%s.json' % state, "w+") as json_file:
        json.dump(codesDict, json_file)

#Request the forecast on a city and return a Forecast class
def requestForecast(state='', city='', code=None):
    state = state
    city = city

    if os.path.isfile(str(pathlib.Path().absolute()) + '\\weatherterm\\core\\state_codes\\%s.json' % state):
        with open(str(pathlib.Path().absolute()) + '\\weatherterm\\core\\state_codes\\%s.json' % state, "r") as f:
            jdata = json.load(f)
            if len(get_close_matches(city, jdata.keys())) > 0:
                city = get_close_matches(city, jdata.keys())[0]
                code = jdata[city]
    else:
        requestCodes(state)
        with open(str(pathlib.Path().absolute()) + '\\weatherterm\\core\\state_codes\\%s.json' % state, "r") as f:
            jdata = json.load(f)
            if len(get_close_matches(city, jdata.keys())) > 0:
                city = get_close_matches(city, jdata.keys())[0]
                code = jdata[city]

    #Weather Forcast Request
    weatherRequest = requests.get(weatherBaseURL + str(code))
    weatherContent = weatherRequest.content
    weatherSoup = BeautifulSoup(weatherContent, "html.parser")
    try:
        current = (weatherSoup.find("span", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY").contents[0])
        pressure = weatherSoup.find("span", class_="_-_-components-src-atom-WeatherData-Pressure-Pressure--pressureWrapper--3SCLm undefined").contents[-1]
        moleculeData = weatherSoup.find_all("div", class_="_-_-components-src-molecule-WeatherDetailsListItem-WeatherDetailsListItem--wxData--kK35q")

        humidity = (moleculeData[2].contents[0].contents[0])
        high= (moleculeData[0].contents[0].contents[0])
        low = (moleculeData[0].contents[2].contents[0])
        wind = (moleculeData[1].contents[0].contents[-1])

        return Forecast(city, state, current, humidity, wind, high, low)
    except:
        print("Something went wrong. City-State mismatch?")


