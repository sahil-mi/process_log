import re
import unittest
def process_log(log_content):

    # initializing data
    data = {
        "total_errors":0,
        "unique_error_messages":[]
    }
    # handling log content is empty 
    if log_content == "":
        return data


    # The pattern to find the error message
    pattern = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}] ERROR:([^[]*)"
    
    # using the pattern to find all matches
    try:
        result = re.findall(pattern,log_content)
    except TypeError:
        return 'Log content is not a string'
    except Exception as e:
        return f"Something went wrong! - {e}"
    
    #removing whitespaces 
    result = [message.strip() for message in result]

    # calculating total errors and sorted error messages
    total_errors = len(result)
    #removing duplicates
    unique_error_messages = list(set(result))
    unique_error_messages.sort()

    #updating data
    data["total_errors"] = total_errors
    data["unique_error_messages"] = unique_error_messages
    

    return data






