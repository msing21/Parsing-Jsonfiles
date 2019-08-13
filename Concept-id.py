import pandas as pd
import json
import csv
import time
import os


def json_to_csv(filename):
    with open(filename) as json_file:
        json_parsed = json.load(json_file)
        for terms in json_parsed['_embedded']['terms']:
            id = terms['annotation']
            for i in id:
                conceptid = id['closeMatch']
                df1 = pd.DataFrame.from_dict(conceptid)
                df1.to_csv('/home/manali/Downloads/json/EFO_0000304.csv')
                return df1


# print (json_to_csv('/home/manali/Downloads/C0858252'))

if __name__ == "__main__":
    filename = '/home/manali/Downloads/json/EFO_0000304.json'
    start = time.time()
    json_to_csv(filename)
    end = time.time()

    print 'time elapsed:' + str(end - start)
    print json_to_csv(filename)


