from spacy_llm.util import assemble

nlp = assemble("config.cfg")
doc = nlp("You look gorgeous!")
print(doc.cats)
