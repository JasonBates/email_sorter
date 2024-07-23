"""
This module provides a function to print a summary of email messages.

The email_test_print function takes a dictionary of email messages and prints a summary
of each message, including the subject, sender, and the first few lines of the message body.
The function can handle both plain text and HTML message bodies.

Usage:
    messages = {...}  # A dictionary of email messages
    email_test_print(messages, number=5, lines=5)
"""

import email.parser
from itertools import islice
import email
from html import unescape
from email.header import decode_header
from email.parser import BytesParser
import chardet
from typing import Union

def decode_rfc2047(byte_like_subject_line):
    """
    Decode a Subject line encoded using RFC 2047.

    Args:
        byte_like_subject_line (bytes): The byte-like encoded Subject line.

    Returns:
        str: The decoded Subject line.
    """
    # Decode the byte-like object to a string
    encoded_text = byte_like_subject_line.decode('utf-8')
    # Decode the encoded header
    decoded_parts = decode_header(encoded_text)
    # Initialize an empty list to hold decoded strings
    decoded_string_parts = []
    # Process each part of the decoded header
    for part, charset in decoded_parts:
        if isinstance(part, bytes):
            if charset is not None:
                # Decode byte string to a regular string using the specified charset
                decoded_string_parts.append(part.decode(charset))
            else:
                # Decode byte string using utf-8 as default charset
                decoded_string_parts.append(part.decode('utf-8'))
        else:
            # Part is already a string (not bytes)
            decoded_string_parts.append(part)
    # Join all parts into a single string
    decoded_subject_line = ''.join(decoded_string_parts)
    return decoded_subject_line

def email_test_print(messages, number=10, lines=10):
    """
    Print a summary of email messages.

    Args:
        messages (dict): A dictionary containing email messages, where the keys are message IDs
                         and the values are dictionaries containing message data.
        number (int, optional): The maximum number of messages to return. Defaults to 10.
        lines (int, optional): The number of lines from the message body to print. Defaults to 10.

    Raises:
        None
    
    Returns:
        None
    """
    for msg_id, data in islice(messages.items(), number):
        # get the subject and from field from the ENVELOPE
        envelope = data[b'ENVELOPE']
        date_received = envelope.date if envelope.date else ''
        from_field = f"{envelope.sender[0]}" if envelope.sender else ''
        # decode tricky subject line with encoding of emojis and the like
        subject = decode_rfc2047(envelope.subject)

        # get the body of the message and decode it from BODY.PEEK[]
        body_bytes = data[b'BODY[]']
        message= BytesParser().parsebytes(body_bytes)
        body_text = ''

        # Go through multipart email and pull out the text with HTML as a fallback
        if message.is_multipart() or 'multipart/' in message.get_content_type():
            # print("Message is multipart")
            for part in message.walk():
                if part.get_content_type() == 'text/plain':
                    # print(f"Processing text/plain")
                    try:
                        body_text = part.get_payload(decode=True).decode() # type: ignore
                        # print("Found text/plain part, setting body_text")
                    except UnicodeDecodeError:
                        body_text = 'Unable to decode message body'
                        break
                elif part.get_content_type() == 'text/html' and not body_text:
                    try:
                        body_html = part.get_payload(decode=True).decode() # type: ignore[attr-defined]
                        body_text = unescape(email.parser.Parser().parsestr(body_html).get_payload()) # type: ignore
                        # print("Found text/html part, setting body_text")
                    except UnicodeDecodeError:
                        body_text = 'Unable to decode message body'
                        break
        else:
            try:
                body_text = message.get_payload(decode=True).decode() # type: ignore
                # print('just text... ')
            except UnicodeDecodeError:
                result = chardet.detect(message.get_payload(decode=True)) # type: ignore
                if result['encoding'] is not None:
                    try:
                        body_text = message.get_payload(decode=True).decode(result['encoding']) # type: ignore
                    except UnicodeDecodeError:
                        body_text = 'Unable to decode message body'
                else:
                    body_text = 'Unable to decode message body'

        body_lines = body_text.split('\n')
        first_x_lines = '\n'.join(body_lines[:lines])
        
        # this is where a dictionary needs to be returned and the printing stuff happens in main.py

        print("=======================================================")
        print(f"{msg_id} \nSubject: {subject} \nFrom: {from_field} \nDate: {date_received}")
        print(f"First {lines} lines of text content:\n")
        print("-------------------------------------------------------")
        print(f" {first_x_lines} \n")