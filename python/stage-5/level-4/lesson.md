# Level 4: Simple To-Do List

> **📖 LESSON NOTE:** This lesson file is **read-only** to prevent accidental edits. Your code goes in the **right window** (\`main.cpp\` or similar). The lesson stays on the **left** for reference. Press \`Ctrl+l\` to switch to your code window, or \`<Space>h\` for help.



## Stage 5: Capstone Project

### Your Project

Build a to-do app that:

1. Displays menu: Add, View, Remove, Quit
2. Add tasks to list
3. Show all tasks with numbers
4. Remove tasks by number
5. Save when quitting

---

## ANSWER KEY

```python
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
```

---

**List management and data persistence!**
