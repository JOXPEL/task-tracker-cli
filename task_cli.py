import json
import sys
import os
from datetime import datetime
#--------------------------------------------------------------------------------------------------------------
FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):  # if the file doesn't exist, create it with an empty list. 
        with open(FILE, "w") as f:
            json.dump([], f)
    with open(FILE, "r") as f:
        return json.load(f)
#--------------------------------------------------------------------------------------------------------------
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)
#--------------------------------------------------------------------------------------------------------------
def add_task(description):
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")
#--------------------------------------------------------------------------------------------------------------
def delete_task(task_id):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            found = True
    if found:
        save_tasks(tasks)
        print("Task removed successfully")
    else:
        print("Your id not found")
#--------------------------------------------------------------------------------------------------------------
def update_task(task_id, new_description):
    tasks = load_tasks()
    update = False
    for task in tasks:
            if task["id"] == task_id:
                task["description"] = new_description
                task["updatedAt"] = datetime.now().isoformat() 
                update = True
    if update:
        save_tasks(tasks)
        print("Your task have been updated successfully")
    else:
        print("Your id not found")
#--------------------------------------------------------------------------------------------------------------
def change_status(task_id, new_status):
    tasks = load_tasks()
    update = False
    for task in tasks:
            if task["id"] == task_id:
                task["status"] = new_status
                task["updatedAt"] = datetime.now().isoformat() 
                update = True
    if update:
        save_tasks(tasks)
        print("Your task status have been updated successfully")
    else:
        print("Your id not found")
#--------------------------------------------------------------------------------------------------------------
def list_tasks(status=None):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if status == None or task["status"] == status:
            print(task["id"])
            print(task["description"])
            print(task["status"])
            print(task["createdAt"])
            print(task["updatedAt"])
            print("=" *20)
            found = True
    if not found:
        print(f"No tasks found in this status: {status}")
#=============================================================================================================
# Without it — if someone imports your file, the CLI code will run automatically which is wrong!
# With it — the CLI code only runs when you call it directly from terminal.
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide an action!")
    else:
        action = sys.argv[1]
    if action == "add":
        description = sys.argv[2]
        add_task(description)
    elif action == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_id)
    elif action == "update":
        task_id = int(sys.argv[2])
        new_description = sys.argv[3]
        update_task(task_id, new_description)
    elif action == "mark-done":
        task_id = int(sys.argv[2])
        change_status(task_id, "done")
    elif action == "mark-in-progress":
        task_id = int(sys.argv[2])
        change_status(task_id, "in-progress")
    elif action == "list":
        if len(sys.argv) > 2: 
            status = sys.argv[2]
            list_tasks(status)
        else:
            list_tasks()
    else:
        print("Your action is incorrect")

