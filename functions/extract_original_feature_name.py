def extract_original(string):
    """
    Deleting characters from string, that are before fist underscore.
    """
    return string.rsplit('_', 1)[0]