import spacy
import json

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

# Define a function to process all emails in the test email set
def process_all_emails(json_file):
    with open(json_file, 'r') as f:
        emails = json.load(f)

    all_extracted_entities = []
    for email in emails:
        print(f"Processing email from {email['sender']} to {email['recipient']}")
        extracted_entities = process_email(email['body'])
        all_extracted_entities.append({
            "sender": email['sender'],
            "recipient": email['recipient'],
            "extracted_entities": extracted_entities
        })
    
    return all_extracted_entities

# Specify the JSON file containing the test emails
json_file = 'test_emails.json'

# Process all the emails and print the extracted entities
all_extracted_entities = process_all_emails(json_file)
print("Extracted Entities from all emails:")
print(json.dumps(all_extracted_entities, indent=2))
