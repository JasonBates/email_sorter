# STEPS TAKEN TO BUILD THE AI EMAIL SORTER
# SEE README.md FOR MORE DETAILS

1. DONE: create folder structure
2. DONE: create config and .env files to store credentials and load them into constants
3. DONE: create modules in the folders with __init__.py files
4. DONE: create files according to proposed folder structure
5. DONE: Create the config.py loader of the .env file in the config folder
6. DONE: create the email/client.py file and access the email credentials created by config.config
    NB. To run this and to be able to access the modules correctly you have to run the command:
    python3 -m email.client from the root folder of the project.. this runs the module from the correct place
7. DONE: created a wrapper EmailClient for IMAPClient to make it easier to use, manage persistent connections and throw better errors
8. DONE: functions:
    email_client.connect()
    email_client.get_folder_list()
    email_client.select_folder()
    email_client.get_emails()
    email_client.process_email()
    email_client.disconnect()

9. DONE : Connect, select inbox, get emails, and print out the id and subject line of the inbox... then disconnect

10. DONE: OK, I can get the emails and print out the details using a little email_test_print 

11. DONE: fixed email_utils.py print emails to fix multipart messages .. caused by BODY.PEEK[TEXT]

12. DONE: Fixed problematic subject lines, crazy tuples of emoji !? 🤷

13. DONE: Fixed py linting issues ... with # type: ignore which feels a bit dirty, but works. Look more into that

======

12. TODO: rather than printing out the email messages, create and return a dictionary that contains the email. envelope details, message ID, message body, time / date, etc. .. and test that with messages called from main.py

12. TODO: move the smart bit from printing the email to a separate function so that I can start on the LLM part of the codebase
