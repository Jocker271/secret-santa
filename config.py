#!/usr/bin/python

"""This file contains the settings of the secret santa script"""

# === General Settings ===
INPUT_FILE = "persons.csv"
TESTMODE = True  # don't send mail in testmode

# === Gmail Account ===
# Secret login data to Gmail account from Windows environment variables
# MAIL_ACCOUNT_USERNAME, MAIL_ACCOUNT_PASSWORD = os.environ.get('GMAIL_PYTHON_LOGIN').split()
MAIL_ACCOUNT_USERNAME = ""
MAIL_ACCOUNT_PASSWORD = ""

# === Mail ===
MAIL_FROM = "Jocker271"
MAIL_SUBJECT = "Dein Wichtel-Match 2023"
MAIL_TITLE = "It's a Match"
MAIL_PREFIX = "dein Wichtelmatch für dieses Jahr ist"
MAIL_SUFFIX = "PS: dieses Jahr darfst du 20€ ausgeben"
MAIL_GIF = "https://media3.giphy.com/media/6LWgndjhVe1HTb0pQi/giphy.gif?cid=ecf05e47whhnc3oq9eh3gw0xnmx4p86gbssths3lf6jsgaty&ep=v1_gifs_search&rid=giphy.gif&ct=g"
# "https://64.media.tumblr.com/23372bd0f4fda961a4bc44b6c9a31d1d/tumblr_ngv34sdk9M1s8njeuo1_540.gifv"
