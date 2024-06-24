from spacy_llm.util import assemble

nlp = assemble("config.cfg")
doc = nlp("Jack and Jill rode up the hill in Les Deux Alpes")
print([(ent.text, ent.label_) for ent in doc.ents])
