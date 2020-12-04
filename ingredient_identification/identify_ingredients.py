import spacy

nlp = spacy.load('en_core_web_sm')


def acquire_ingredients(tagged_text: str) -> list:
    """"""

    curated_ingredients = []
    item_sets = tagged_text.split("itemst")
    for item in item_sets:
        item.replace("itemfn", "")
        ingredients = [i.text for i in nlp(item) if i.label == "PRODUCT"]  # Collect every "product" tagged elements
        curated_ingredients.append(ingredients)

    return curated_ingredients


def test_acquire_ingredients():
    array = acquire_ingredients(
        "ingrlst itemst 0.5 (8 ounce) package button mushrooms itemfn itemst 0.5 (6 ounce) packagepresliced portabella mushrooms itemfn itemst 1 teaspoon olive oil itemfn itemst 1 teaspoon butter itemfn itemst 2 tablespoons finely chopped shallots itemfn itemst 2 garlic cloves, chopped itemfn itemst 18 teaspoon salt itemfn itemst 14 wonton wrappers itemfn itemst 1 teaspoon cornstarch itemfn itemst 12 cup 1% low-fat milk itemfn itemst 1 tablespoon all-purpose flour itemfn itemst 2 tablespoons grated fresh parmesan cheese itemfn itemst 1 tablespoon chopped fresh chives itemfn itemst 18 teaspoon salt itemfn itemst 1 dash fresh ground black pepper itemfn")

    print(array)
    return array


def are_ingredients_the_same(tagged_ingredient_list: str, tagged_instructions: str) -> bool:
    return acquire_ingredients(tagged_ingredient_list) == acquire_ingredients(tagged_instructions)
