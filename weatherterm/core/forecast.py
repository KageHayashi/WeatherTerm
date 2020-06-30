from datetime import date
from .colors import colors
class Forecast:
    def __init__(
        self, 
        city,
        state,
        current_temp,
        humidity,
        wind,
        high_temp=None,
        low_temp=None,
        description='',
        forecast_date=None,):
        self.city = city
        self.state = state
        self._current_temp = current_temp
        self._high_temp = high_temp
        self._low_temp = low_temp
        self._humidity = humidity
        self._wind = wind
        self._description = description
    
    @property
    def forecast_date(self):
        return self._forecast_date
    @forecast_date.setter
    def forecast_date(self, forecast_date):
        self._forecast_date = forecast_date.strftime("%a %b %d")
    @property
    def current_temp(self):
        return self._current_temp
    @property
    def humidity(self):
        return self._humidity
    @property
    def wind(self):
        return self._wind
    @property
    def description(self):
        return self._description
    @property
    def high_temp(self):
        return self._high_temp

    @property
    def low_temp(self):
        return self._low_temp

    def __str__(self):
        temperature = None
        offset = ' ' * 3
        indent = '\u00A4'

        Status_OK = f'[{colors.OKGREEN}+{colors.ENDC}]'
        Status_WARNING = f'[{colors.WARNING}-{colors.ENDC}]'
        Status_FAIL = f'[{colors.FAIL}!{colors.ENDC}]'
        Status_HEADER = f'[{colors.HEADER}{indent}{colors.ENDC}]'
        Status_KEY = f'{colors.OKBLUE}'

        return(f'{Status_HEADER} Today\'s forecast for {Status_KEY}{self.city}, {self.state.title()} {colors.ENDC}\n'
               f'{offset}{Status_OK} Temp: {self.current_temp}\n'
               f'{offset}{Status_OK} Humidity: {self.humidity}\n'
               f'{offset}{Status_OK} Wind: {self.wind}\n'
               f'{offset}{Status_WARNING} High/Low: {self.high_temp}/{self.low_temp}\n'
               )