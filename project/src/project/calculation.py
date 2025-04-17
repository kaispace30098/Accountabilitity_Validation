def calculate_school_average(data):
    """
    Calculate the average of proficiency of a given school.
    Return 0 if there is no value
    """
    if not data:
        return 0
    else:
        return sum(data)/len(data) 