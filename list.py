class ToDoList:
    def __init__(self):
        self.tasks=[]

    def add(self,task):
        self.tasks.append({'task':task, 'completed': False})
        print(f"Task '{task}' added successfully")

    def show(self):
        if not self.tasks:
            print("no tasks to display")
        else:
            print("Tasks:")
            for index, task_info in enumerate(self.tasks, start=1):
                task_status="Done" if task_info['completed'] else ""
                print(f"{index}.[{task_status}]{task_info['task']}")

    def mark_as_completed(self,task_index):
        try:
            task_info= self.tasks[task_index-1]
            task_info['completed']=True
            print(f"Task'{task_info['task']}'marked as completed")
        except IndexError:
            print("invalid task index")


if __name__=="__main__":
    todolist= ToDoList()

    while True:
        print("\n To-Do List:")
        print("1.Add")
        print("2.Show")
        print("3.Mark as complete")
        print("4.Exit")

        choice = input("Enter your choice : ")

        if choice =="1":
            task = input("Enter the task ")
            todolist.add(task)
        elif choice =="2":
            todolist.show()
        elif choice =="3":
            todolist.show()
            task_index= int(input("Enter the index of the task to mark as completed "))
            todolist.mark_as_completed(task_index)
        elif choice=="4":
            print("Exiting ")
            break
        else:
            print("Invalid choice")
