tasks = []

while True:
    print("\nTo-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Quit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)
        print("Added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks")
        else:
            for i in range(len(tasks)):
                print(str(i+1) + ". " + tasks[i])

    elif choice == "3":
        for i in range(len(tasks)):
            print(str(i+1) + ". " + tasks[i])
        num = int(input("Remove which: "))
        tasks.pop(num-1)
        print("Removed!")

    elif choice == "4":
        print("Goodbye!")
        break
