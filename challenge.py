#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Minimal normalization of json file containing organization affiliation data from https://arxiv.org/"""

import json
import re
import csv

# TODO handle accidental input with the file extension
input_file = (
    input("Enter the name of the input file, excluding the file extension:\n") + ".json"
)
output_file = (
    input("Enter the name for the output file, excluding the file extension:\n")
    + ".csv"
)

data = json.load(open(input_file, "r"))
ABBRS = {
    "u": "University",
    "uni": "University",
    "univ": "University",
    "dept": "Department",
    "inst": "Institute",
    "nat": "National",
    "chem": "Chemistry",
    "div": "Division",
    "obs": "Observatory",
    "phys": "Physics",
    # 'tech' could be 'Technology' or 'Technological' so it is not included
}


def fix_abbreviations(items: list, abbreviations: dict):
    normalized = {}
    change_count = 0
    for item in items:
        org = item["author_affiliation"]
        if normalized.get(org):
            normal = normalized[org]
        else:
            normal = org
            for (
                abbr
            ) in abbreviations:  # instead of iterating over the abbreviations list,
                # it might be better to iterate over each word in the org
                normal = re.sub(rf"(?i)\b{abbr}($|\.|\b)", abbreviations[abbr], normal)
            normalized[org] = normal
        if normal != org:
            change_count += 1
    return normalized


# TODO: normalize missing values: '', 'na', 'n/a', etc.
# TODO: normalize orgs listed as one character
# TODO: remove repeated phrases like "for the"

if __name__ == "__main__":
    normalized = fix_abbreviations(data, ABBRS)
    with open(output_file, "w") as f:
        w = csv.writer(f, dialect="excel")
        w.writerow(["original_affiliation", "normalized_affiliation"])
        w.writerows(normalized.items())
    print(f"File saved as {output_file}")
