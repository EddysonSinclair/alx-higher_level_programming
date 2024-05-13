def reload_from_json(self, json):
    """Replace all attributes of the Student.

    Args:
        json (dict): The key/value pairs to replace attributes with.
    """
    for k, v in json.items():
        if hasattr(self, k):
            setattr(self, k, v)
        else:
            print(f"Attribute '{k}' does not exist in the Student class.")
