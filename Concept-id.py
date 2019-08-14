import pandas as pd
import json
import csv
import time
import sys,os,argparse


def json_to_csv(filename):
    with open(filename) as json_file:
        json_parsed = json.load(json_file)
        for terms in json_parsed['_embedded']['terms']:
            id = terms['annotation']
            for i in id:
                conceptid = id['closeMatch']
                df1 = pd.DataFrame.from_dict(conceptid)
                df1[0] = df1[0].map(lambda x: x.lstrip('http://linkedlifedata.com/resource/umls/id/'))
                df1.to_csv('test.csv', index=None, header=None)
                

def getArgs():
    parser = argparse.ArgumentParser('python')
    parser.add_argument('-infile', required = True)
    return parser.parse_args()

if __name__ == "__main__":
    args = getArgs()
    filename = json_to_csv(args.infile)
    start = time.time()
    end = time.time()

    print 'time elapsed:' + str(end - start)
    


