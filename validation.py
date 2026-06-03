# lab assignment: validation functions
# purpose: check task data constraints

from datetime import datetime

def validate_task_title(title):
    # strict text match check for length
    if len(title) == 0:
        print("Invalid choice. Please try again.")
        return False
    return True

def validate_task_description(description):
    # strict text match check for length
    if len(description) == 0:
        print("Invalid choice. Please try again.")
        return False
    return True

def validate_due_date(due_date):
    # check for empty text string
    if len(due_date) == 0:
        print("Invalid choice. Please try again.")
        return False

    # check date structure for error handling match
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid choice. Please try again.")
        return False
