#Define the base class player
class player:
  def player(self):
    print("The player is playing cricket.")

#Define the drived clas Batsman
class Batsman(player):
  def player(self):
    print("The Batsman is batting.")
#Define the derived class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

#create objects of Batsman and Bowler classes 
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object
batsman.player()