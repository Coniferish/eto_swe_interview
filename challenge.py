#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Minimal normalization of json file containing organization affiliation data from https://arxiv.org/"""

from distutils.util import change_root
import json
import re
import csv
import sys
import logging


ABBREVIATIONS = {
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


def fix_abbreviations(items: list):
    normalized = {}
    final_affiliations = []
    change_count = 0
    for item in items:
        org = item["author_affiliation"]
        if normalized.get(org):
            final_affiliations.append((org, normalized.get(org)))
            change_count += 1
        else:
            normal_org = normalize_name(org)
            if normal_org != org:
                change_count += 1
            final_affiliations.append((org, normal_org))
    return final_affiliations, change_count

def normalize_name(org):
    for abbreviation, full in ABBREVIATIONS.items():
        re.sub(rf"(?i)\b{abbreviation}($|\.|\b)", full, org)
    return org


# TODO: normalize missing values: '', 'na', 'n/a', etc.
# TODO: normalize orgs listed as one character
# TODO: remove repeated phrases like "for the"

if __name__ == "__main__":

    # TODO handle invalid arguments
    if len(sys.argv) != 3:
        raise IndexError(
            "Please try running again with arguments <input_file_name> <output_filename>")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, "r"):
        data = json.load(open(input_file, "r"))

    normalized, change_count = fix_abbreviations(data)
    logging.info(change_count)

    with open(output_file, "w") as f:
        w = csv.writer(f, dialect="excel")
        w.writerow(["original_affiliation", "normalized_affiliation"])
        w.writerows(normalized)
    print(f"File saved as {output_file}")
    
