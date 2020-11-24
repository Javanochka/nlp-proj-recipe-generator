import json
import nltk
from nltk.corpus import wordnet as wn

results = []
path = r'G:\corpus\layer1.json'

with open(path, 'r') as file:
    time = 0

    for line in file:
        time+=1

        if(time != 1):
            temp = []
            line = line[:-2]
            dic = json.loads(line)
            ingredients = dic["ingredients"]
            # print(ingredients)
            choises = []
            food = [wn.synset('food.n.01'), wn.synset('food.n.02'), wn.synset('food.n.03'),
                    wn.synset('living_thing.n.01')]

            for content in ingredients:

                text = content["text"]
                tokens = nltk.word_tokenize(text)
                tagged = nltk.pos_tag(tokens)
                print('----------------')
                print(tokens)

                for unit in tagged:
                    if(unit[1]=='NN' or unit[1]=='NNP' or unit[1]=='NNS'):
                        try:
                            noun = nltk.stem.PorterStemmer().stem(unit[0].lower())
                            noun = noun.lower()
                            kind = wn.synset(unit[0].lower() + '.n.01')
                            #print(unit[0])
                            hyper = lambda s: s.hypernyms()
                            hyperKind = list(kind.closure(hyper))
                            #print(hyperKind)


                            for item in hyperKind:
                                if((item in food) and (unit[0].lower() not in temp)):
                                    print(unit[0] + " is food")
                                    temp.append(unit[0].lower())
                                    break
                        except:
                            continue

            if(temp.__len__() != 0):
                print('final result is :')
                print(temp)
                print('--------------')
                path = r'E:\编程文件\python\Uni Lorraine\recipeCreator\nodes.txt'
                with open(path, 'a') as file:
                    for i in temp:
                        file.write(i + ' ')
                    file.write('\n')
                if(time == 1000):
                    break

