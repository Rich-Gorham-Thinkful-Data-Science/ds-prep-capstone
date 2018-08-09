import pandas as pd

def data(f):
    data = pd.read_csv('./data/' + f, dtype={13:object, 15:object, 37:object,\
                                 39:object, 82:object, 84:object,\
                                 91:object, 93:object})

    return data
