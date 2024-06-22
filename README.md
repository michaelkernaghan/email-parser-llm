# Email Parsing with LLM Integration

## Project Overview

This project provides an automated solution to parse shipment notification emails and extract relevant details using a Large Language Model (LLM) and a custom Named Entity Recognition (NER) model. The extracted details are validated and processed through mock ERP and accounting systems. The primary motivation is to streamline the workflow for companies handling numerous shipment notifications, reducing manual data entry and potential errors.

## Motivation

A printed circuit board (PCB) contract manufacturer handles a significant volume of incoming shipment notifications from various suppliers. These emails contain critical information that needs to be processed promptly to maintain efficient operations. The current manual process is time-consuming and prone to errors. This project aims to automate the extraction and validation of shipment details, thus improving efficiency and accuracy.

## Introduction to spaCy and Named Entity Recognition (NER)

### spaCy

#### History and Overview
spaCy is an open-source library for Natural Language Processing (NLP) in Python, developed by Explosion AI. It was first released in 2015 and has since become one of the most popular NLP libraries due to its efficiency and ease of use. spaCy is designed specifically for production use and provides a robust framework for processing large volumes of text quickly.

#### Capabilities
spaCy offers a wide range of features including:
- Tokenization: Breaking down text into individual words and punctuation.
- Part-of-Speech Tagging: Identifying the grammatical parts of speech for each token.
- Dependency Parsing: Analyzing the grammatical structure of a sentence.
- Named Entity Recognition (NER): Identifying and classifying named entities in text.
- Text Classification: Categorizing text into predefined categories.
- Lemmatization: Reducing words to their base or root form.

#### Why spaCy?
spaCy is chosen for this project because of its high performance, extensive functionality, and ease of integration. It provides pre-trained models for various languages and tasks, which can be fine-tuned for specific needs. Additionally, spaCy's pipeline design allows for easy customization and extension, making it ideal for building and deploying NLP solutions in production environments.

### Named Entity Recognition (NER)

#### What is NER?
Named Entity Recognition (NER) is a subtask of information extraction that seeks to locate and classify named entities in text into predefined categories such as names of persons, organizations, locations, dates, and other entities. NER is crucial for understanding the context and extracting meaningful information from text.

#### History and Development
NER has been a significant focus in NLP research since the 1990s, with early systems relying on handcrafted rules and dictionaries. The development of machine learning algorithms, particularly Conditional Random Fields (CRFs) and deep learning methods, has significantly improved the accuracy and robustness of NER systems. Modern NER models leverage large annotated corpora and advanced neural network architectures to achieve state-of-the-art performance.

#### Why Use NER in This Project?
In the context of this project, NER is used to identify and extract entities relevant to shipment notifications, such as purchase order (PO) numbers, part numbers, quantities, and tracking numbers. Automating this extraction process reduces manual data entry, minimizes errors, and improves operational efficiency.

#### Comparison with Other Machine Learning Solutions
- **Rule-Based Systems**: While rule-based systems can be highly accurate for specific tasks, they lack the flexibility and scalability of machine learning models. They require extensive manual effort to create and maintain rules, making them less suitable for dynamic and diverse datasets.
- **Traditional Machine Learning Models**: Models such as CRFs and Support Vector Machines (SVMs) have been widely used for NER. However, they often require extensive feature engineering and may not perform as well as modern deep learning approaches.
- **Deep Learning Models**: Recent advancements in deep learning, particularly models like BERT and GPT, have significantly improved NER performance. These models can capture complex patterns and dependencies in text without the need for extensive feature engineering. spaCy supports integration with deep learning frameworks, making it a versatile choice for NER tasks.

Overall, spaCy and NER are chosen for their robustness, performance, and ease of use, providing a comprehensive solution for extracting and processing critical information from shipment notification emails.


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

This will create a labeled_test_emails.json file containing 30 test emails. Note that this is a simplification for the purpose of this project. In practice, email content can vary widely in structure and format.

## Prompt Engineering Example

