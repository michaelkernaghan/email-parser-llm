import json
import spacy
from spacy.tokens import DocBin
from spacy.training import Example

# Load pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Load labeled data
with open('labeled_test_emails.json', 'r') as f:
    data = json.load(f)

def create_training_data(data):
    train_data = []
    for item in data:
        email_text = item['body']
        labels = item['labels']
        entities = []
        seen_spans = set()
        
        def add_entity(start, end, label):
            if all(start >= e_end or end <= e_start for e_start, e_end, _ in seen_spans):
                entities.append((start, end, label))
                seen_spans.add((start, end, label))
        
        for po in labels['po_numbers']:
            start = email_text.find(po)
            if start != -1:
                end = start + len(po)
                add_entity(start, end, 'PO_NUMBER')

        for part in labels['part_numbers']:
            start = email_text.find(part)
            if start != -1:
                end = start + len(part)
                add_entity(start, end, 'PART_NUMBER')

        for quantity in labels['quantities']:
            start = email_text.find(str(quantity))
            if start != -1:
                end = start + len(str(quantity))
                add_entity(start, end, 'QUANTITY')

        tracking_number = labels['tracking_number']
        start = email_text.find(tracking_number)
        if start != -1:
            end = start + len(tracking_number)
            add_entity(start, end, 'TRACKING_NUMBER')

        train_data.append((email_text, {"entities": entities}))

    return train_data

# Create training data
train_data = create_training_data(data)

# Convert to spaCy DocBin format
doc_bin = DocBin()
for text, annotations in train_data:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    doc_bin.add(example.reference)

# Save the training data to disk
doc_bin.to_disk("./train.spacy")
