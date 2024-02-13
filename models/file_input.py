import json
import pandas as pd

DATA_FILE = 'models/sample.json'

def getRTData():
    data = json.load(open(DATA_FILE))
    data = pd.DataFrame({'id': data['N_ind'], 'congruency': data['condition'],'rt': [x/1000 for x in data['RT']], 'accuracy': [x-1 for x in data['choice']]})
    data['congruency'] = ['congruent' if x == 1 else 'incongruent' for x in data['congruency']]
    return data