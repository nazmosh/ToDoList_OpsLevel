from prettytable import PrettyTable

class ToDoList():

    def __init__(self):

        self.todo = {}
        self.missing_priorities = []
        self.uid = 100

    def add_task (self,priority,task):
        """This function takes the task and associated priority and adds it to the list with the allocated UID.

        Args:
            priority (integer): A positive integer representing the priority of the task.
            task (string): Title of the task
        """
        self.todo[self.uid] = (priority, task)
        self.uid += 1

    def del_task (self,uid):

        """ This function will delete the task based on its UID.

            Arg:
                uid (integer): A positive integer greater or equal to 100 which is allocated when the task is added.
        """
        if uid in self.todo.keys():
            del self.todo[uid]
    
    def find_missing_priorities (self):

        """ This funtion generates the list of missing priorities.

        Returns:
            list: An array of positive integers that represent the missing priorities from todo list.
        """

        all_tasks = self.todo.values()
        present_priorities = [t[0] for t in all_tasks]
        missing_priorities = set(range(1,max(present_priorities))) - set(present_priorities)
        return missing_priorities

    def show_todo(self):

        """This function prints the tasks, their priority and their associated UID in a table.
        """

        task_table = PrettyTable()
        task_table.field_names = ["UID", "Priority", "To Do"]
        sorted_todo = {key:value for key,value in sorted(self.todo.items(), key=lambda item: item[1][0])}
        for uid in sorted_todo.keys():
                task_table.add_row ([uid, sorted_todo[uid][0], sorted_todo[uid][1]])
        
        print(task_table)

    