import re

with open("../../data/external/hochschulen.txt") as aff_file:
    with open("../../data/internal/affiliations.txt", "w") as aff_write:
        for idx, row in enumerate(aff_file):
            affiliation = re.sub("[\(\[].*?[\)\]]", "", row).strip().replace("Technische Universität", "TU")
            affiliation = affiliation.replace("München", "Munich")
            aff_write.write(affiliation + "\n")