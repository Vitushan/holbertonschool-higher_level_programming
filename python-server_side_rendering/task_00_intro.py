#!/usr/bin/python3


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
    if not isinstance(attendees, list):
        print('Invalid input: attendees must be a list of dictionaries.')
