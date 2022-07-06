import unittest
import challenge

# def capitalize(string):
#     return string.capitalize()

# def add_period(string):
#     return string + '.'

# def same(string):
#     return string

# def capital_period(string):
#     return capitalize(add_period(string))

# def all_abbrs(abbreviations: dict, variations: list):
#     return { y(x):abbreviations[x] for x in abbreviations.keys() for y in variations }

# VARIATIONS = [
# capitalize,
# add_period,
# same,
# capital_period
# ]

# # creating the list of abbreviations since the fix_abbreviations function uses regex to match against multiple cases
# # due to time, I did not use this to test my regex pattern as intended
# # TODO: write test for regex pattern
# ALL_ABBRS = all_abbrs(challenge.abbreviations, VARIATIONS)

ORGS = [
    {"Technological University of Uruguay": "Technological University of Uruguay"},
    {"uni. of somewhere": "University of somewhere"},
    {"Uni of somewhere": "University of somewhere"},
    {"Vienna, Tech. U.": "Vienna, Tech. University"},
    {"Vienna, Tech. U": "Vienna, Tech. University"},
    {"Uni of somewhere": "University of somewhere"},
    {"Villanova University": "Villanova University"},
    {"UC Davis": "UC Davis"},
    {"U of GA, dept of math": "University of GA, Department of math"},
]

import ipdb; 
class FixAbbreviationsTest(unittest.TestCase):

    # test that the list of ORGS returns their expected values
    def test_all(self):
        for i in ORGS:
            with self.subTest(i=i):  # using subTest to test each individaul org in ORGS
                # using "list(i.keys())" is returning "Error in argument: '(i.keys())'" for some reason
                self.assertEqual(
                    challenge.fix_abbreviations(
                        [{"author_affiliation":x} for x in i.keys()], challenge.ABBRS
                    ),
                    i,
                )


if __name__ == "__main__":
    unittest.main()
