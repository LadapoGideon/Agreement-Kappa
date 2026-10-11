import unittest

from kappa import cohens_kappa, percent_agreement


class KappaTests(unittest.TestCase):
    def test_perfect_agreement(self):
        a = ["safe", "unsafe", "safe"]
        self.assertEqual(cohens_kappa(a, a), 1.0)

    def test_known_worked_example(self):
        # Observed agreement 0.75, chance agreement 0.5, so kappa = 0.5
        a = ["yes", "yes", "no", "no"]
        b = ["yes", "no", "no", "no"]
        self.assertEqual(percent_agreement(a, b), 0.75)
        self.assertAlmostEqual(cohens_kappa(a, b), 0.5)

    def test_mismatched_lengths_raise(self):
        with self.assertRaises(ValueError):
            cohens_kappa(["a"], ["a", "b"])

    def test_empty_input_raises(self):
        with self.assertRaises(ValueError):
            cohens_kappa([], [])


if __name__ == "__main__":
    unittest.main()
