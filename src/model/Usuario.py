from Task import Task

class Usuario:

    login:str
    password:str
    email:str
    id:str
    task_list: list[Task] = []

    def __init__(self, login:str, password:str, email:str, id:str):

        self.login = login
        self.password = password
        self.email = email
        self.id = id

    def addTask(self, task_name: str):
        new_task: Task = Task(task_name)
        self.task_list.append(new_task)
        return True

    def deleteTask(self, task: Task):
        if(task in self.task_list):
            self.task_list.remove(task)
            return True
        return False
        

    def editTask(self, task:Task, new_name:str):
        if(task in self.task_list):
            task.change_name(new_name)
            return True
        return False
            

    def completeTask(self, task:Task):
        if(task in self.task_list):
            task.completeTask()
            return True
        return False

    def cancelCompleteTask(self, task:Task):
        if(task in self.task_list):
            task.cancelTask()
            return True
        return False

    def login(self, login:str, password:str):
        return login == self.login and password == self.password
        