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
		Shipping invoice number:				20230623	
							
							
To:   Shipco Circuits Ltd.					Date:	2023/06/23	
          Bowl Road,							
          Macroom,							
          Co.Cork,							
          Ireland						               	
							
Tel: +353 26 41314		Delivery terms: EXW HK by DHL					
Fax: +353 26 42083      		(at your DHL account no:954403906)					
Attn:  Niall Kelleher		Payment terms: Net 30 days from invoice date					
							
Bare printed circuit boards							
							
     Order No. 	Description	REF No.	Quantity		 Unit price	 Amount	
							
43212	 F26510 Matcha vP1.2.0-20221221 	1074LE1152	56	PCS	3	168.00 	
							
				Total: USD		168.000 	
							
					Emily		
					         Authorized signature		
							
"""

# Process the email and print the extracted entities
extracted_entities = process_email(email_text)
print("Extracted Entities:")
print(extracted_entities)
