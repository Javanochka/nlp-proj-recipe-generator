import unittest
import identify_ingredients as module

# Sample of an ingredient list
INGREDIENT_LIST_SAMPLE: str = "ingrlst itemst 0.5 (8 ounce) package button mushrooms itemfn itemst 0.5 (6 ounce) package pre-sliced portabella mushrooms itemfn itemst 1 teaspoon olive oil itemfn itemst 1 teaspoon butter itemfn itemst 2 tablespoons finely chopped shallots itemfn itemst 2 garlic cloves, chopped itemfn itemst 18 teaspoon salt itemfn itemst 14 wonton wrappers itemfn itemst 1 teaspoon cornstarch itemfn itemst 12 cup 1% low-fat milk itemfn itemst 1 tablespoon all-purpose flour itemfn itemst 2 tablespoons grated fresh parmesan cheese itemfn itemst 1 tablespoon chopped fresh chives itemfn itemst 18 teaspoon salt itemfn itemst 1 dash fresh ground black pepper itemfn"
INSTRUCTION_LIST_SAMPLE = "instrst sentst drain the pineapple , then put into a large bowl . sentfn sentst reserve the cup . sentfn sentst meanwhile , combine chocolate chips and sugar in a large bowl . sentfn sentst stir until slightly thickened , about 8 minutes . sentfn sentst add 1 / 2 cup of 1 / 2 cup of the whites and then beat until stiff peaks form , about mixture ) . sentfn sentst brush each half over hot dough by lightly both sides and cut during the baking . sentfn sentst sprinkle with cinnamon and glaze . sentfn sentst cookies sentfn sentst melt chocolate chips and butter over medium heat . sentfn sentst stir together the caramel topping and eggs . sentfn sentst place onto squares and to warmed molds and place on a plate . sentfn sentst run knife around each 8 sides to touch in center of each rectangle . sentfn sentst invert onto well floured surface sprayed with cooking spray , pressing into rounds . sentfn"


class IdentifyIngrTest(unittest.TestCase):
    def test_split_ingrlst_into_list(self):
        """Test identify_ingredients' split_ingrlst_into_list method."""
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

    def test_split_instrst_into_list(self):
        """Test the split_instrst_into_list method — Currently only printing the result."""
        array = module.split_instrst_into_list(INSTRUCTION_LIST_SAMPLE)
        print(array)

    def test_acquire_ingredients_from_ingrlst(self):
        """Test the acquire_ingredients_from_ingrlst method — Currently only printing the result."""
        array = module.acquire_ingredients_from_ingrlst(INGREDIENT_LIST_SAMPLE)
        print(array)

    def test_acquire_ingredients_from_instrst(self):
        """Test the acquire_ingredients_from_instrst method — Currently only printing the result."""
        array = module.acquire_ingredients_from_instrst(INSTRUCTION_LIST_SAMPLE)
        print(array)

    if __name__ == '__main__':
        unittest.main()
