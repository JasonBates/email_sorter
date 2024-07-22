from itertools import islice
import email
import pprint
from email.header import decode_header, make_header
from html import unescape
from email.parser import BytesParser
import chardet

def email_test_print(messages, number = 10, lines = 10):
    for msg_id, data in islice(messages.items(), number):
        envelope = data[b'ENVELOPE']
        subject = envelope.subject.decode() if envelope.subject else ''
        from_field = f"{envelope.sender[0]}" if envelope.sender else ''
        body_bytes = data[b'BODY[]']
    
        message = BytesParser().parsebytes(body_bytes)

        body_text = ''

        print("content type", message.get_content_type())
        print("boundary string", message.get_boundary())
        
        if message.is_multipart() or 'multipart/' in message.get_content_type():
            print("Message is multipart")
            for part in message.walk():
                if part.get_content_type() == 'text/plain':
                    print(f"Processing text/plain")
                    try:
                        body_text = part.get_payload(decode=True).decode()
                        print("Found text/plain part, setting body_text")
                    except UnicodeDecodeError:
                        body_text = 'Unable to decode message body'
                        break
                elif part.get_content_type() == 'text/html' and not body_text:
                    try:
                        body_html = part.get_payload(decode=True).decode()
                        body_text = unescape(email.parser.Parser().parsestr(body_html).get_payload())
                        print("Found text/html part, setting body_text")
                    except UnicodeDecodeError:
                        body_text = 'Unable to decode message body'
                        break             
        else:
            try:
                body_text = message.get_payload(decode=True).decode()
                print('just text... ')
            except UnicodeDecodeError:
                result = chardet.detect(message.get_payload(decode=True))
                if result['encoding'] is not None:
                    try:
                        body_text = message.get_payload(decode=True).decode(result['encoding'])
                    except UnicodeDecodeError:
                        body_text = 'Unable to decode message body'
                else:
                    body_text = 'Unable to decode message body'
    
        body_lines = body_text.split('\n')
        first_x_lines = '\n'.join(body_lines[:lines])
    
        print("=======================================================")
        print(f"{msg_id}, subject: {subject}, \n from: {from_field} \n")
        print(f"First {lines} lines of text content:\n{first_x_lines}\n")
