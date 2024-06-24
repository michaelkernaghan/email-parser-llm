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
        if ent.label_ in extracted_entities:
            extracted_entities[ent.label_].append(ent.text)
    
    return extracted_entities

# Define the email content as a plain text string
email_text = """
From pcb design to pcb assembly, your most trustworthy partner

COMMERCIAL INVOICE Date: 2024/4/27
No.: 2024-1475-B004CI
To: Shipco Circuits Ltd. From: King Credie Technology Limited
Attn: Niall/Tom Attn: Spring
Tel: 353 26 41314 Tel: 0755-23110700
Fax: 353 26 42083 Fax: 0755-23110701

EORI Number: IE6362175L
Post Code: P12YD25
Departure: RM601, Block 5-A, Tongtai Times Center, Fuyong Town, Shenzhen City, 518103, China
Deliver to: BOWL ROAD, MACROOM, CO. CORK P12YD25, Ireland (DHL: 954403906)

PO No. Part No. Qty(pnl) Unit Price Tooling Freight Amount
PO43840 7564-C Sensor(10115) 500 0.120 88.00 0.00 148.00

Remark: Printed circuit board Total(USD): 148.00

Country of manufacture: China
HS Code: 8534009000

Yours sincerely,
KING CREDIE TECHNOLOGY LIMITED
Spring sales05@kingcredie.com
Mobile: 135 3812 2055
"""

# Process the email and print the extracted entities
extracted_entities = process_email(email_text)
print("Extracted Entities:")
print(extracted_entities)
