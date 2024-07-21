from itertools import islice
from email.parser import BytesParser
import chardet

def email_test_print(messages, number = 10, lines = 10):
    for msg_id, data in islice(messages.items(), number):
        envelope = data[b'ENVELOPE']
        subject = envelope.subject.decode() if envelope.subject else ''
        from_field = f"{envelope.sender[0]}" if envelope.sender else ''
    
        body_bytes = data[b'BODY[TEXT]']
    
        message = BytesParser().parsebytes(body_bytes)

        body_text = ''

        if message.is_multipart():
            for part in message.walk():
                if part.get_content_type() == 'text/plain':
                    try:
                        body_text = part.get_payload(decode=True).decode()
                    except UnicodeDecodeError:
                        body_text = 'Unable to decode message body'
                        break
        else:
            try:
                body_text = message.get_payload(decode=True).decode()
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

    
                
