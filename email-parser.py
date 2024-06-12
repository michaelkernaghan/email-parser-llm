import json
import openai
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Mock classes to simulate interaction with an ERP system and Xero for demonstration purposes
class ERPSystem:
    def validate(self, details):
        print("Validating with ERP system...")
        return True

    def create_grn(self, details):
        print("Creating GRN in ERP system...")
        print(f"Details: {details}")

class XeroSystem:
    def create_invoice(self, details):
        print("Creating payable invoice in Xero system...")
        print(f"Details: {details}")

# Initialize instances of the mock systems
erp_system = ERPSystem()
xero_system = XeroSystem()

# This function interacts with the OpenAI GPT model to extract structured data from an email text.
# It sets up the API key, sends a formatted prompt to the GPT model, and returns the parsed response.
def call_openai_gpt(prompt):
    openai.api_key = openai_api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts data from emails."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

# This function constructs a prompt for the GPT model to parse an email and extract specific shipment details.
# It processes the GPT response and converts it into a JSON object.
def parse_email_with_gpt(email_text):
    prompt = (
        "You will be given a shipment notification email. Extract the following details and provide them in JSON format:\n"
        "1. PO numbers (list of strings)\n"
        "2. Part numbers (list of strings)\n"
        "3. Quantities (list of integers)\n"
        "4. Tracking number (string)\n\n"
        "Email:\n"
        f"{email_text}\n\n"
        "Provide the details in the following JSON format:\n"
        "{\n"
        "  \"po_numbers\": [\"PO1\", \"PO2\", ...],\n"
        "  \"part_numbers\": [\"Part1\", \"Part2\", ...],\n"
        "  \"quantities\": [Quantity1, Quantity2, ...],\n"
        "  \"tracking_number\": \"TrackingNumber\"\n"
        "}"
    )
    response = call_openai_gpt(prompt)
    print(f"GPT raw response: {response}")
    try:
        details = json.loads(response)
    except json.JSONDecodeError:
        print("Failed to parse JSON response from GPT.")
        details = {}
    return details

# This function simulates the validation of shipment details with an ERP system.
# It is essential for ensuring that the data meets the ERP system's requirements before further processing.
def validate_with_erp(details):
    try:
        return erp_system.validate(details)
    except Exception as e:
        print(f"Error validating with ERP: {e}")
        return False

# This function simulates the validation of a tracking number.
# It is crucial for verifying the integrity and existence of the tracking information.
def validate_tracking_number(tracking_number):
    print(f"Mock validating tracking number: {tracking_number}")
    return True

# This function simulates the creation of a Goods Receipt Note (GRN) in an ERP system.
# It is necessary for documenting the receipt of goods in the system.
def create_grn(details):
    try:
        erp_system.create_grn(details)
    except Exception as e:
        print(f"Error creating GRN: {e}")

# This function simulates the creation of a payable invoice in the Xero system.
# It is needed for managing the financial transactions related to the shipment.
def create_payable_invoice(details):
    try:
        xero_system.create_invoice(details)
    except Exception as e:
        print(f"Error creating payable invoice: {e}")

# This function orchestrates the shipment processing workflow.
# It ensures that all necessary validations and creations are performed in the correct order.
def process_shipment(details):
    required_keys = ['po_numbers', 'part_numbers', 'quantities', 'tracking_number']
    missing_keys = [key for key in required_keys if key not in details]
    
    if missing_keys:
        print(f"Missing keys in the details: {missing_keys}")
        return
    
    if validate_with_erp(details):
        if validate_tracking_number(details['tracking_number']):
            create_grn(details)
            create_payable_invoice(details)

# This function processes a batch of test emails containing shipment notifications.
# It reads the emails from a JSON file, parses them, and initiates the shipment processing workflow for each email.
def process_test_emails(json_file):
    with open(json_file, 'r') as f:
        test_emails = json.load(f)
    
    for email in test_emails:
        print(f"Processing email from {email['sender']} to {email['recipient']}")
        shipment_details = parse_email_with_gpt(email['body'])
        process_shipment(shipment_details)

# Start processing the test emails from the specified JSON file
process_test_emails('test_emails.json')
