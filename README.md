
# Email Parser with LLM Integration

## Project Overview

This project provides an automated solution to parse shipment notification emails and extract relevant details using a Large Language Model (LLM). The extracted details are validated and processed through mock ERP and accounting systems. The primary motivation is to streamline the workflow for companies handling numerous shipment notifications, reducing manual data entry and potential errors.

## Motivation

A printed circuit board (PCB) contract manufacturer, handles a significant volume of incoming shipment notifications from various suppliers. These emails contain critical information that needs to be processed promptly to maintain efficient operations. The current manual process is time-consuming and prone to errors. This project aims to automate the extraction and validation of shipment details, thus improving efficiency and accuracy.

## Features

- **Automated Email Parsing**: Uses OpenAI's GPT-4 model to extract shipment details from email content.
- **Data Validation**: Validates extracted details against mock ERP and accounting systems.
- **Mock System Integration**: Demonstrates integration with ERP and accounting systems through mock implementations.
- **Environment Configuration**: Uses a `.env` file to manage sensitive information such as API keys.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip

Install the required Python libraries:

```sh
pip install openai requests python-dotenv
```

### Setup

#### Clone the Repository:

```sh
git clone https://github.com/michaelkernaghan/email-parser-llm.git
cd email-parser-llm
```

#### Create a `.env` File:

Create a `.env` file in the project directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

#### Generate Test Emails:

Run the script to generate test emails:

```sh
python generate_test_emails.py
```

This will create a `test_emails.json` file containing 30 test emails.

#### Run the Parser Script:

Execute the parser script to process the test emails:

```sh
python parser.py
```

## File Structure

```
email-parser-llm/
│
├── generate_test_emails.py    # Script to generate test emails
├── parser.py                  # Main script to parse and process emails
├── test_emails.json           # Generated test emails (after running generate_test_emails.py)
├── .env                       # Environment variables (API keys)
├── requirements.txt           # List of required Python libraries
├── README.md                  # Project documentation
```

## Detailed Explanation of Key Files

### `generate_test_emails.py`

This script generates a set of test emails with varying content while maintaining the form. It saves the emails in `test_emails.json` file.

### `parser.py`

This is the main script that:

- **Loads environment variables**: Uses `python-dotenv` to load the OpenAI API key.
- **Defines mock ERP and accounting systems**: These classes simulate the validation and processing of shipment details.
- **Calls the OpenAI GPT model**: Extracts shipment details from emails.
- **Processes the extracted details**: Validates and processes the details through the mock systems.

### `test_emails.json`

This file contains the generated test emails and is used by the `parser.py` script for processing.

### `.env`

This file stores sensitive information like the OpenAI API key. Ensure this file is added to `.gitignore` to prevent it from being tracked by version control.

### `requirements.txt`

List of required Python libraries:

- openai
- requests
- python-dotenv

## Contact

For questions or contributions, please contact:

- **Your Name**: Michael Kernaghan
- **Email**: michaelkernaghan@ecadabs.com
- **GitHub**: [michaelkernaghan](https://github.com/michaelkernaghan)

## License

This project is licensed under the MIT License. See the LICENSE file for details.