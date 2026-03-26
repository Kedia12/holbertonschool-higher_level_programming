def generate_invitations(template, attendees):
    # 🔹 Vérification des types
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # 🔹 Vérifier template vide
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # 🔹 Vérifier liste vide
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # 🔹 Placeholders attendus
    keys = ["name", "event_title", "event_date", "event_location"]

    # 🔹 Traitement des attendees
    for i, attendee in enumerate(attendees, start=1):
        output = template

        for key in keys:
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            output = output.replace("{" + key + "}", str(value))

        # 🔹 Création fichier
        filename = f"output_{i}.txt"

        try:
            with open(filename, "w") as f:
                f.write(output)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")