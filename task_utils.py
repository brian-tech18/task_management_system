# lab assignment: task utility functions
# details: functions to add, complete, view, and track tasks

from datetime import datetime
from validation import validate_task_title, validate_task_description, validate_due_date

# start with an empty tasks list
tasks = []

# function to add a new task
def add_task(title, description, due_date):
    # run all validation checks first
    if validate_task_title(title) and validate_task_description(description) and validate_due_date(due_date):
        # make the dictionary for the task
        new_task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        tasks.append(new_task)
        print("Task added successfully!")
        return True
    return False

# function to change a task to completed
def mark_task_as_complete(index, tasks=tasks):
    # catch any number errors simply
    try:
        number_choice = int(index)
        # make sure number fits inside the list
        if number_choice >= 0 and number_choice < len(tasks):
            tasks[number_choice]["completed"] = True
            print("Task marked as complete!")
            return True
        else:
            print("Invalid choice. Please try again.")
            return False
    except ValueError:
        print("Invalid choice. Please try again.")
        return False

# function to display pending tasks
def view_pending_tasks(tasks=tasks):
    # check if there are any uncompleted tasks
    pending_exists = False
    for single_task in tasks:
        if single_task["completed"] == False:
            pending_exists = True

    # if none are found print the error
    if pending_exists == False:
        print("No working currently")
        return

    print("Pending Tasks:")
    counter = 0
    for single_task in tasks:
        if single_task["completed"] == False:
            print("Index:", counter)
            print("Title:", single_task["title"])
            print("Due Date:", single_task["due_date"])
            print("---")
        counter = counter + 1

# function to calculate current progress percentage
def calculate_progress(tasks=tasks):
    total = len(tasks)
    # print message if list is empty
    if total == 0:
        print("No working currently")
        progress = 0.0
        return progress

    # count tasks that are done
    done_count = 0
    for single_task in tasks:
        if single_task["completed"] == True:
            done_count = done_count + 1

    # basic percentage calculation
    progress = (done_count / total) * 100
    print("Current progress:", progress, "%")
    return progress
