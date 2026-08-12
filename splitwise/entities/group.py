class Group:
    def __init__(self,group_id:str,name:str):
        self.group_id=group_id
        self.name=name
        self.members=[]

    def add_member(self,user):
        if user not in self.members:
            self.members.append(user)