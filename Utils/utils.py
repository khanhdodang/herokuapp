import csv


class Utility():

  def read_csv(self, file):
    data = []
    with open(file, 'r') as csvfile:
      reader = csv.reader(csvfile, skipinitialspace=True)
      for row in reader:
        data.append(row)
    return data
