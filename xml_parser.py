import bioc
from bioc import BioCFileType
import json
import re

# Original file found at http://cs.ijs.si/repository/FoodBase/foodbase.zip

# Decode an XML file and create a bioc.collection object in a variable called output
with open("foodbase/FoodBase_curated.xml", "r") as xml_file:
    collection = bioc.load(xml_file)
    output = bioc.dumps(collection, BioCFileType.BIOC_JSON, indent=2)

# Encode the variable called ouput in a JSON file
with open("foodbase.json", "w") as json_file:
    json_file.write(output)


# This block creates a python dictionary of ingredients and tags
tags_dict = {}                                          # {ingredient: tag(s)}

with open("foodbase.json", "r") as f:                   # Open the food corpus containing tags
    corpus = json.load(f)                               # Load the corpus in a variable
    for recipe in corpus["documents"]:                  # Loop through the recipes of the corpus
        for ingredient in recipe["annotations"]:        # Loop through the ingredients of each recipe
            tags_dict[ingredient["text"]] = ingredient["infons"]["semantic_tags"]   # Get ingredient's name and tag(s)


# This block removes duplicates from the dictionary
keys_list = []                                          # List of unique ingredients
for i in tags_dict:                                     # For each element in the dictionary
    if i not in keys_list:                              # If encountered for the first time
        keys_list.append(i)                             # Add it to the list
    elif i in keys_list:                                # If already encountered
        del tags_dict[i]                                # Remove it from the dictionary

# This block cleans the tags in the dictionary
for pair in tags_dict:                                      # For each key: value in the dictionary
    my_list = re.findall(r"\[(.+?)]", tags_dict[pair])      # Look in value for all tags -> [cheese]
    tags_dict[pair] = my_list                               # Replace the value by a list of tags
