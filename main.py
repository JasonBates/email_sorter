from config.config import EMAIL_HOST, EMAIL_PASSWORD, EMAIL_USER, EMAIL_ADDRESS, OPENAI_API_KEY
from email_fetcher.email_utils import email_2_dict
from email_fetcher.client import EmailClient
import itertools

# ======= GET THE EMAILS =========

# setup email client and login
email_client = EmailClient(EMAIL_ADDRESS, EMAIL_HOST, EMAIL_USER, EMAIL_PASSWORD)
email_client.connect()

# get the list of emails from the INBOX folder
email_client.select_folder('INBOX')
message_IDs = email_client.get_all_email_IDs()
messages = email_client.get_email_content(message_IDs)

# extract messages to a dictionary I can iterate over
email_messages = email_2_dict(messages)

# Concatenate all the email content into a single string for classification
# email_doc = create_context(email_messages)

# ====== FIRE UP THE LLM ========

# Create an LLM connection to the LLM service (e.g., OpenAI)
# llm = LLM(api_key="OPEN_API_KEY")
# llm.connect()

# send email messages to the LLM service for classification
# prompt = "Classify the following emails into categories:"
# email_filing_instructions = llm_connection.classify_emails(email_doc, prompt)

# ======= MOVE THE EMAILS TO THE RIGHT FOLDERS ========

# move the emails with message ID to inbox with label provided by LLM
# for message_id, target_folder in email_filing_instructions.items():
#     email_client.move_email(message_id, 'INBOX', target_folder)

# ======= CREATE A SUMMARY OF WHAT HAS MOVED WHERE ==========


# print messages from dictionary to test
for message_ID, message_metadata in itertools.islice(email_messages.items(), 1):
    print(message_ID)
    print("From:", message_metadata['from'])
    print("Subject:", message_metadata['subject'])
    print("Date:", message_metadata['date'])
    print("Body:", message_metadata['body'])
    print("---------------------------------")

# disconnect LLM service
# llm_connection.close()

# disconnect email server... bye bye
email_client.disconnect()