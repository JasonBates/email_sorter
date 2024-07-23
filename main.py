from config.config import EMAIL_HOST, EMAIL_PASSWORD, EMAIL_USER, EMAIL_ADDRESS
from email_fetcher.email_utils import email_test_print
from email_fetcher.client import EmailClient


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
email_test_print(messages, number = 50, lines = 3)

# disconnect... bye bye
email_client.disconnect()