class Musician(object):
    def __init__(self, sounds, musician):
        self.sounds = sounds
        self.musician = musician

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)])
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"], "Bob")

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"], "Travis")

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Drummer, self).__init__(["Bang", "Bop", "Bam"], "Ringo")

    def count(self):
        print("And a one, two, three, four")

    def combust(self):
        print("COMBUST!")
        
class Band(Musician):

    def __str__(self):
        return "%s is hired!" % (self.musician)
        #return "%s is fired!" % (self.musician)
        
    def play(self):
        pass
    
guitarist = Guitarist()
guitarist.tune()

drummer = Drummer()
drummer.combust()
drummer.count()

# band = Band()
# band.__str__()