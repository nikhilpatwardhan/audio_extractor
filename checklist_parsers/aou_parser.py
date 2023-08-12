"""
Parse the csv file from https://checklist.americanornithology.org/taxa/ into a json metadata file.
"""
import json
import csv
from os.path import exists


def read(infilepath):
    result = []
    with open(infilepath, 'r') as infile:
        csv_reader = csv.DictReader(infile)
        for d in csv_reader:
            subset = {k: v for k, v in d.items() if k in ['common_name', 'order', 'family', 'genus', 'species']}
            result.append(subset)
    return result


def write(outfilepath, data):
    if exists(outfilepath):
        raise ValueError(f'{outfilepath} exists already.')

    with open(outfilepath, 'w') as outfile:
        outfile.write(json.dumps(data, indent=2))


if __name__ == '__main__':
    data = read('checklists/NACC_list_species.csv')
    write('../data/NACC_list_species.json', data)
