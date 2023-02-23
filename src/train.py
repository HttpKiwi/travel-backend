import random

import spacy
import spacy.lang.es
from spacy.training import Example
from spacy.pipeline import EntityRuler
from utils import load_data, convert_training_data, save_data


def test():
    return 'hi'

def test_model(model, text):
    doc = model(text)
    results = []
    entities = []
    for ent in doc.ents:
        entities.append((ent.start_char, ent.end_char,ent.label_))
    if len(entities) > 0:
        results = [text, {"entities": entities}]
    return results

sample = load_data("data/test_data.json")
results = []

nlp = spacy.load("travel_ner")

for text in sample:
    result = test_model(nlp, text)
    if result != None:
        results.append(result)

save_data("training_data/training_set.json", results)

TRAIN_DATA = load_data("training_data/training_set.json")
convert_training_data(TRAIN_DATA)