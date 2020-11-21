"""Dictionary containing the food-related ambiguities and less ambiguous forms.
The syntax of the value tables [British English word, American English word]. """
ENGLISH_AMBIGUITIES = {
    "french dressing": ["vinaigrette", "Marie Rose sauce"],
    "chips": ["chips", "French fries"],  # Potential problems if the user writes "chips" as the potato slices
    "prawns": ["prawns", "¤"],  # Prawns in the UK refer to both shrimps and the bigger prawns.
}
# TODO: Filter according to actual ingredients (e.g., "chips")
# TODO: Find an efficient way for plurals (e.g., for changes such as -y>-ies and -es)
# TODO: Check if there is a need to change to British English everywhere or not (i.e., the corpora use only one).
# TODO: Implement an input prompt for ¤ placeholders.
# TODO: Implement a mean for twofer differences (e.g., "chips" are either UK's fries or US's potato slices)
# TODO:

# Function prompting the user pick the less ambiguous forms.
# TODO?: Function prompting the user to pick one kind of English in case of ambiguities. (pick once or for each?)
