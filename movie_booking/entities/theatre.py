class Theatre:
    def __init__(self,theatre_id:str,name:str):
        self.theatre_id=theatre_id
        self.name=name
        self.screens=[]

    def add_screen(self,screen):
        self.screens.append(screen)