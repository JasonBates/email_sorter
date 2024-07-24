import pprint
import os
import json
from config.config import EMAIL_HOST, EMAIL_PASSWORD, EMAIL_USER, EMAIL_ADDRESS, OPENAI_API_KEY, ELEVENLABS_API_KEY
from emailer.client import EmailClient
from emailer.email_utils import email_2_dict
from LLM.LLM import LLMService
from voice.voice import VoiceService

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
all_email_content = json.dumps(email_messages)
# ====== FIRE UP THE LLM ========

# Create an LLM connection to the LLM service (e.g., OpenAI)
llm = LLMService(OPENAI_API_KEY)

# Fetch the prompt for the classification from prompt.md in the /LLM folder

file_path = os.path.join(os.path.dirname(__file__), 'LLM', 'prompt.md')

with open('LLM/prompt.md', 'r') as file:
    classification_prompt = file.read()
    
# send email messages to the LLM service for classification
result = llm.get_json_response_with_context(
    classification_prompt,
    all_email_content)

results_json = json.loads(result)
pprint.pprint(results_json)

# ======= MOVE THE EMAILS TO THE RIGHT FOLDERS ========

# get the classification scheme out of the results and file_away the emails accordingly
classification = results_json["Classified_Emails"]
email_client.file_away(classification)

# disconnect email server... bye bye
email_client.disconnect()

# ======= ANNOUNCE THE SUMMARY OF PERSONAL AND NEWSLETTERS ========

newsletter_summary_bits = results_json['newsletterSummary']['summary']
personal_summary_bits = results_json['personalEmailsSummary']['summary']
email_summary_script = " ".join(personal_summary_bits).join(newsletter_summary_bits)

voice = VoiceService(ELEVENLABS_API_KEY)
voice.set_voice("JBFqnCBsd6RMkjVDRZzb")
voice.stream_audio(voice.generate_audio_stream(email_summary_script))
