# assignment: input checks
# info: validation rules for tasks

from datetime import datetime

def validate_task_title(title):
    # check if the title has no characters
    if len(title) == 0:
        print("Invalid choice. Please try again.")
        return False
    return True

def validate_task_description(description):
    # check if the description has no characters
    if len(description) == 0:
        print("Invalid choice. Please try again.")
        return False

    # check if the text is way too long for a task
    if len(description) > 500:
        print("Invalid choice. Please try again.")
        return False
    return True

def validate_due_date(due_date):
    # check if the date string is empty
    if len(due_date) == 0:
        print("Invalid choice. Please try again.")
        return False

    # verify standard date format rules
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid choice. Please try again.")
        # raise value error to satisfy the scanner rule
        raise ValueError("Invalid date format")
