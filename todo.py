import time

def CreateTask(task):
    i = len(task)+1
    desc = input("Enter about the task to do.. : ")
    task[i] = {"description":desc,"status":False}
    time.sleep(2)
    print("--- Task creation successfull..! ---")

def UpdateTask(task):
    i=int(input("Enter the id of the task to update : "))
    if i in task:
        desc = input(f"Enter the description to update on the task {i} : ")
        task[i]["description"] = desc
        time.sleep(2)
        print("--- The task was updated successfully..! ---")

    else:
        print("The task id you entered is not available  ")

def DeleteTask(task):
    i = int(input("Enter the id of the task to delete from the list : "))
    if i in task:
        del task[i]
        time.sleep(2)
        print("--- The task was successfully deleted from the list..! ---")
    else:
        print("The task id you entered is not available : ")

def TaskDone(task):
    i = int(input("Enter the id of the task to mark it as completed : "))
    if i in task:
        task[i]["status"] = True
        time.sleep(2)
        print(f"--- The task with id {i} was marked as completed...! ---")
    else:
                print("The task id you entered is not available : ")


def ViewTask(task):
    if not task:
        print("Nothing in the list..!")
    else:
        time.sleep(2)
        for i,j in task.items():
            if j["status"]:
                s="done"
            else:
                s="pending"
            print(f"[{i}] {j['description']} => {s}")

            
task = {}
print("Welcome to TO DO LIST MANAGER!!")
time.sleep(2)
while(True):
    print("\n\t Options avail\n")
    print("\t---------------------------")
    print("\t1. Create Task")
    print("\t2. Delete Task")
    print("\t3. Update task")
    print("\t4. Mark Task as done")
    print("\t5. View Tasks")
    print("\t6. Exit..")
    

    c=int(input("Enter your choice : "))
    if c==1:
        CreateTask(task)

    elif c==2:
        DeleteTask(task)
    elif c==3:
        UpdateTask(task)
    elif c==4:
        TaskDone(task)
    elif c==5:
        ViewTask(task)
    else:
        print("Thank you..!")
        break


