import spacy                                                            # NLP library

nlp = spacy.load("en_core_web_sm")                                      # Load in pretrained model

with open("frankenstein.txt", "r", encoding="utf-8") as source:         # Load in some text
    data = source.read()                                                # Make it accessible as strings
    doc = nlp(data)                                                     # Apply pretrained model on the data
    for ent in doc.ents:                                                # Retrieve the NER tags
        print(ent.text, ent.label_)
