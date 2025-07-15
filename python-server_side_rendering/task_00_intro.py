#!/usr/bin/python3


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
    if not isinstance(attendees, list):
        print('Invalid input: attendees must be a list of dictionaries.')

    if template.strip() == "":
        print("Template is empty, no output files generated.")

    if len(attendees) == 0:
        print("No data provided, no output files generated.")

    i = 1
    for attendee in attendees:
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        invitation = template.replace("{name}", name)
        invitation = invitation.replace("{event_title}", event_title)
        invitation = invitation.replace("{event_date}", event_date)
        invitation = invitation.replace("{event_location}", event_location)

        with open(f"output_{i}.txt", "w") as f:
            f.write(invitation)

        i +=1