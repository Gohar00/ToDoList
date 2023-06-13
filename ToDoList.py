import datetime
import time

todo_list = []


def display_todo_list(todo_list):
    print("========== TO-DO LIST ==========")
    now = datetime.datetime.now()
    for i, todo in enumerate(todo_list):
        task = todo["task"]
        deadline = todo.get("deadline", "No deadline set")
        deadline_date = todo.get("deadline_date")
        if todo.get("completed"):
            print(f"{i + 1}. [COMPLETED] {task} - Deadline: {deadline}")
        elif deadline_date is not None:
            time_until_deadline = deadline_date - now
            if time_until_deadline <= datetime.timedelta(minutes=13):
                print(f"{i + 1}. [DEADLINE APPROACHING] {task} - Deadline: {deadline}")
            elif time_until_deadline <= datetime.timedelta(minutes=15):
                print(f"{i + 1}. [URGENT] {task} - Deadline: {deadline}")
            else:
                print(f"{i + 1}. {task} - Deadline: {deadline}")
        else:
            print(f"{i + 1}. {task} - Deadline: {deadline}")
    print("================================")


def add_task(task, deadline):
    try:
        deadline_date = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M")
        todo_list.append({"task": task, "deadline": deadline, "deadline_date": deadline_date})
        print("Task added!")
    except ValueError:
        print("Invalid deadline format. Please use the format YYYY-MM-DD HH:MM.")



def mark_completed(task_number):
    if 1 <= task_number <= len(todo_list):
        completed_task = todo_list[task_number - 1]
        print(f"Completed: {completed_task['task']}")
        completed_task['completed'] = True
    else:
        print("Invalid task number!")


def change_task(task_number, new_task):
    if 1 <= task_number <= len(todo_list):
        todo_list[task_number - 1]['task'] = new_task
        print("Changed!")
    else:
        print("Invalid task number!")


def remove_task(task_number):
    if 1 <= task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Removed: {removed_task['task']}")
    else:
        print("Invalid task number!")


def mark_deadline(task_number):
    if 1 <= task_number <= len(todo_list):
        deadline = input("Enter the deadline (YYYY-MM-DD HH:MM format): ")
        try:
            deadline_date = datetime.datetime.strptime(deadline, "%Y-%m-%d %H:%M")
            todo_list[task_number - 1]['deadline'] = deadline
            todo_list[task_number - 1]['deadline_date'] = deadline_date
            print("Deadline added/updated!")
        except ValueError:
            print("Invalid deadline format. Please use the format YYYY-MM-DD HH:MM.")
    else:
        print("Invalid task number!")


def show_count():
    completed_tasks = sum(1 for todo in todo_list if todo.get("completed"))
    uncompleted_tasks = len(todo_list) - completed_tasks
    print(f"Completed tasks: {completed_tasks}")
    print(f"Uncompleted tasks: {uncompleted_tasks}")


def main():
    while True:
        display_todo_list(todo_list)
        print("\nWhat would you like to do?")
        print("1. Add a new task")
        print("2. Mark a task as completed")
        print("3. Change a task")
        print("4. Remove a task")
        print("5. Mark deadline")
        print("6. Show the number of completed and uncompleted tasks")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            new_task = input("Enter the new task: ")
            deadline = input("Enter the deadline (YYYY-MM-DD HH:MM format): ")
            add_task(new_task, deadline)
            time.sleep(1)
        elif choice == "2":
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_completed(task_number)
        elif choice == "3":
            task_number = int(input("Enter the task number to change it: "))
            new_task = input("Enter the new task: ")
            change_task(task_number, new_task)
        elif choice == "4":
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        elif choice == "5":
            task_number = int(input("Enter the task number to add/update the deadline: "))
            mark_deadline(task_number)
        elif choice == "6":
            show_count()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
