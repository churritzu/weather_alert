#! /usr/bin/python3

import json, requests, time, datetime

class Bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

class ErrorTypes:
	ALERT = "[ERROR]"
	WARNING = "[WARNING]"
	INFO =  "[INFO]"

messages = {
	"es":{
		"errors":{
			"404": "No se encontro el servidor",
			"503": "Servicio no disponible."
		},
		"response":{
			"alert": "Como quieres tus huevos al sol?",
			"warning": "Se necesita prender la refrigeracion",
			"normal": "A todo dar, ten un buen dia",
		}
	},
	"en":{
		"errors":{
			"404": "Server not found",
			"503": "Service Unavailable"
		},
		"response":{
			"alert": "My god, the planet is melting",
			"warning": "We need to turn on the cooling",
			"normal": "Oh boy, what a good day."
		}
	}
}

def log(message, type = ErrorTypes.INFO):
	diafecha = str(datetime.datetime.now())
	full_message = type + " [" + diafecha + "]: " + message

	open("logs.txt", 'a').write(full_message + "\n")
	return full_message 

def read_conf_file():
  data = None
  with open("./wa-conf.json") as conf_file: data = json.load(conf_file)
  return data

def get_params(data):
  data = read_conf_file()
  if data['api'] in data : return data[data['api']]
  else: 
    print("[ERROR]: The api your looking not exist.")
    return None

def get_open_weather_data(params):
  city = "q="+params['city']
  state = ","+params['state']
  country = ","+params['country']
  appKey = "&appid="+params['api_key']
  lang = "&lang=es"
  unit = "&units=metric"
  req = requests.get(params['base_url']+'?'+city+state+country+lang+unit+appKey)
  if req.status_code == 200: return req.json()
  else: 
    print("[ERROR] Server not found")
    return None

if __name__ == "__main__":
  config = read_conf_file()
  params = get_params(config)

  while True:
    data = get_open_weather_data(params)
    temp = data['main']['temp']
    print(temp)
    if temp >= 50:
      print("Como quieres tus huevos al sol???")
    elif temp < 50 and temp >= 40:
      print("Se necesita prender la refrigeracion :(")
    else:
      print("A todo dar, ten un buen dia :)")

    time.sleep(config['sleep']*60)


