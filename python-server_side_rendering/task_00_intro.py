def generate_invitations(template, attendees):
    # Check the template type
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Verify that attendees is a list of dicts.
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # verify if the template empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # veify if the list empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Treating everyone
    for index, person in enumerate(attendees, start=1):
        filled_template = template
        # Replace each placeholder with value or N/A
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = person.get(key)
            if value is None:
                value = "N/A"
            filled_template = filled_template.replace(f"{{{key}}}", str(value))
        
        # save the file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as f:
                f.write(filled_template)
        except Exception as e:
            print(f"Error writing to file {output_filename}: {e}")
