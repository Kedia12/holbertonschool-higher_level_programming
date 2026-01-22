def say_my_name(first_name, last_name=""):
    """Returns a string with the given first name and last name.

    If the last name is not provided, it returns only the first name.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person. Defaults to "".

    Returns:
        str: A string containing the full name or just the first name.
    """
    if last_name:
        return f"{first_name} {last_name}"
    return first_name
