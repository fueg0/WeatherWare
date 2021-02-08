import weatherware


class DayWeather:
    def __init__(self, url):
        info = weatherware.get_day(weatherware.get_page(url))
        self.conditions = info.get('condition').get('text')
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

    def make_tweet(self):
        tweet = f'Conditions today: {self.conditions}\n' \
                f'High: {self.max}F, Low: {self.min}F\n' \
                f'Average Temperature: {self.avg}F\n' \
                f'Chance of rain: {self.rain}% / snow: {self.snow}%\n' \
                f'Precipitation: {self.precip} inches\n' \
                f'UV Index: {self.uv}\n' \
                f'Humidity: {round(self.humidity)}%\n' \
                f'Visibility: {self.visibility} miles\n' \
                f'Max Wind: {self.wind}mph'
        return tweet
