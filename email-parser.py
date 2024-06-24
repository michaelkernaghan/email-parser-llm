import openai
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

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
        "Provide the details in the following JSON format and ensure it is a valid JSON:\n"
        "{\n"
        "  \"po_numbers\": [\"PO1\", \"PO2\", ...],\n"
        "  \"part_numbers\": [\"Part1\", \"Part2\", ...],\n"
        "  \"quantities\": [Quantity1, Quantity2, ...],\n"
        "  \"tracking_number\": \"TrackingNumber\"\n"
        "}"
    )
    response = call_openai_gpt(prompt)
   # print(f"GPT raw response: {response}")  # Print the raw response for debugging
    
    # Attempt to clean and parse the JSON response
    try:
        # Ensure that the response is a valid JSON string
        response = response[response.find('{'):response.rfind('}')+1]  # Extract JSON part
        details = json.loads(response)
    except json.JSONDecodeError:
        print("Failed to parse JSON response from GPT.")
        details = {}
    return details

# This function processes a batch of test emails containing shipment notifications.
# It reads the emails from a plain text file, parses them, and prints the extracted details.
def process_test_emails_from_text(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    
    # Split the text into individual emails using a delimiter
    emails = text.split("---EMAIL_SEPARATOR---")
    
    for email in emails:
        email = email.strip()  # Remove leading and trailing whitespace
        if email:
            print("Processing email...")
            shipment_details = parse_email_with_gpt(email)
            print(f"Extracted Entities: {json.dumps(shipment_details, indent=2)}")

# Start processing the test emails from the specified plain text file
process_test_emails_from_text('test_emails.txt')
