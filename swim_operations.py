import xml.etree.ElementTree as ET
import pandas as pd

def operate(data:pd.DataFrame, lap:ET.Element):
    operation = lap.find('operation')
    match operation.get('name'):
        case 'sort_values':
            by=operation.find('by').text
            ascending=operation.find('ascending').text
            ascending=bool(int(ascending))
            data = data.sort_values(by=by,ascending=ascending)
        case 'explode':
            series=operation.find('series')
            cols=[col.text for col in series.findall('col')]
            data = data.explode(column=cols)
        case 'split':
            column=lap.find('column').text
            pat=operation.find('pat').text
            data[f'{column}'] = data[f'{column}'].str.split(pat=pat)
        case 'reset_index':
            drop=operation.find('drop').text
            drop=bool(int(drop))
            data = data.reset_index(drop=drop)
    return data