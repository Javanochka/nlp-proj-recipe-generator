import unittest
import identify_ingredients as module

# Sample of an
INGREDIENT_LIST_SAMPLE: str = "ingrlst itemst 0.5 (8 ounce) package button mushrooms itemfn itemst 0.5 (6 ounce) package pre-sliced portabella mushrooms itemfn itemst 1 teaspoon olive oil itemfn itemst 1 teaspoon butter itemfn itemst 2 tablespoons finely chopped shallots itemfn itemst 2 garlic cloves, chopped itemfn itemst 18 teaspoon salt itemfn itemst 14 wonton wrappers itemfn itemst 1 teaspoon cornstarch itemfn itemst 12 cup 1% low-fat milk itemfn itemst 1 tablespoon all-purpose flour itemfn itemst 2 tablespoons grated fresh parmesan cheese itemfn itemst 1 tablespoon chopped fresh chives itemfn itemst 18 teaspoon salt itemfn itemst 1 dash fresh ground black pepper itemfn"


class IdentifyIngrTest(unittest.TestCase):
    def test_split_ingredients_ingrlst(self):
        """Test identify_ingredients' split_elements_into_list method."""
        array = module.split_ingrlst_into_list(INGREDIENT_LIST_SAMPLE)
        print(array)
        self.assertListEqual(array, ['0.5 (8 ounce) package button mushrooms',
                                     '0.5 (6 ounce) package pre-sliced portabella mushrooms', '1 teaspoon olive oil',
                                     '1 teaspoon butter', '2 tablespoons finely chopped shallots',
                                     '2 garlic cloves, chopped', '18 teaspoon salt', '14 wonton wrappers',
                                     '1 teaspoon cornstarch', '12 cup 1% low-fat milk',
                                     '1 tablespoon all-purpose flour',
                                     '2 tablespoons grated fresh parmesan cheese', '1 tablespoon chopped fresh chives',
                                     '18 teaspoon salt', '1 dash fresh ground black pepper'])

    def test_acquire_ingredients_ingrlst(self):
        """Test the acquire_ingredients method — Currently only printing the result."""
        array = module.acquire_ingredients(INGREDIENT_LIST_SAMPLE)
        print(array)
        # We currently try to see whether 'PRODUCT' properly includes ingredients.
        array = module.acquire_ingredients("We will have one teaspoon of butter.")
        print(array)

    if __name__ == '__main__':
        unittest.main()
