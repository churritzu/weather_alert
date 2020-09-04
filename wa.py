#! /usr/bin/python3

import json, requests, time

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


