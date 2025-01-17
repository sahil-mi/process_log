# Log Processing Project

This is a Python project for processing log files to extract error messages. The script `main.py` reads log content and extracts error messages, counts the total number of errors, and provides a list of unique error messages.

## Setup

### Prerequisites
Make sure you have Python3 installed.


### Install Dependencies
No dependencies need to be installed

### Running the Script
 ```shell
python3 process_log.py
```
### Running Tests
```shell
python3 test.py
```
###  Known limitations
- The current implementation assumes that the log entries strictly follow the pattern of [YYYY-MM-DD HH:MM:SS] ERROR: <message>. If the log format changes the script may not work correctly.
- Processing very large log  may result in performance issues.
### Improvement Suggestions
- Optimization for large size files.
### Scaling Considerations
- Check the memory usage
- Read data from a file
- Integrate with database


