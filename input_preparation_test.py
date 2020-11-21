import unittest

exec(open("input_preparation.py").read())


class InputPreparationModuleTester(unittest.TestCase):
    """The expected output from the sample example (extract from the 2nd report). Uses hyphen, for ease of use."""
    expected_result = """
    - 1 whole lemon , sliced thin on the horizontal to form rings
    - 1 cup water
    - 23 cups sugar
    - 1 - 1 / 2 tablespoon flax meal
    """

    def test_main_from_inline(self):
        """Case with an inline input."""
        str = "1 whole lemon , sliced thin on the horizontal to form rings, 1 cup water, 23 cups sugar, 1 - 1 / 2 tablespoon flax meal"
        self.assertEquals(self.expected_result, prepare_input(str))
        pass

    def test_main_from_proper(self):
        """Given a proper input, it should be returned without changes."""
        self.assertEquals(self.expected_result, prepare_input(self.expected_result))
        pass


if __name__ == '__main__':
    unittest.main()
