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
    
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"

            invitation = invitation.replace("{" + key + "}", str(value))

        output_filename = f"output_{index}.txt"
        try:
            if os.path.exists(output_filename):
                print(f"warning: {output_filename} already exist and should erased")

            with open(output_filename, 'w') as outfile:
                outfile.write(invitation)
            print(f"File generated: {output_filename}")
        except Exception as e:
            print(f"Error when writing on file {output_filename}:{e}")

    
        try:
            with open('template.txt', 'r') as file:
                template_content = file.read()
        except FileNotFoundError:
            print("Error: file template.txt is not found")
            template_content = ""

        attendees = [
            {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
            {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
            {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
        ]

    if __name__ == "__main__":
        generate_invitations(template_content, attendees)
