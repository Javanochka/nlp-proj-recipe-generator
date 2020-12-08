import spacy

nlp = spacy.load('en_core_web_sm')


def split_ingrlst_into_list(tagged_text: str) -> list:
    """Break the ingredient textual list into a list object."""
    res = tagged_text.replace("ingrlst itemst ", "")  # Ingredient list's start tag.
    res = res.replace(" itemfn", "")
    res = res.split(" itemst ")
    return res
    # for instlst: ingrlfn  instrst / sentfn sentst


def acquire_ingredients(tagged_text: str) -> list:
    """"""

    curated_ingredients = []
    item_sets = tagged_text.split("itemst")
    for item in item_sets:
        item.replace("itemfn", "")
        ingredients = [i.text for i in nlp(item) if i.label == "PRODUCT"]  # Collect every "product" tagged elements
        curated_ingredients.append(ingredients)

    return curated_ingredients


def are_ingredients_the_same(tagged_ingredient_list: str, tagged_instructions: str) -> bool:
    return acquire_ingredients(tagged_ingredient_list) == acquire_ingredients(tagged_instructions)
