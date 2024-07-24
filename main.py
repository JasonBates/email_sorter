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

# create a prompt for the classification
classification_prompt = """ 

# Purpose

You are an amazing email classification assistant. Given a list of emails, You will succeed if you can do 3 things listed below.
Try hard, thinking deeply about the challenges, creating a step by step strategy before you start. 

1) Go through the email and classify them emails into the groups I described below according to the criteria provided. 
As output for this challenge, create a list of email subject lines for each grouping title based on the intent of the sender
Read the emails and think about the intention of the sender, use that as the basis of classification.

## Newsletters - designed to inform me
- Emails that are regular updates from a source about topics such as technology, finance, health, or lifestyle.
- They are often a sequence of unrelated stories of the week about a particular theme 
- Those stories often have headlines and then a news story
- regular newsletters I receive include messages from:

## Personal - personal communications with friends and colleagues
- These tend to be text notes that address me by name and are asking a question, letting me know about something
confirming a meeting, or sending me a file or information that's important.
- they tend to be from individuals rather than companies
- they don't tend to be sales messages or have lots of graphics, 

## Adverts - trying to get me to buy a product, service, or ticket
- They are trying to sell me something with language like 'Buy now', 'book now', or 'special offer'
- They are often trying to get me to buy a ticket to an event by telling me about the event
- They often mention discounts especially if I act quickly
- They use typical sales language 
- They are often from companies rather than individuals
- They are often HTML with graphics and images of the products they are selling

## Orders and receipts - confirming a purchase I've already made
- They refer to something I've purchased or an event I have already booked
- Often they confirm the order or charge or delivery of the item
- They are likely to include the price of the item or service I bought

2) Give me a summary of the key point, requests, or actions required from the emails you classify as Personal emails. 
Respond in json that wraps paragraphs of text.

3) Give me a summary of the key stories in the emails you class as Newsletters in a way that I could read out to a friend or colleague.
Pull out the most interesting points, quotes, or stories, and keep the summary to under 500 tokens. Respond in json that wraps paragraphs of text.


# Final Output
- respond in JSON
- keep the responses to each of the three challenges separate
- Follow my instructions above

"""
# send email messages to the LLM service for classification
result = llm.get_response_with_context_json(classification_prompt, email_doc)

llm_response = json.loads(result)
pprint.pprint(llm_response)

# SUCCESS!!! 

# ======= MOVE THE EMAILS TO THE RIGHT FOLDERS ========

# move the emails with message ID to inbox with label provided by LLM
# for message_id, target_folder in email_filing_instructions.items():
#     email_client.move_email(message_id, 'INBOX', target_folder)

# ======= CREATE A SUMMARY OF WHAT HAS MOVED WHERE ==========

# disconnect email server... bye bye
email_client.disconnect()
