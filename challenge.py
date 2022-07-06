#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Minimal normalization of json file containing organization affiliation data from https://arxiv.org/"""

import json
import re
import sys
import csv

if len(sys.argv) != 3:
    raise IndexError(
        "Please try running again with arguments <input_file_name> <output_filename>"
    )
input_file = sys.argv[1]
output_file = sys.argv[2]

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
    # 'tech': 'Technology' or 'Technological'
}

# this function needs to be separated into smaller functions to separately test
# that the abbreviations list is being correctly generated
# and that the test_orgs are changed correctly
def fix_abbreviations(orgs: list, abbreviations: dict):
    normalized = {}  # not included as a parameter because of testing
    change_count = 0
    for org in orgs:
        org = org["author_affiliation"]
        if normalized.get(org):
            normal = normalized[org]
        else:
            normal = org
            for abbr in abbreviations:
                normal = re.sub(rf"(?i)\b{abbr}($|\.|\b)", abbreviations[abbr], normal)
            normalized[org] = normal
        if normal != org:
            change_count += 1
    return normalized, change_count


# TODO: normalize missing values: '', 'na', 'n/a', etc.
# TODO: normalize orgs listed as one character
# TODO: remove repeated phrases like "for the"

if __name__ == "__main__":
    normalized, change_count = fix_abbreviations(data, ABBRS)
    with open(output_file, "w") as f:
        w = csv.writer(f, dialect="excel")
        w.writerow(["original_affiliation", "normalized_affiliation"])
        w.writerows(normalized.items())
    print(f"File saved as {output_file}\n{change_count} corrections made")
