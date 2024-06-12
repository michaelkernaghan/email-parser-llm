import spacy
from spacy.tokens import DocBin
from spacy.training import Example
from spacy.util import minibatch, compounding

# Load the training data
doc_bin = DocBin().from_disk("./train.spacy")
train_docs = list(doc_bin.get_docs(spacy.blank("en").vocab))

# Create training examples
train_data = []
for doc in train_docs:
    example = Example.from_dict(doc, {"entities": [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]})
    train_data.append(example)

# Create a blank spaCy model
nlp = spacy.blank("en")

# Create a new NER component and add it to the pipeline
ner = nlp.add_pipe("ner")

# Add the labels to the NER component
for example in train_data:
    for ent in example.reference.ents:
        ner.add_label(ent.label_)

# Start the training
optimizer = nlp.begin_training()
for i in range(10):
    losses = {}
    batches = minibatch(train_data, size=compounding(4.0, 32.0, 1.001))
    for batch in batches:
        for example in batch:
            nlp.update([example], drop=0.35, losses=losses)
    print(f"Losses at iteration {i}: {losses}")

# Save the trained model
nlp.to_disk("./trained_model")