Prompt engineering involves crafting inputs (prompts) to large language models (LLMs) like GPT-4 to achieve desired outputs. Effective prompt engineering can significantly enhance the performance and reliability of LLMs in various tasks, including text extraction, summarization, and more.

### Why Prompt Engineering?
- Flexibility: Allows you to adapt the model for a wide range of tasks without extensive retraining.
- Ease of Use: Minimal coding required to implement complex tasks.
- Efficiency: Quickly iterate and test different prompts to optimize performance.

### Steps to Optimize Prompts
- Define Clear Instructions: Ensure the prompt clearly states what information to extract.
- Provide Context: Include necessary context to help the model understand the task.
- Iterate and Test: Experiment with different phrasings and structures to improve accuracy.

### Benefits of Prompt Engineering in This Project
- Rapid Development: Quickly develop and test the email parsing functionality.
- Adaptability: Easily adjust prompts to handle different email formats and content variations.
- Reduced Complexity: Simplifies the integration of advanced NLP capabilities without extensive custom coding.

Run 
```sh 
email-parser.py
```
to see how an OPENAI LLM can be used to parse emails.

## Learning Model

### Current Approaches and Orchestration of Tasks with LLM Agents

In the realm of modern AI, large language models (LLMs) like OpenAI's GPT-4 have become powerful tools for a variety of NLP tasks. These models can perform tasks such as text generation, summarization, translation, and more, with minimal coding required. This paradigm, often referred to as "no-code" or "low-code" AI, enables users to orchestrate complex workflows using pre-trained models and APIs without needing to delve deeply into the specifics of model training and feature engineering.

In this project, the use of GPT-4 for parsing emails represents this modern, no-code approach. By leveraging an LLM, we can quickly prototype and implement solutions that understand and extract relevant information from text. The benefits of this approach include:
- **Ease of Use**: With pre-trained models, there's no need for extensive training or hyperparameter tuning.
- **Flexibility**: LLMs can handle a wide range of tasks and can be adapted to different contexts with minimal changes.
- **Rapid Development**: Solutions can be developed and deployed quickly, which is ideal for projects with tight timelines or limited resources.

### Contrast with Custom NER Models

While LLMs offer a flexible and general-purpose approach, custom Named Entity Recognition (NER) models like those trained using spaCy provide a more targeted and specialized solution. NER models are specifically designed to extract structured information from text, making them ideal for tasks where precision and domain-specific knowledge are critical.

#### Custom NER Models
- **Specialization**: Custom NER models can be fine-tuned to recognize specific entities relevant to the task at hand, such as PO numbers, part numbers, quantities, and tracking numbers in shipment emails.
- **Efficiency**: Once trained, NER models can be very efficient in terms of processing speed and resource utilization.
- **Control**: Developers have more control over the training process, allowing for optimization and adjustment based on specific needs and feedback.

In this project, the NER model is trained using labeled data to recognize entities specific to shipment notifications. This targeted approach ensures high accuracy and reliability in extracting the necessary information, in contrast with the more flexible but generalized capabilities of the LLM.

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
├── README.md                  # Project documentation
```

## Detailed Explanation of Key Files

### generate_test_emails.py
This script generates a set of test emails with varying content while maintaining the form. It saves the emails in labeled_test_emails.json file. Note that this is a simplification for the purpose of this project. In practice, email content can vary widely in structure and format.

### convert-test-data.py
This script converts the labeled test emails into a format suitable for training an NER model using spaCy. It ensures that there are no overlapping entity annotations and saves the data in the train.spacy file.

### learning-model.py
This script trains a custom NER model using the labeled data. The model is trained to recognize entities such as PO numbers, part numbers, quantities, and tracking numbers. The trained model is saved in the trained_model directory.

### use_trained_model.py
This script demonstrates how to use the trained NER model to extract entities from new emails. It processes the email text and prints the extracted entities.

### test_emails.json
This file contains the generated test emails and is used by the parser.py script for processing.
