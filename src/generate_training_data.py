from utils import save_data, load_data
import spacy
import random

verbs = load_data("data/verb.json")
people = load_data("data/people.json")
places = load_data("data/place.json")
events = load_data("data/event.json")
airlines = load_data("data/airline.json")
modifiers = load_data("data/modifier.json")
months = load_data("data/month.json")
ammenities = load_data("data/ammenity.json")
hosting_verb = load_data("data/hosting_verb.json")

def generate_querys():
    querys = []
    temp_query = ""
    for place in places:
        verb = verbs[random.randint(0, len(verbs)-1)]
        for person in people:
            if (person["value"][-1] == "s"):
                temp_query = f'{verb} {place["value"]} con mis {person["value"]}'
            elif (person == "solo" or person == "sola"):
                temp_query = f'{verb} {place["value"]} {person["value"]}'
            else:
                temp_query = f'{verb} {place["value"]} con mi {person["value"]}'
            querys.append(temp_query + f' con cualquier aerolinea {modifiers[random.randint(0, len(modifiers)-1)]} {airlines[random.randint(0, len(airlines)-1)]["value"]} en {random.choice(months)["value"]}')
            querys.append(temp_query + f'con {airlines[random.randint(0, len(airlines)-1)]["value"]}')
            querys.append(temp_query + f' y {hosting_verb[random.randint(0,len(hosting_verb)-1)]} en un lugar con {ammenities[random.randint(0,len(ammenities)-1)]["value"]}')
    for event in events:
        if (person["value"][-1] == "s"):
            temp_query = f'{verb} el {event["value"]} con mis {person["value"]}'
        elif (person == "solo" or person == "sola"):
            temp_query = f'{verb} el {event["value"]} {person["value"]}'
        else:
            temp_query = f'{verb} el {event["value"]} con mi {person["value"]}'
        querys.append(temp_query)

    save_data("data/test_data.json", querys)


def create_training_patterns():
    types = ["EVENT", "PEOPLE", "PLACE", "MODIFIER", "AIRLINE", "MONTH", "AMMENITY"]
    patterns = []
    for data_type in types:
        pattern = extract_pattern(
            load_data(f'data/{data_type.lower()}.json'), data_type)
        for pat in pattern:
            patterns.append(pat)
            print(pat)
    return patterns


def extract_pattern(data, type):
    patterns = []

    for item in data:
        if (type != "MODIFIER"):
            item = item["value"]
        pattern = {
            "label": type,
            "pattern": item
        }
        patterns.append(pattern)
    return patterns


def generate_rules(patterns):
    nlp = spacy.blank("es")
    ruler = nlp.add_pipe("entity_ruler", config={
                         "overwrite_ents": True, "phrase_matcher_attr": "LOWER"})
    ruler.add_patterns(patterns)
    nlp.to_disk("travel_ner")


patterns = create_training_patterns()
generate_querys()
generate_rules(patterns)
