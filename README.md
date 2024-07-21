# AI powered email sorter

- I'd like to create a python application that accesses an Imap email account, and reads, classifies, and moves email into appropriate folders in my inbox according to whether the email is a personal communication, a newsletter, a marketing / sales letter, or something else

1. Start with the Email Client Module and test it independently by connecting to your email account and listing/fetching emails.
2. Implement the Text Extraction Module and test it with sample email content.
3. Set up the Language Model Module and test it with sample text inputs.
4. Develop the Email Classification Module and test it with sample email text and LLM outputs.
5. Integrate all the modules into the Main Application Module and test the end-to-end workflow.

Throughout the development process, ensure that you follow best practices such as writing unit tests, handling exceptions, and logging errors and debug messages.

Here's a suggested structure and a list of targets for what to code:

1. **Email Client Module**
    - Create a class to handle email client operations (e.g., `EmailClient`)
    - Implement methods to connect to the IMAP server and authenticate
    - Implement methods to list emails in the inbox
    - Implement methods to fetch email content (subject, body, attachments)
    - Implement methods to move emails to specific folders

2. **Text Extraction Module**
    - Create a function or a class to extract plain text content from email bodies and attachments
    - Handle different email formats (HTML, plain text, etc.)
    - Normalize and clean the extracted text (remove unwanted characters, formatting, etc.)

3. **Language Model Module**
    - Create a class or a set of functions to interact with the OpenAI API (or any other LLM provider)
    - Implement methods to send text to the LLM and receive the classification result
    - Handle any necessary preprocessing or postprocessing of the text for the LLM

4. **Email Classification Module**
    - Create a class or a set of functions to handle email classification
    - Implement methods to preprocess the email text (e.g., remove signatures, disclaimers)
    - Implement methods to classify emails based on the LLM output
    - Define the classification categories (personal, newsletter, marketing, etc.)

5. **Main Application Module**
    - Create the main entry point for your application
    - Import and use the classes and functions from the other modules
    - Implement the main loop to process emails, classify them, and move them to appropriate folders

6. **Configuration and Utilities**
    - Create a configuration module to store sensitive information (e.g., email account credentials, API keys)
    - Create utility functions for logging, error handling, and other common tasks

---

Here's what each directory and file would contain:

- `config/`: This directory would hold your configuration files, such as `config.py`, which would store sensitive information like email account credentials and API keys.
- `email/`: This directory would contain modules related to email operations.
    - `client.py`: This file would contain the `EmailClient` class for connecting to the IMAP server, listing emails, fetching email content, and moving emails to folders.
    - `utils.py`: This file could contain utility functions related to email operations, if needed.
- `language_model/`: This directory would contain modules for interacting with the LLM (OpenAI or others).
    - `openai_model.py`: This file would contain a class or functions for sending text to the OpenAI API and receiving the classification result.
- `classification/`: This directory would contain modules for email classification.
    - `classifier.py`: This file would contain a class or functions for preprocessing email text, handling LLM output, and classifying emails into categories.
- `utils/`: This directory would contain utility modules.
    - `text_extraction.py`: This file would contain functions for extracting plain text from email bodies and attachments.
    - `logging.py`: This file would contain functions for logging messages and errors.
    - `exceptions.py`: This file would contain custom exception classes for your application, if needed.
- `tests/`: This directory would contain unit tests for each module.
    - `test_email_client.py`: This file would contain tests for the `EmailClient` class.
    - `test_text_extraction.py`: This file would contain tests for the text extraction functions.
    - `test_openai_model.py`: This file would contain tests for the OpenAI model integration.
    - `test_classifier.py`: This file would contain tests for the email classification module.
- `main.py`: This file would be the main entry point for your application, where you would import and use the classes and functions from the other modules to run the email classification process.
- `requirements.txt`: This file would list all the Python dependencies required for your project.
- `README.md`: This file would provide documentation and instructions for setting up and running your project.

project/
├── __init__.py
├── config/
│   ├── __init__.py
│   └── config.py
├── email_agent/
│   ├── __init__.py
│   ├── client.py
│   └── utils.py
├── language_model/
│   ├── __init__.py
│   └── openai_model.py
├── classification/
│   ├── __init__.py
│   └── classifier.py
├── utils/
│   ├── __init__.py
│   ├── text_extraction.py
│   ├── logging.py
│   └── exceptions.py
├── tests/
│   ├── __init__.py
│   ├── test_email_client.py
│   ├── test_text_extraction.py
│   ├── test_openai_model.py
│   └── test_classifier.py
├── main.py
├── requirements.txt
└── README.md


This structure follows the principles of modularity and separation of concerns, making it easier to develop, test, and maintain each component independently. Additionally, it allows for easy integration and testability of the overall application.

