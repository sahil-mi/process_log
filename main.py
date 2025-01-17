import re
import unittest
def process_log_file(log_content=""):

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






class Test(unittest.TestCase):
    
    def test_case_1(self):
        log_content = """
        [2024-01-07 10:15:30] ERROR: Database connection failed
        [2024-01-07 10:15:35] INFO: Retry attempt 1
        [2024-01-07 10:15:40] ERROR: Database connection failed
        [2024-01-07 10:15:45] ERROR: Authentication failed
        """
        
        expected_output = {
            "total_errors": 3,
            "unique_error_messages": [
                "Authentication failed",
                "Database connection failed"
            ]
        }
        result = process_log_file(log_content)
        self.assertEqual(result, expected_output)
        
        
    def test_case_2(self):
        log_content = """
        [2024-01-07 10:15:30] ERROR: Memory overflow
        [2024-01-07 10:15:35] ERROR: Memory overflow
        """
        expected_output = {
            "total_errors": 2,
            "unique_error_messages": [
                "Memory overflow",
            ]
        }
        result = process_log_file(log_content)
        self.assertEqual(result, expected_output)
        
        
    def test_case_3(self):
        log_content = ""
        expected_output = {
            "total_errors": 0,
            "unique_error_messages": []
        }
        result = process_log_file(log_content)
        self.assertEqual(result, expected_output)




if __name__ == "__main__":
    unittest.main()