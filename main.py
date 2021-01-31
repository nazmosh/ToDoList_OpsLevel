from Todolist import ToDoList
from cli import Cli

if __name__ == "__main__":
    """ 
    todo1 = ToDoList()
    todo1.add_task(1,"kill bill")
    todo1.add_task(2,"boro baba")
    todo1.add_task(3,"boro bababa")
    todo1.del_task(101)
    todo1.add_task(3, "nazzyala")

    todo1.show_todo()
    todo1.find_missing_priorities()
    """
    
    cli = Cli()
    cli.run_cli()
