import json
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin


def convert_training_data(TRAIN_DATA):
    nlp = spacy.blank("es")
    db = DocBin() 

    for text, annot in tqdm(TRAIN_DATA): 
        doc = nlp.make_doc(text)
        """ print(annot["entities"]) """
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents = ents 
        db.add(doc)

    db.to_disk("./train.spacy") 

def save_data(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data