def task():
    tasks = []
    print("--------------WELCOME TO THE TASK MANAGEMENT APP------------")

    total_tasks = int(input("ENTER THE TOTAL TASKS YOU WANT TO ADD IN NUMBERS: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    print(f"TODAY'S TOTAL TASKS ARE \n{tasks}")

    while True:
        operation = int(input("ENTER: 1-add\n2-update\n3-delete\n4-view\n5-exit\n"))
        if operation == 1:
            add = input("ENTER THE TASK: ")
            tasks.append(add)
            print(f"NEW TASK = {add} HAS BEEN ADDED")

        elif operation == 2:
            updated_value = input("ENTER THE TASK NAME YOU WANT TO UPDATE: ")
            if updated_value in tasks:
                up = input("ENTER THE NEW TASK: ")
                ind = tasks.index(updated_value)
                tasks[ind] = up
                print(f"YOUR UPDATED TASK IS = {up}")

        elif operation == 3:
            del_task = input("ENTER THE TASK WHICH YOU WANT TO DELETE: ")
            if del_task in tasks:
                tasks.remove(del_task)
                print(f"TASK {del_task} HAS BEEN DELETED")

        elif operation == 4:
            print(f"TOTAL TASKS ARE {tasks}")

        elif operation == 5:
            print("CLOSING THE PROGRAM...")
            break

        else:
                        print("INVALID INPUT...")
            
            
task()
