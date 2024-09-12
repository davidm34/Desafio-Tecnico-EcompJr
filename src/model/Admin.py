from Usuario import Usuario

class Admin(Usuario):

    def __init__(self, login, password, email, id):
        super().__init__(login, password, email, id)

    def addUser(self, user_list:list, login:str, password:str, email:str, id:str):
        new_user: Usuario = Usuario(login, password, email, id)
        user_list.append(new_user)
        return True
    
    def removeUser(self, user:Usuario, user_list:list):
        if(user in user_list):
            user_list.remove(user)
            return True
        return False
    
    def searchUser(self, user_list: list, id: str):
        for user in user_list:
            if user.id == id:
                return user
        return None



