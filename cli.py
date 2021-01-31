from Todolist import ToDoList

class Cli:

    def __init__(self):
        self.todo = ToDoList()
        
    def menu_prompt (self):
        print ("Pick from the options below:")
        print ("1. Show My To Do List")
        print ("2. Create New Item")
        print ("3. Delete Existing Item")
        print ("4. Show The Missing Priorities")
        print ("0. Exit")

        user_input = input ("\n$ : ")

        return user_input
    
    def run_cli(self):
        

        user_input = self.menu_prompt()

        while user_input != '0':
            if user_input == '1':
                self.todo.show_todo()
            elif user_input == '2':
                self.add_menu()
            elif user_input == '3':
                self.del_menu()
            elif user_input == '4':
                self.show_missing()
            else:
                print("Command not valid, please pick a command between 1 and 4.")
            
            user_input = self.menu_prompt()

    def add_menu(self):
        priority = input("Task priority: ")
        task_description = input("Task description: ")

        self.todo.add_task(int(priority), task_description)

    def del_menu(self):
        self.todo.show_todo()

        uid = input("Choose the UID of the task you wish to delete: ")
        self.todo.del_task(int(uid))

    def show_missing (self):
        
        missing_priorities = self.todo.find_missing_priorities()
        if len(missing_priorities) > 0:
            print ("Missing Priorities are: ", self.todo.find_missing_priorities())
        else:
            print ("There are no missing priorities.")

