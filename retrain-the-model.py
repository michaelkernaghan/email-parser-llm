import spacy
from spacy.training.example import Example
import random

# Load existing spaCy model
nlp = spacy.load("./trained_model")

# Create a new NER component
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")

# Add new labels to the NER component
labels = ["INVOICE_NUMBER", "DATE", "TRACKING_NUMBER", "PO_NUMBER", "PART_NUMBER", "QUANTITY", "TOTAL_AMOUNT"]
for label in labels:
    ner.add_label(label)

# Prepare the training data
TRAIN_DATA = [
    (
        "Shipping invoice number: 20230623\n\nTo: Shipco Circuits Ltd. Date: 2023/06/23\n"
        "Bowl Road,\nMacroom,\nCo.Cork,\nIreland\n\nTel: +353 26 41314 Delivery terms: EXW HK by DHL\n"
        "Fax: +353 26 42083 (at your DHL account no: 954403906)\nAttn: Niall Kelleher Payment terms: Net 30 days from invoice date\n\n"
        "Bare printed circuit boards\n\nOrder No. Description REF No. Quantity Unit price Amount\n"
        "43212 F26510 Matcha vP1.2.0-20221221 1074LE1152 56 PCS 3 168.00\n\nTotal: USD 168.000\n\nEmily\nAuthorized signature\n",
        {
            "entities": [
                (22, 30, "INVOICE_NUMBER"),
                (111, 121, "DATE"),
                (243, 261, "TRACKING_NUMBER"),
                (383, 388, "PO_NUMBER"),
                (389, 416, "PART_NUMBER"),
                (417, 427, "REF_NUMBER"),
                (428, 430, "QUANTITY"),
                (475, 482, "TOTAL_AMOUNT")
            ]
        }
    ),
    (
        "From pcb design to pcb assembly, your most trustworthy partner\n\nCOMMERCIAL INVOICE Date: 2024/4/27\n"
        "No.: 2024-1475-B004CI\nTo: Shipco Circuits Ltd. From: King Credie Technology Limited\n"
        "Attn: Niall/Tom Attn: Spring\nTel: 353 26 41314 Tel: 0755-23110700\nFax: 353 26 42083 Fax: 0755-23110701\n\n"
        "EORI Number: IE6362175L\nPost Code: P12YD25\nDeparture: RM601, Block 5-A, Tongtai Times Center, Fuyong Town, Shenzhen City, 518103, China\n"
        "Deliver to: BOWL ROAD, MACROOM, CO. CORK P12YD25, Ireland (DHL: 954403906)\n\n"
        "PO No. Part No. Qty(pnl) Unit Price Tooling Freight Amount\nPO43840 7564-C Sensor(10115) 500 0.120 88.00 0.00 148.00\n\n"
        "Remark: Printed circuit board Total(USD): 148.00\n\nCountry of manufacture: China\nHS Code: 8534009000\n\n"
        "Yours sincerely,\nKING CREDIE TECHNOLOGY LIMITED\nSpring sales05@kingcredie.com\nMobile: 135 3812 2055\n",
        {
            "entities": [
                (58, 68, "DATE"),
                (74, 91, "INVOICE_NUMBER"),
                (334, 344, "TRACKING_NUMBER"),
                (358, 365, "PO_NUMBER"),
                (366, 384, "PART_NUMBER"),
                (385, 388, "QUANTITY"),
                (437, 440, "TOTAL_AMOUNT")
            ]
        }
    )
]

# Disable other pipes during training to speed up the process
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    for itn in range(30):
        random.shuffle(TRAIN_DATA)
        losses = {}
        for text, annotations in TRAIN_DATA:
            example = Example.from_dict(nlp.make_doc(text), annotations)
            nlp.update([example], drop=0.35, losses=losses)
        print(f"Iteration {itn}, Losses: {losses}")

# Save the model
nlp.to_disk("./retrained_model")
