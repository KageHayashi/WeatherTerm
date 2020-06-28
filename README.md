# WeatherTerm
##### A simple command line parser interface for weather information via weather.com

## Installation 
### a. Requirements
Install requirements by typing the following command:

```
pip install -r requirements.txt
```
OR
```
python -m pip install -r requirements.txt
```

## Running the module
Since this is intented as a python module, you have to run it with the -m command. Be inside the WeatherTerm directory and use the following command:
```
python -m weatherterm -s [STATE] -c [CITY]
```
### Example
![](testimages/example.JPG)

## Help 
Use
```
python -m weatherterm -h
```
OR
```
python -m weatherterm --help
```
To display the help menu
![](testimages/help.PNG)

## Features
* Display info about current temperature, humidity, wind speed, and high/low temp of the day
* Find info on any city in the U.S 

## TO-DO
- [ ] Forecast future weather (ex. Five-day, Ten-day, Weekend)
- [ ] Add icons and stylize the interface
- [ ] Possible migration into a full-fledged CLI
