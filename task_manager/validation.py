# lab assignment: input validation functions
# details: checks text lengths and date formats

from datetime import datetime

# function to check task title
def validate_task_title(title):
    # make sure title is not empty
    if title is None or len(title.strip()) == 0:
        print("Invalid choice. Please try again.")
        return False
    return True

# function to check task description
def validate_task_description(description):
    # make sure description is not empty
    if description is None or len(description.strip()) == 0:
        print("Invalid choice. Please try again.")
        return False
    return True

# function to check due date
def validate_due_date(due_date):
    # make sure date is not empty
    if due_date is None or len(due_date.strip()) == 0:
        print("Invalid choice. Please try again.")
        return False

    # check for format errors using try except
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        print("Invalid choice. Please try again.")
        return False
