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
            print("Error: Each element of attendees must be a dictionary")
            return
        
    if template.strip() == "":
        print("Template is empty, no output files generated")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated")
        return
    
    placeholders = ["name", "event_title", "even_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"

