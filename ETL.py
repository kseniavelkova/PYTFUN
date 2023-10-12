import collections
import random
import string
import datetime
import json
from json import dumps
import sys


def simulation(command):
    database = []
    for x in range(5):
        database.append(collections.OrderedDict([
            ('key', str(random.randint(100, 999)) + random.choice(string.ascii_uppercase)),
            ('value', round(random.uniform(0, 50), 1)),
            ('ts', str(datetime.datetime.now()))
        ]))

    with open('../rand_data.json', 'w') as output:
        output.write(dumps(database, indent=4))

    if command == 'Simulation':
        for i in database:
            print(i['key'], i['value'], i['ts'])

    elif command == 'File':
        with open('../rand_data.json', encoding='utf-8', errors='ignore') as json_data:
            data = json.load(json_data)
            for i in data:
                print(i['key'], i['value'], i['ts'])


class ETL:

    def source(self, data_source: str):
        command = data_source
        if data_source == 'Simulation':
            simulation(command)
        elif data_source == 'File':
            simulation(command)

        return self

    def sink(self, data_sink: str):
        self.data_sink = data_sink
        return self

    def run(self):
        pass
        if self.data_sink == 'Console':
            command = 'Continue'
            user_command = input('Please type to Continue or to Stop!')
            while command != 'Stop':
                simulation()


ETL().source('Simulation').sink('Console').run()
