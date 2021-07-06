class ToDoList:
    def __init__(self, file_name):
        self.file_name = file_name
        self.tasks = self.load_file_into_list()

    def load_file_into_list(self):
        tasks = []
        with open(self.file_name, 'r') as f:
            for task in f:
                tasks.append(task.strip())
        return tasks

    def list_task(self):
        for index, task in enumerate(self.tasks, start=1):
                print('{}) {}'.format(index, task))

    def write_into_file(self):
        with open(self.file_name, 'w') as f:
            for task in self.tasks:
                f.write('{}\n'.format(task))
                
    def add_task(self, task):
        self.tasks.append(task)
        self.write_into_file()

    def done_task(self, task_index):
        try:
            del(self.tasks[task_index-1])
            self.write_into_file()
        except IndexError:
            print('There are no open tasks with index {}'.format(task_index))
       

def todo_help():
    print()
    print("To-do List")
    print("* Create new task: [todo TASK]")
    print("* Mark a task as done: [done INDEX]")
    print("* See the to-do list: [list]")
    print()


def run():
    todolist = ToDoList('todolist.txt')
    todo_help()
    
    while True:
        cmd_detail = input('Enter cmd: ')
        cmd = cmd_detail.split(' ', 1)[0]
        if cmd == 'list':
            todolist.list_task()
        elif cmd == 'todo':
            task_descr = cmd_detail.split(' ', 1)[1]
            todolist.add_task(task_descr)
        elif cmd == 'done':
            task_index = int(cmd_detail.split(' ', 1)[1])
            todolist.done_task(task_index)
        elif cmd == 'help':
            todo_help()
        else:
            break

run()


