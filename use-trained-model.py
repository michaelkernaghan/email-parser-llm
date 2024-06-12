import spacy

# Load the trained model
nlp = spacy.load("./trained_model")

# Define a function to process a new email and extract entities
def process_email(email_text):
    doc = nlp(email_text)
    extracted_entities = {
        "PO_NUMBER": [],
        "PART_NUMBER": [],
        "QUANTITY": [],
        "TRACKING_NUMBER": []
    }
    
    for ent in doc.ents:
        extracted_entities[ent.label_].append(ent.text)
    
    return extracted_entities

# Example new email
new_email = """
Hi Tom/Niall,
See below shipment:
| PO    | Part No.                                         | Pnl  |
|-------|--------------------------------------------------|------|
| 43875 | Catamount 8L RI Rev 1 & Catamount 8L REStripline | 5    |
| 43881 | PT-0037229 Rev A PT-0038573 Rev A                | 10   |
| 43884 | Dual Sensor V2.0                                 | 10   |
| 43882 | Panel_CAM81204140_01                             | 200  |
| 43885 | DA0961 SMTPA PCB V1P3                            | 50   |
DHL: 7322345656 
Vincent Lim
Sales Manager
<Attachment: Commercial Invoice 2269A>
"""

# Process the email and extract entities
extracted_entities = process_email(new_email)
print("Extracted Entities:")
print(extracted_entities)
