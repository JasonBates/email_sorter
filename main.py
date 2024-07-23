from config.config import EMAIL_HOST, EMAIL_PASSWORD, EMAIL_USER, EMAIL_ADDRESS, OPENAI_API_KEY
from email_fetcher.email_utils import email_2_dict
from email_fetcher.client import EmailClient
import itertools

# setup email client and login
email_client = EmailClient(EMAIL_ADDRESS, EMAIL_HOST, EMAIL_USER, EMAIL_PASSWORD)
email_client.connect()

# get the list of emails from the INBOX folder
email_client.select_folder('INBOX')
message_IDs = email_client.get_all_email_IDs()
messages = email_client.get_email_content(message_IDs)

# extract messages to a dictionary I can iterate over
email_messages = email_2_dict(messages)

# Create an LLM connection to the LLM service (e.g., OpenAI)
llm_connection = LLMservice(OPEN_API_KEY)

# send email messages to the LLM service for classification
# classified_emails = classify_emails(llm_connection, email_messages)

# move the emails with message ID to inbox with label provided by LLM
# for classified_email in classified_emails:
#     email_client.move_email(classified_email['message_id'], 'INBOX', classified_email['label'])


# print messages from dictionary to test
for message_ID, message_metadata in itertools.islice(email_messages.items(), 3):
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