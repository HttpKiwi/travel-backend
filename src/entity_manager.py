import spacy

from utils import load_data
from difflib import SequenceMatcher

people = load_data("data/people.json")
places = load_data("data/place.json")
events = load_data("data/event.json")
airlines = load_data("data/airline.json")
modifiers = load_data("data/modifier.json")
months = load_data("data/month.json")
ammenities = load_data("data/ammenity.json")

def most_similar(data, ent):
    largest = 0
    largest_idx = 0
    idx=-1
    for x in data:
        idx += 1
        ratio = SequenceMatcher(None, x["value"], ent).ratio() 
        if ratio > largest:
            largest_idx = idx
            largest = ratio
    print(data[largest_idx]["value"])
    return data[largest_idx]["value"]


def extract_entities(text):
    nlp = spacy.load("travel_ner")
    doc = nlp(text)

    ents = []

    for ent in doc.ents:
        ents.append([ent.text, ent.label_])

    print(ents)

    extract_iata(ents)

def translate_ents(ents, text):
    for ent in ents:
        print(ent)

def extract_iata(ents):
    test = ""
    for ent in ents:
        if ent[1] == "EVENT":
            test = most_similar(events, ent[0])
        elif ent[1] == "PLACE":
            test = most_similar(places, ent[0])
    print(test)