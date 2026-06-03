# Import all the needed functions from our package
from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

import time

def main():
    while True:
        # Show menu options to the user
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            # get all input data from the user
            title = input("Enter task title: ").capitalize()
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            # extract only the numbers typed by the user
            only_numbers = ""
            for character in due_date:
                if character.isdigit():
                    only_numbers = only_numbers + character

            # automatically split into 4, 2, and 2 numbers with dashes
            if len(only_numbers) >= 8:
                year = only_numbers[0:4]
                month = only_numbers[4:6]
                day = only_numbers[6:8]
                due_date = year + "-" + month + "-" + day

            # pass data to our utility function
            add_task(title, description, due_date)

        elif choice == "2":
            index = input("Enter the task index to mark as complete: ")
            mark_task_as_complete(index)

        elif choice == "3":
            view_pending_tasks()

        elif choice == "4":
            calculate_progress()

        elif choice == "5":
            print("Exiting the program...")
            time.sleep(2)
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

