def cap_text(text):
    """
    Capitalizes the first letter of the input text.
    
    Args:
        text (str): The input string to be capitalized.
        
    Returns:
        str: The input string with the first letter capitalized.
    """
    if not text:
        return ""
    return text[0].upper() + text[1:]