#!/usr/bin/python
"""
Created by Jocker271
------------------------------
Basic script for Secret Santa (aka wichteln)
"""

import csv
import os
import random
import smtplib
from email.mime.text import MIMEText

import config


def get_persons():
    with open(
        f"{os.path.dirname(__file__)}\\{config.INPUT_FILE}", newline=""
    ) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=";")
        next(csv_reader)
        persons = []
        for row in csv_reader:
            if len(row) >= 2:
                no_match = row[2] or False if len(row) >= 3 else False
                persons.append(
                    {"name": row[0], "mail": row[1], "no_match": no_match}
                )
        return persons


def get_matches(persons, loop_count=0):
    if loop_count > 100:  # prevent endless loop
        return False
    matches = {}
    not_matching = set()
    for x in persons:
        not_matching.add(x.get("name"))
        if x.get("no_match"):
            for l in x.get("no_match").split(","):
                not_matching.add(l.strip())
        matchable = [
            w["name"] for w in persons if w["name"] not in not_matching
        ]
        if len(matchable) >= 1:
            match = random.choice(matchable)
            matches[x["name"]] = match
            not_matching = set(list(matches.values()))
        else:
            return get_matches(persons, loop_count + 1)
    return matches


def load_template():
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, "index.html")
    template = open(file, encoding="utf-8", mode="r").read().replace("\n", "")
    template = template.replace("[xX-title-Xx]", config.MAIL_TITLE)
    template = template.replace("[xX-prefix-Xx]", config.MAIL_PREFIX)
    template = template.replace("[xX-suffix-Xx]", config.MAIL_SUFFIX)
    template = template.replace("[xX-gif-Xx]", config.MAIL_GIF)
    return template


def customize_message(template, wichtel, match):
    template = template.replace("[xX-wichtel-Xx]", wichtel.get("name"))
    template = template.replace("[xX-match-Xx]", match)
    msg = MIMEText(template, "html")
    msg["From"] = "%s <%s>" % (config.MAIL_FROM, config.MAIL_ACCOUNT_USERNAME)
    msg["To"] = ",".join([wichtel.get("mail")])
    msg["Subject"] = config.MAIL_SUBJECT
    return msg


def send_mails(persons, matches, template):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(
            config.MAIL_ACCOUNT_USERNAME, config.MAIL_ACCOUNT_PASSWORD
        )
        for wichtel in persons:
            mail_to = [wichtel.get("mail")]
            match = matches.get(wichtel.get("name"))
            msg = customize_message(template, wichtel, match)
            server.sendmail(
                config.MAIL_ACCOUNT_USERNAME, mail_to, msg.as_string()
            )
        server.quit()
        print("send mails successfully")
    except:
        print("failed to send mails")


def main():
    if not config.MAIL_ACCOUNT_USERNAME or not config.MAIL_ACCOUNT_PASSWORD:
        print("You have to setup the config.py first!")
        input("Press any Key to exit")
        return False
    persons = get_persons()
    matches = get_matches(persons)
    template = load_template()
    if matches:
        if not config.TESTMODE:
            send_mails(persons, matches, template)
        else:
            print(matches)
    else:
        print("failed while calculating matches")


if __name__ == "__main__":
    main()
