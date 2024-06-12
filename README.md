# Email Parser with LLM Integration

## Project Overview

This project provides an automated solution to parse shipment notification emails and extract relevant details using a Large Language Model (LLM) and a custom Named Entity Recognition (NER) model. The extracted details are validated and processed through mock ERP and accounting systems. The primary motivation is to streamline the workflow for companies handling numerous shipment notifications, reducing manual data entry and potential errors.

## Motivation

A printed circuit board (PCB) contract manufacturer handles a significant volume of incoming shipment notifications from various suppliers. These emails contain critical information that needs to be processed promptly to maintain efficient operations. The current manual process is time-consuming and prone to errors. This project aims to automate the extraction and validation of shipment details, thus improving efficiency and accuracy.

## Features

- **Automated Email Parsing**: Uses OpenAI's GPT-4 model to extract shipment details from email content.
- **Custom NER Model**: Trains a custom Named Entity Recognition (NER) model using spaCy to extract entities from emails.
- **Data Validation**: Validates extracted details against mock ERP and accounting systems.
- **Mock System Integration**: Demonstrates integration with ERP and accounting systems through mock implementations.
- **Environment Configuration**: Uses a `.env` file to manage sensitive information such as API keys.

## Getting Started

### Prerequisites

Ensure you have the following installed:

```sh
- Python 3.8+
- pip
```

Install the required Python libraries:

```sh
pip install spacy openai requests python-dotenv
python -m spacy download en_core_web_sm
```

### Setup
Clone the Repository:
```sh
git clone https://github.com/michaelkernaghan/email-parser-llm.git
cd email-parser-llm
```

Create a .env file in the project directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```
## Generate Test Emails:
Run the script to generate test emails:
```sh
python generate_test_emails.py
```

This will create a labeled_test_emails.json file containing 30 test emails.

# Prompt Engineering Example

run 
```sh 
email-parser.py
```
to see how an OPENAI LLM can be used to parse emails.

# Learning Model

Here we train the system to learn the features of inco,ing emails and to produce a usable output when given new unseen examples.

## Convert Test Emails to Labeled Data:
Run the script to convert test emails to the labeled data format required for training the NER model:
```sh
python convert-test-data.py
```

This will create a train.spacy file.

## Train the Custom NER Model:
Run the script to train the custom NER model:

```sh
python learning-model.py
```

This will train the model and save it in the trained_model directory.

## Use the Trained Model:
Run the script to use the trained model to extract entities from new emails:

```sh
python use_trained_model.py
```
## File Structure
```bash
email-parser-llm/
│
├── generate_test_emails.py    # Script to generate test emails
├── convert-test-data.py       # Script to convert test emails to labeled data for training
├── learning-model.py          # Script to train the custom NER model
├── use_trained_model.py       # Script to use the trained NER model
├── labeled_test_emails.json   # Generated test emails with labels
├── train.spacy                # Labeled data in spaCy format
├── .env                       # Environment variables (API keys)
├── requirements.txt           # List of required Python libraries
├── README.md                  # Project documentation

```
## Detailed Explanation of Key Files
### generate_test_emails.py
This script generates a set of test emails with varying content while maintaining the form. It saves the emails in labeled_test_emails.json file.

### convert-test-data.py
This script converts the labeled test emails into a format suitable for training an NER model using spaCy. It ensures that there are no overlapping entity annotations and saves the data in train.spacy file.

### learning-model.py
This script trains a custom NER model using the labeled data. The model is trained to recognize entities such as PO numbers, part numbers, quantities, and tracking numbers. The trained model is saved in the trained_model directory.

### use_trained_model.py
This script demonstrates how to use the trained NER model to extract entities from new emails. It processes the email text and prints the extracted entities.

### test_emails.json
This file contains the generated test emails and is used by the parser.py script for processing.

### .env
This file stores sensitive information like the OpenAI API key. Ensure this file is added to .gitignore to prevent it from being tracked by version control.

### requirements.txt
List of required Python libraries:
```sh
spacy
openai
requests
python-dotenv
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.