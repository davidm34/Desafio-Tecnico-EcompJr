class Task:

    name:str
    is_completed:bool

    def __init__(self, name):
        self.name = name
        self.is_completed = False

    def change_name(self, name:str):
        self.name = name
        return True
    
    def completeTask(self):
        if(not self.is_completed):
            self.is_completed = True
            return True
        return False
    
    def cancelTask(self):
        if(self.is_completed):
            self.is_completed = False
            return True
        return False

