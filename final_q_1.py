import random

class Player:

    def __init__(self,name,health):
        self.name=name
        self.health=health  

    def damage(self):
        self.hit=random.randint(1,10)
        return self.hit

    def health(self,user):
        pass

player1=Player("player1",100)
player2=Player("player2",100)

for i in range(1):
    if player2.health>=0:
        hit=player1.damage()
        player2.health-=hit
        print(hit)
    else:
        print("player2 died")
    if player1.health>=0:
        hit=player2.damage()
        player1.health-=hit
        print(hit)

    else:
        print("player1 died")


print(player1.health)
print(player2.health)

