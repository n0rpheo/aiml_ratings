import csv

affiliations = set()
with open("../../data/internal/affiliations.txt") as aff_file:

    for line in aff_file:
        affiliations.add(line.strip().lower())

match_affs = set()
with open("../../data/external/csratings.csv") as csratings_file:
    spamreader = csv.DictReader(csratings_file, delimiter=',')

    for idx, row in enumerate(spamreader):
        if row['affiliation'].lower() in affiliations:
            match_affs.add(row['affiliation'])

print(str(match_affs))
print()
