"""
Module to handle email client operations.
"""
from imapclient import IMAPClient
from  config.config import EMAIL_HOST, EMAIL_PASSWORD, EMAIL_USER, EMAIL_ADDRESS

class EmailClient:
    """
    Class to handle email client operations.
    """

    def __init__(self, address, host, user, password):
        """
        Initialize the EmailClient with the necessary credentials and server information.
        """
        self.host = host
        self.address = address
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        """
        Establish a connection with the email server and authenticate the user.
        throw error if connection fails with message
        """
        try:
            # Create an IMAPClient instance with the host
            self.connection = IMAPClient(self.host)
            # Login to the email server with the provided user and password
            self.connection.login(self.user, self.password)
            print(f"connected to email server {self.host}")
        except Exception as e:
            # If there is an error while connecting, print the error message and set the connection to None
            print(f"failed to connect to email server {self.host} with error {e}")
            self.connection = None

    def _ensure_connection(self):
        if not self.connection:
            self.connect()

    def get_folder_list(self):
        """
        If there is a connection to IMAP, get folder names
        return list of folder names
        """
        self._ensure_connection()
        try:
            if self.connection:
                return [mb[2] for mb in self.connection.list_folders()]
            else:
                print(f"There is no connection to {self.host} to get folder list from")
        except Exception as e:
            print(f"failed to get folder names from email server {self.host} with error {e}")
            return []

    def select_folder(self, folder):
        """
        Select the specified folder for fetching messages later
        """
        self._ensure_connection()
        try:
            if self.connection:
                self.connection.select_folder(folder)
            else:
                print(f"There is no connection to {self.host} to select folder {folder}")
        except Exception as e:
            print(f"failed to select folder {folder} from email server {self.host} with error {e}")

    def get_all_email_IDs(self, folder='INBOX'):
        """
        Retrieve a list of email objects from the specified folder.
        which is either specified here, or the default INBOX folder.
        """
        self._ensure_connection()
        try:
            if self.connection:
                self.connection.select_folder(folder)
                return self.connection.search('ALL')
            else:
                print(f"There is no connection to {self.host} to get emails from")
        except Exception as e:
            print(f"failed to get emails from email server {self.host} with error {e}")
            return []

    def get_email_content(self, email_id):
        """
        Get email content from the specified email id
        """
        self._ensure_connection()
        try:
            if self.connection:
                return self.connection.fetch(email_id, ['ENVELOPE', 'BODY.PEEK[]'])
            else:
                print(f"There is no connection to {self.host} to get email content from")
                return []
        except Exception as e:
            print(f"failed to get email content from email server {self.host} with error {e}")
            return []

    def move_emails(self, messages, target_folder):
        """
        Move specified messages to the target folder.
        """
        self._ensure_connection()
        try:
            if self.connection:
                self.connection.move(messages, target_folder)
                print(f"successfully moved messages to {target_folder}")
            else:
                print(f"There is no connection to {self.host} to move messages to {target_folder}")
        except Exception as e:
            print(f"failed to move messages to folder {target_folder} from email server {self.host} with error {e}")


    def file_away(self, classification):
        try:
            for email_id in classification["Newsletters"]:
                self.move_emails(email_id, "INBOX.Newsletters")
                print(f'Moved email {email_id} to Newsletters')
            for email_id in classification["Personal"]:
                self.move_emails(email_id, "INBOX.Personal")
                print(f'Moved email {email_id} to Personal')
            for email_id in classification["Orders and Receipts"]:
                self.move_emails(email_id, "INBOX.Receipts")
                print(f'Moved email {email_id} to Orders and Receipts')
            for email_id in classification["Adverts"]:
                self.move_emails(email_id, "INBOX.Adverts")
                print(f'Moved email {email_id} to Adverts')
        except Exception as e:
            print(f"The error is {e}")

    def disconnect(self):
        """
        Close the connection with the email server.
        """
        if self.connection:
            try:
                self.connection.logout()
                print(f"successfully logged out from email server {self.host}")
            except Exception as e:
                print(f"failed to logout from email server {self.host} with error {e}")
            finally:
                self.connection = None
