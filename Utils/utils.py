import csv
import json


class Utility():

  def read_csv(self, file):
    data = []
    with open(file, 'r') as csvfile:
      reader = csv.reader(csvfile, skipinitialspace=True)
      for row in reader:
        data.append(row)
    return data

  def read_json(self, file):
    data = []
    with open(file, 'r') as jsonfile:
      reader = json.load(jsonfile)
      for d in reader:
        print(d)
        data.append(d)
    return data
