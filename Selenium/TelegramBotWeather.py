import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

config_dict = config.get_default_config()
config_dict['language'] = 'ua'  # your language here
bot = telebot.TeleBot("546513672:AAH5EUrfJbVFZu0zFsWgbaeULta0LaEdlK8", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

owm = OWM('d9678d1c755cbff1c1ebc6dbc1c2985a', config_dict)
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_welcome(message):
	# place = input('Погода в якому місті Вас цікавить?: ')
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	print (str(w)+str(message.text))

	# daily_forecaster = mgr.forecast_at_place(message.text, 'daily')
	# tomor = timestamps.tomorrow()
	# weath = daily_forecaster.get_weather_at(tomor)
	# print(weath)

	temp1 = w.temperature('celsius')['temp']
	temp_max = w.temperature('celsius')['temp_max']
	temp_min = w.temperature('celsius')['temp_min']
	wind = w.wind()['speed']
	rain = w.rain

	answer = 'В місті ' + message.text + ' зараз ' + w.detailed_status + '\n'
	answer += "Температура зараз десь " + str(temp1) + ' C\n'
	answer += "Cьогодні максимальна температура буде: " + str(temp_max) + ' С\n'
	answer += "Мінімальна температура: " + str(temp_min) + ' С\n\n'

	if temp1 < 10:
	    answer += 'Зараз дуже холодно! Вдівай шубу!\n\n'
	elif temp1 < 20:
	    answer += 'Зараз прохолодно! Вдягайся тепло!\n\n'
	else:
	   answer += 'Температура нормальна - можна в шльопанцях йти!\n\n'

	answer += "Швидкість вітру: " + str(wind) + ' м/с.\n'
	if len(rain)>0:
		answer += "Дощ: " + str(rain['1h']) + ' мм/год\n'
	else:
		answer += "Дощ: немає\n"
	bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)
