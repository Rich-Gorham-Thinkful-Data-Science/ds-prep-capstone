import pandas as pd

def US_Population_1996_2015(f):
    US_Population = pd.read_csv('./data/' + f, dtype={0:int, 1:float})
    US_Population.sort_values('Year', inplace=True)
    US_Population_1996_2015 = \
         pd.DataFrame(US_Population[US_Population['Year']\
           .between(1996, 2015, inclusive=True)])

    US_Population_1996_2015.reset_index(drop=True, inplace=True)

    return US_Population_1996_2015
