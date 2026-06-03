from datetime import datetime

def validate_task_title(title):
    # check if title has text
    if isinstance(title, str) and len(title.strip()) > 0:
        return True
    print("Error: Task title cannot be empty.")
    return False

def validate_task_description(description):
    # check if description has text
    if isinstance(description, str) and len(description.strip()) > 0:
        return True
    print("Error: Task description cannot be empty.")
    return False

def validate_due_date(due_date):
    # check if empty first
    if not isinstance(due_date, str) or len(due_date.strip()) == 0:
        print("Error: Due date cannot be empty.")
        return False

    # check if it is a real date layout
    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        print("Error: Due date must be a valid date in YYYY-MM-DD format.")
        return False

