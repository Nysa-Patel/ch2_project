from datetime import datetime
tasks = []

print("To do list: Enter 3 tasks that are currently on your mind")
#asks user for 3 tasks
for i in range (3):
    task = input("\nEnter task: ")
    priority = input("Is this Urgent, Important, Somewhat Important, Can Wait, or Does not Matter for Now: ")
    duedate = input("When will this task be due (YYYY-MM-DD): ")
    duedate = datetime.strptime(duedate, "%Y-%m-%d")

    if priority == 'Urgent':
        priorityval =1
    elif priority == 'Important':
        priorityval = 2
    elif priority == 'Somewhat Important':
        priorityval = 3
    elif priority == 'Can Wait':
        priorityval = 4
    elif priority == 'Does not Matter for Now':
        priorityval = 5
    tasks.append((task, priorityval, duedate))


tasks.sort(key= lambda x: (x[2], x[1]))

print('\nSorted! Order for your tasks: ')
for task, priorityval, date in tasks:
    if priorityval == 1:
        priority = "Urgent"
    elif priorityval == 2:
        priority = "Important"
    elif priorityval == 3:
        priority = "Somewhat Important"
    elif priorityval == 4:
        priority = "Can Wait"
    else:
        priority = "Does not Matter for Now"

    #output
    print("- {task}, priority: {priority} (due {date.strftime('%Y-%m-%d')})")









