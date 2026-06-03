# assignment: task utility functions
# description: helper functions to add, view, and complete tasks

from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    # check everything first
    check1 = validate_task_title(title)
    check2 = validate_task_description(description)
    check3 = validate_due_date(due_date)

    if check1 == True and check2 == True and check3 == True:
        # build the task map structure
        new_task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }
        tasks.append(new_task)
        print("Task added successfully!")
        return True
    else:
        print("Validation failed.")
        return False

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    # check if they typed digits before converting
    if str(index).isdigit():
        number_choice = int(index)

        # check if the number choice is inside our list size
        if number_choice >= 0 and number_choice < len(tasks):
            tasks[number_choice]["completed"] = True
            print("Task marked as complete!")
            return True
        else:
            print("Invalid index choice.")
            return False
    else:
        print("Error: Please enter a valid number, not text.")
        return False


# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    print("Pending Tasks:")


      # check if the list has nothing inside
    if len(tasks) == 0:
        print("No task found.")
        return

    # simple counting loop
    counter = 0
    for single_task in tasks:
        if single_task["completed"] == False:
            print("Index:", counter)
            print("Title:", single_task["title"])
            print("Due Date:", single_task["due_date"])
            print("---")
        counter = counter + 1

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    total = len(tasks)

    if total == 0:
        progress = 0.0
        print("Current progress:", progress, "%")
        return progress

    # count completed tasks manually
    done_count = 0
    for single_task in tasks:
        if single_task["completed"] == True:
            done_count = done_count + 1

    # basic percentage calculation
    progress = (done_count / total) * 100
    print("Current progress:", progress, "%")
    return progress
