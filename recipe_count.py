import ijson                                    # Like json but does stream parsing to save on memory.

dracula = []                                    # List to store unique recipe IDs.

recipe = ijson.parse(open("layer1.json"))       # Import the file to python chunk by chunk.

for prefix, value in recipe:                    # Look into the recipe currently in memory.
    if (prefix == "item.id" and                 # Grab the recipe's id.
            value not in dracula):              # Make sure it is unique.
        dracula.append(value)                   # Add it to the list.
        print("Found one!")                     # Sanity check.

print(len(dracula))                             # Count dracula.
