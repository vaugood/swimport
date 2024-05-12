# This is a hypothetical embedable script. Users may want to fetch data via API
# and parse it to a DataFrame so Swimport can use it. Users can also use
# scripts to parse local non-csv files to a DataFrame.
import pandas as pd

def main(apikey):
    if apikey == '9cdfb439c7876e703e307864c9167a15':
        df = {'productid': {0: 'p-101',1: 'p-105',2: 'p-109',3: 'p-203',4: 'p-300',5: 'p-301',7: 'p-302',8: 'p-306'}, 'name': {0: 'Sound Bowl',1: 'Quartz Rock',2: 'Quartz Skull',3: 'Pine Oil',4: 'Moss Stone',5: 'Sulfuric Acid',7: 'China Bowl',8: 'Topaz Ring'}}
        return pd.DataFrame(df)
    else:
        return 'Nope'