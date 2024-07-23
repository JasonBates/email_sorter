from config.config import EMAIL_HOST, EMAIL_PASSWORD, EMAIL_USER, EMAIL_ADDRESS, OPENAI_API_KEY
from email_fetcher.email_utils import email_2_dict
from email_fetcher.client import EmailClient
from LLM.LLM import LLMService
import pprint
import itertools
import json

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
email_doc = json.dumps(email_messages)
# ====== FIRE UP THE LLM ========

# Create an LLM connection to the LLM service (e.g., OpenAI)
llm = LLMService(OPENAI_API_KEY)

classification_prompt = """ 

# Purpose

You are an email classification assistant. Given a list of emails please classify these emails into the following
groups according to the criteria provided:

## Newsletters
- Emails that are regular updates from a source about topics such as technology, finance, health, or lifestyle.
- They are often a sequence of unrelated stories of the week about a particular theme 
- Those stories often have headlines and then a news story
- regular newsletters I receive include messages from:
    - tim ferris
    - readwise
    - Examine
    - Early retirement
    - the daily skim
    - morning brew 
    ...and others

## Personal
- These tend to be text notes that address me by name and are asking a question, letting me know about something
confirming a meeting, or sending me a file or information that's important.
- they tend to be from individuals rather than companies
they don't tend to be sales messages or have lots of graphics, 

## Adverts
- They are trying to sell me something
- They are often trying to get me to buy a ticket to an event by telling me about the event
- They often mention discounts if I act quickly
- They use sales language to try to get me to buy a ticket, product, or service
- They are often from companies rather than individuals
- They are often HTML with graphics and images of the products they are selling

## Orders and receipts
- They refer to something I've purchased or an event I have already booked
- Often they confirm the order or charge or delivery of the item
- They are likely to include the price of the item or service I bought

# Output
- create a list of email subject lines for each grouping title
- Respond in json format but don't put '/n' in the answer

"""

result = llm.get_response_with_context_json(classification_prompt,email_doc)
pprint.pprint(result)

# send email messages to the LLM service for classification
# prompt = "Classify the following emails into categories:"
# email_filing_instructions = llm_connection.classify_emails(email_doc, prompt)

# ======= MOVE THE EMAILS TO THE RIGHT FOLDERS ========

# move the emails with message ID to inbox with label provided by LLM
# for message_id, target_folder in email_filing_instructions.items():
#     email_client.move_email(message_id, 'INBOX', target_folder)

# ======= CREATE A SUMMARY OF WHAT HAS MOVED WHERE ==========

# disconnect email server... bye bye
email_client.disconnect()
