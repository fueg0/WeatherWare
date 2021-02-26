from urllib import request
from bs4 import BeautifulSoup
import json
import DayWeather
import config
import tweepy

# Requires a WeatherAPI API key and US zipcode stored in config file
url = f"http://api.weatherapi.com/v1/forecast.json?key={config.WW_API}&q={config.zipcode}&days=1"

# Requires tweepy consumer public key and secret key
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)

# Requires tweepy public access token and secret access token
auth.set_access_token(config.access_token, config.access_token_secret)

# Create API object
api = tweepy.API(auth)


# BeautifulSoup json page request and loading
def get_page(page_url):
    html = request.urlopen(page_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    site_json = json.loads(soup.text)
    return site_json


# Parse through initial JSON
def get_day(json_info):
    json_info = json_info.get('forecast')
    json_info = json_info.get('forecastday')
    return json_info[0].get('day')


def generate_tweet(link):
    tweet = DayWeather.DayWeather(link)
    return tweet.make_tweet()


if __name__ == '__main__':
    api.update_status(generate_tweet(url))
