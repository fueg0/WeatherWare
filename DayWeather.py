import weatherware
import config
from datetime import date
from datetime import datetime
import calendar
my_date = date.today()
weekday = calendar.day_name[my_date.weekday()]


class DayWeather:
    def __init__(self, url, zipcode):
        loc = weatherware.get_page(url)
        info = weatherware.get_day(loc)
        self.conditions = info.get('condition').get('text')
        self.city = loc.get('location').get('name')
        self.state = loc.get('location').get('region')
        self.max = info.get('maxtemp_f')
        self.min = info.get('mintemp_f')
        self.avg = info.get('avgtemp_f')
        self.visibility = info.get('avgvis_miles')
        self.humidity = info.get('avghumidity')
        self.wind = info.get('maxwind_mph')
        self.rain = info.get('daily_chance_of_rain')
        self.snow = info.get('daily_chance_of_snow')
        self.precip = info.get('totalprecip_in')
        self.uv = info.get('uv')
        self.zip = zipcode

    def make_tweet(self):
        tweet = f'Weather for {self.city}, {self.state}, {weekday}, {my_date}\n\n' \
                f'Conditions today: {self.conditions}\n' \
                f'High: {self.max}F, Low: {self.min}F\n' \
                f'Average Temperature: {self.avg}F\n' \
                f'Chance of rain: {self.rain}% / snow: {self.snow}%\n' \
                f'Precipitation: {self.precip} inches\n' \
                f'UV Index: {self.uv}\n' \
                f'Humidity: {round(self.humidity)}%\n' \
                f'Visibility: {self.visibility} miles\n' \
                f'Max Wind: {self.wind}mph'
        return tweet
