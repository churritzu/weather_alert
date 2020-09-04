#! /usr/bin/python3

import json

def read_conf_file():
  data = None
  with open("./wa-conf.json") as conf_file: data = json.load(conf_file)
  return data

def get_default_params():
  data = read_conf_file()
  if data['api'] in data : 
    return data[data['api']]
  else: 
    print("[ERROR]: The api your looking not exist.")
    return None

def get_open_weather_data():
  pass
    # r = requests.get('https://api.github.com/user')
    # print(r)

if __name__ == "__main__":
    params = get_default_params()
    print(params)
