import unittest
from main import process_log
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
        result = process_log(log_content)
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
        result = process_log(log_content)
        self.assertEqual(result, expected_output)
        
        
    def test_case_3(self):
        log_content = ""
        expected_output = {
            "total_errors": 0,
            "unique_error_messages": []
        }
        result = process_log(log_content)
        self.assertEqual(result, expected_output)
        
    #Error case
    def test_case_4(self):
        log_content = 1234
        expected_output = "Log content is not a string"
        
        result = process_log(log_content)
        self.assertEqual(result, expected_output)




if __name__ == "__main__":
    unittest.main()