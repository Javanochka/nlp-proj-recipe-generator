import spacy

nlp = spacy.load('en_core_web_md')


def split_ingrlst_into_list(tagged_text: str) -> list:
    """Break the ingredient textual list into a list object."""
    res = tagged_text.replace("ingrlst itemst ", "")  # Ingredient list's start tag.
    res = res.replace(" itemfn", "")
    res = res.split(" itemst ")
    return res
    # for instlst: ingrlfn  instrst / sentfn sentst


def acquire_ingredients(tagged_text: str) -> list:
    """We collect the ingredient in the text through PRODUCT-type Named Entities."""
    curated_ingredients = []
    for item in split_ingrlst_into_list(tagged_text):
        # For testing — TODO: To erase
        ingredients = [(ent.text, ent.label_) for ent in nlp(item).ents]
        # It fails to work — TODO: to fix.
        # ingredients = [ent.text for ent in nlp(item).ents if ent.label_ == "PRODUCT"]
        curated_ingredients.append(ingredients)

    return curated_ingredients


def are_ingredients_the_same(tagged_ingredient_list: str, tagged_instructions: str) -> bool:
    return acquire_ingredients(tagged_ingredient_list) == acquire_ingredients(tagged_instructions)
