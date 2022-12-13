import unittest
import challenge


TEST_ORGS = [
    ("Technological University of Uruguay", "Technological University of Uruguay"),  # no change
    ("uni. of somewhere", "University of somewhere"),  # abbreviation, case, and punctuation
    ("Uni of somewhere", "University of somewhere"),  # abbreivation
    ("Vienna, Tech. U.", "Vienna, Tech. University"),  # abbreviation and period, ending
    ("Vienna, Tech. U", "Vienna, Tech. University"),  # abbreviation, ending
    ("Uni of somewhere", "University of somewhere"),  # abbreviation
    ("U of GA, dept of math", "University of GA, Department of math"),  # multiple abbreviation
    # multiple abbreviation, case, and punctuation
    ("nat. dept. of science at some uni.", "National Department of science at some University") 
]


class FixAbbreviationsTest(unittest.TestCase):

    # test that the list of TEST_ORGS returns their expected values
    def test_normalize_name(self):
        for i in TEST_ORGS:
            with self.subTest(i=i):  # using subTest to test each individaul org in ORGS
                # using "list(i.keys())" is returning "Error in argument: '(i.keys())'" for some reason
                self.assertEqual(
                    challenge.normalize_name(i[0]), i[1]
                )


if __name__ == "__main__":
    unittest.main()
