import bioc
from bioc import BioCFileType
import json
import re

# Original file found at http://cs.ijs.si/repository/FoodBase/foodbase.zip


class FileMaker:

    def xml_decoder(self):
        """Decode an XML file and return a bioc.collection object in a variable called output."""
        with open("foodbase/FoodBase_curated.xml", "r") as xml_file:
            collection = bioc.load(xml_file)
            output = bioc.dumps(collection, BioCFileType.BIOC_JSON, indent=2)

        return output

    def json_maker(self):
        """Encode the variable called ouput in a JSON file."""
        output = self.xml_decoder()

        with open("foodbase.json", "w") as json_file:
            json_file.write(output)


class DictMaker:

    def dict_extractor(self):
        """Create a python dictionary of ingredients and tags."""
        tags_dict = {}                                          # {ingredient: tag(s)}

        with open("foodbase.json", "r") as f:                   # Open the food corpus containing tags
            corpus = json.load(f)                               # Load the corpus in a variable
            for recipe in corpus["documents"]:                  # Loop through the recipes of the corpus
                for ingredient in recipe["annotations"]:        # Loop through the ingredients of each recipe
                    tags_dict[ingredient["text"]] = ingredient["infons"]["semantic_tags"]     # Fill dict

        return tags_dict

    def rm_duplicates(self):
        """Remove duplicates from the dictionary."""
        tags_dict = self.dict_extractor()
        keys_list = []                                          # List of unique ingredients

        for i in tags_dict:                                     # For each element in the dictionary
            if i not in keys_list:                              # If encountered for the first time
                keys_list.append(i)                             # Add it to the list
            elif i in keys_list:                                # If already encountered
                del tags_dict[i]                                # Remove it from the dictionary

        return tags_dict

    # This block cleans the tags in the dictionary to have {ingredient1: [tag1, tag2, tag3], ingredient2: [tag1]}
    def tags_cleaner(self):
        """Clean the tags in the dictionary to have {ingredient1: [tag1, tag2, tag3], ingredient2: [tag1]}"""
        tags_dict = self.rm_duplicates()

        for pair in tags_dict:                                      # For each key: value in the dictionary
            my_list = re.findall(r"\[(.+?)]", tags_dict[pair])      # Look in value for all tags -> [cheese]
            tags_dict[pair] = my_list                               # Replace the value by a list of tags

        for i in tags_dict:
            tags_dict[i] = str(tags_dict[i])

        return tags_dict
