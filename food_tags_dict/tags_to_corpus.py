import ijson                                    # Like json but does stream parsing to save on memory.
import nltk
from tags_dict_maker import DictMaker

instance = DictMaker()                          # To import the {ingredient: tags} dictionary
instance.dict_extractor()                       # To import the {ingredient: tags} dictionary
instance.rm_duplicates()                        # To import the {ingredient: tags} dictionary
instance.tags_cleaner()                         # To import the {ingredient: tags} dictionary


class Tagger:

    def implement_tags(self):
        """Applies the ingredient tags to the Recipe1M+ recipe corpus."""
        tags_dict = instance.tags_cleaner()             # Import the {ingredient: tags} dictionary
        recipe = ijson.parse(open("layer1.json"))       # Import the corpus to python chunk by chunk

        for prefix, event, value in recipe:                             # Look into the recipe currently in memory
            if prefix == "item.ingredients.item.text":                  # Grab a recipe instruction
                tokenized = nltk.word_tokenize(value)                   # Tokenize it -> [word1, word2, word3]
                dracula = 0
                new_string = ""
                for word in tokenized:                                  # For each word in the list
                    if dracula > 1:                                     # Avoid infinte loop (see below)
                        continue                                        # Avoid infinte loop (see below)
                    elif word in tags_dict.keys():                      # If the word is in the tag dictionary
                        for i in range(len(tokenized)):                 # Find index of word
                            if tokenized[i] == word:                    # Find index of word
                                tokenized.insert(i+1, tags_dict[word])  # Insert the associated tag behind the word
                                new_string = " ".join(tokenized)        # Merge the list into a string
                                dracula += 1                            # Avoid infinte loop created by this for loop
                print(new_string)                                       # Print each instructions with tags.


instance2 = Tagger()
instance2.implement_tags()
