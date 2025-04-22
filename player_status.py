

class player():


    def __init__ (self, name):    
        self.name = name
        self.level = 1
    def set_postiton(self, postition):
        self.postiton = postition

    def set_level(self, level):
        self.level = level

    def set_status(self, random_score):
        self.status = random_score

    def level_up(self, level):
        self.set_level(level + 1)
        self.set_status(0)

    def level_down(self, level):
        self.set_level(level - 1)
        self.set_status(0)
        if self.level < 1:
            print("You are not a player anymore")

    def get_postiton(self):
        return self.postiton

    def get_level(self):
        return self.level
    
    
