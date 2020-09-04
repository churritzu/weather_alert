#! /usr/bin/python3

import json

def read_conf_file():
  with open("./wa-conf.json") as conf_file:
      data = json.load(conf_file)
      print(data)

if __name__ == "__main__":
    read_conf_file()
