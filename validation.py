# lab assignment: input validation functions
# description: check string lengths and date errors

from datetime import datetime

def validate_task_title(title):
    # check for empty length directly
    if len(title) == 0:
        print("Invalid choice. Please try again.")
        return False
    return True

def validate_task_description(description):
    # check for empty length directly
    if len(description) == 0:
        print("Invalid choice. Please try again.")
        return False
    return True

def validate_due_date(due_date):
    # check for empty length directly
    if len(due_date) == 0:
        print("Invalid choice. Please try again.")
        return False

    # check if the date raises a value error
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid choice. Please try again.")
        return False
