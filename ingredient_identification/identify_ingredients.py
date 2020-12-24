import re

import spacy

# Load the custom model
nlp = spacy.load('../models')


def split_ingrlst_into_list(tagged_text: str) -> list:
    """Break the ingredient set into a list object."""
    res = tagged_text.replace("ingrlst itemst ", "")  # Ingredient set's start tag.
    res = res.replace(" itemfn", "")
    res = res.split(" itemst ")
    return res


def split_instrst_into_list(tagged_text: str) -> list:
    """Break the instruction set into a list object."""
    res = tagged_text.replace("instrst sentst ", "")  # Instruction list's start tag.
    res = res.replace(" . sentfn", "")
    res = res.split(" sentst ")
    return res


# List of false positives among the FOOD named entities. TODO: Improve model and delete list.
FALSE_POSITIVE_LIST = "teaspoon", "chopped"


def add_of_to_measure_units(item: str) -> str:
    """Append the word 'of' to measure units in the items. Allow to have better results with NER."""
    measure_units = ["teaspoons?", "tablespoons?"]
    for unit in measure_units:
        item = re.sub(unit, "\g<0> of", item)
    return item


def acquire_ingredients_from_ingrlst(tagged_text: str) -> list:
    """We collect the ingredient in the text through FOOD-type Named Entities."""
    curated_ingredients = []
    for item in split_ingrlst_into_list(tagged_text):
        # Remove the measures that create problem for NER
        item = add_of_to_measure_units(item)
        # Pick the ingredients found by the NER
        ingredients = [ent.text for ent in nlp(f"I ate {item}").ents if ent.label_ == "FOOD"
                       and ent.text not in FALSE_POSITIVE_LIST]
        if ingredients:
            curated_ingredients.append(ingredients)

    return curated_ingredients


def acquire_ingredients_from_instrst(tagged_text: str) -> list:
    """We collect the ingredient in the text through FOOD-type Named Entities."""
    curated_ingredients = []
    for item in split_instrst_into_list(tagged_text):
        # Pick the ingredients found by the NER
        ingredients = [ent.text for ent in nlp(item).ents if ent.label_ == "FOOD"
                       and ent.text not in FALSE_POSITIVE_LIST]
        if ingredients:
            curated_ingredients.append(ingredients)

    return curated_ingredients


def do_ingredients_correspond(tagged_set: str) -> bool:
    sets = tagged_set.split("ingrlfn")
    return acquire_ingredients_from_ingrlst(sets[0]) == acquire_ingredients_from_instrst(sets[1])
