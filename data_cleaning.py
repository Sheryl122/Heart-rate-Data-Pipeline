def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    #loop over the data and remove any values that are not integers or are outside of a reasonable range (e.g., 30-220 bpm)
    #if statements
    """
    cleaned_values = []
    missing_values = []

    for item in data:
        if item.isdigit() and 30 <= int(item) <= 220:
            cleaned_values.append(int(item))
        else:
            missing_values.append(item)
    
    return cleaned_values, missing_values