class luck(parents_luck):
    death = death() # ?
    # Before birth, there is no luck (zero)
    # Once born, instantiated, luck will be inherited from parents
    if time > parents_luck.death:
        # Assuming parents are dead
        luck = parents_luck.luck
    else:
        # Parents are alive
        luck = parents_luck.get_luck()
    def lucky():
        if time == death:
           break
        else:
           continue
        return (opportunity * self.lucky()) + preparation
    def get_luck(self):
        # Total luck can only be calculated at time of death
        self.luck = self.lucky()
