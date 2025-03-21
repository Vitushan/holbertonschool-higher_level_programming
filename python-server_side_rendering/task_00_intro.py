#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    """
    generate invitation files from template and attendees
    """

    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries")
        return
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Each element of attendees must be a dictionary.")
            return