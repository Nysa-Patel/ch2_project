import sqlite3
from datetime import datetime

conn = sqlite3.connect("to_do.db")
cursor = conn.cursor() #create cursor command to execute commands
#delete prev runs


#creates the table if not already create (tasks)
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT,
    priority TEXT,
    priorityval INTEGER,
    duedate TEXT
)
''')
conn.commit()

cursor.execute("DELETE FROM tasks")
conn.commit()

user_answer='1'
#tasks = []

print("To do list ")
#asks user for tasks
while(user_answer =='1'):
    task = input("\nEnter task: ")
    priority = input("Is this Urgent, Important, Somewhat Important, Can Wait, or Does not Matter for Now: ")
    duedate = input("When will this task be due (YYYY-MM-DD): ")
    duedate = datetime.strptime(duedate, "%Y-%m-%d")

    if priority == "Urgent":
        priorityval =1
    elif priority == "Important":
        priorityval = 2
    elif priority == "Somewhat Important":
        priorityval = 3
    elif priority == "Can Wait":
        priorityval = 4
    else: 
        priorityval = 5

    #tasks.append((task, priority, priorityval, duedate))

    #insert data from user into database
    cursor.execute(
        "INSERT INTO tasks (task, priority, priorityval, duedate) VALUES (?, ?, ?, ?)", #? represent the four parameters
        (task, priority, priorityval, duedate.strftime("%Y-%m-%d"))
    )
    conn.commit()

    user_answer = input("Do you want to enter in another input? 1 for yes 2 for no: ")


#tasks.sort(key= lambda x: (x[2], x[1]))

#displays task
cursor.execute("SELECT task, priority, priorityval, duedate FROM tasks ORDER BY duedate, priorityval")
tasks = cursor.fetchall()


print('\nSorted! Order for your tasks: ')
for task, priority, priorityval, date in tasks:
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
    print(f"- {task}, priority: {priority} (due {date})")
conn.close()
