# STEPS TAKEN TO BUILD THE AI EMAIL SORTER
# SEE README.md FOR MORE DETAILS

1. ~~create folder structure~~
2. ~~create config and .env files to store credentials and load them into constants~~
3. ~~create modules in the folders with __init__.py files~~
4. ~~create files according to proposed folder structure~~
5. ~~Create the config.py loader of the .env file in the config folder~~
6. ~~create the email/client.py file and access the email credentials created by config.config~~
    ~~NB. To run this and to be able to access the modules correctly you have to run the command: ~~
    ~~python3 -m email.client from the root folder of the project.. this runs the module from the correct place~~
7. created a wrapper EmailClient for IMAPClient to make it easier to use, manage persistent connections and throw better errors
8. functions:
    email_client.connect()
    email_client.get_folder_list()
    email_client.select_folder()
    email_client.get_emails()
    email_client.process_email()
    email_client.disconnect()

9. DONE : Connect, select inbox, get emails, and print out the id and subject line of the inbox... then disconnect

10. OK, I can get the emails and print out the details using a little email_test_print 