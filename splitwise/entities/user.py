class User:
    def __init__(self,user_id:str,name:str):
        self.user_id=user_id
        self.name=name

#added repr method because we want to print the name of the user
    def __repr__(self):
        return self.name