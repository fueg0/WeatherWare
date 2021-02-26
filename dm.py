import weatherware as ww
import DayWeather
import tweepy
import config
import re


def read_dms():
    messages = ww.api.list_direct_messages(100)
    return messages
def send_response():
    messages = read_dms()
    if messages:
        for message in messages:
            text = str(message.message_create['message_data']['text'])
            if "Hi! Thanks for" in text or "Please send a" in text:
                pass
            else:
                user_id = message.message_create['sender_id']
                i_d = message.id

                zip = int(re.findall(r"(?<!\d)\d{5}(?!\d)", text)[0])

                if not zip:
                    response = "Please send a message with a zip code for which you would like a weather report"
                else:
                    url = f"http://api.weatherapi.com/v1/forecast.json?key={config.WW_API}&q={zip}&days=1"
                    dm_response = ww.generate_tweet()
                    response = "Hi! Thanks for messaging WeatherWare! Here is your weather report:\n" + dm_response

                ww.api.send_direct_message(user_id, response)
                ww.api.destroy_direct_message(i_d)



#have a sleep for like 5 minutes. wayscript can run the script every 10 minutes
#so if we have a sleep for 5 minutes and then repeat the code we can have
#responses every 5 minutes
if __name__ == '__main__':
    send_response()
