from config.config import EMAIL_HOST, EMAIL_PASSWORD, EMAIL_USER, EMAIL_ADDRESS
from email_fetcher.email_utils import email_2_dict
from email_fetcher.client import EmailClient
import pprint

print(EMAIL_ADDRESS)

print(f"email_agent/client.py running with email address {EMAIL_ADDRESS}")
# setup email client and login
email_client = EmailClient(EMAIL_ADDRESS, EMAIL_HOST, EMAIL_USER, EMAIL_PASSWORD)
email_client.connect()

# get the list of emails from the INBOX folder
email_client.select_folder('INBOX')
message_IDs = email_client.get_all_email_IDs()
messages = email_client.get_email_content(message_IDs)

# print out a few to test the connection using func from email_utils
email_messages = email_2_dict(messages)

for message_ID, message_details in email_messages.items():
    print(message_ID)
    print("From:", message_details['from'])
    print("Subject:", message_details['subject'])
    print("Date:", message_details['date'])
    print("---------------------------------")

# disconnect... bye bye
email_client.disconnect()