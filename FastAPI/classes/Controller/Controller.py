from model.Usuario import Usuario
from model.Admin import Admin
from model.Task import Task

class Controller():

    user_list:list[Usuario] = []

    def __init__(self):
        self.user_list = []

    def removeUser(self, user: Usuario):
        if(user in self.user_list):
            self.user_list.remove(user)
            return True
        return False
       
    def addUsuario(self, login:str, password:str, email:str, id:str):
        new_user: Usuario = Usuario(login, password, email, id)
        self.user_list.append(new_user)
        return new_user

    def addAdmin(self, login:str, password:str, email:str, id:str):
        new_user: Admin = Admin(login, password, email, id)
        self.user_list.append(new_user)
        return new_user

    def deleteAdmin(self, adm: Admin):
        if(adm in self.user_list):
            self.user_list.remove(adm)
            return True
        return False
    
    def searchUser(self, id: str):
        for user in self.user_list:
            if user.id == id:
                return user
        return None