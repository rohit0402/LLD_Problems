class Screen:
    def __init__(self,screen_id:str):
        self.screen_id=screen_id
        self.seats=[]

    def add_seat(self,seat):
        self.seats.append(seat)