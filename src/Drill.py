class Player: 
  def __init__(self):
    self.hasBall = False
    self.running = False

class Drill:
  
  def __init__(self, numLines: int, numPlayers: int):
    assert(numLines < numPlayers, "Number of lines must be less than number of players")
    assert(numLines > 0, "Number of lines must be greater than 0")
    self.numLines = numLines
    self.numPlayers = numPlayers
    self.direction = 'left'
    self.startingLine = 0
    self.currentLine = 0
    self.lines = [[] for i in range(numLines)]
    self.buildLines()
    print(self.lines)
    
  '''
  Runs drill where players pass the ball n times.
  '''
  def runDrill(self, n: int):
    pass
  
  '''
  Prints the drill using * for players without the ball and 
  # for players with the ball.
  '''
  def printDrill(self):
    for line in self.lines:
      for player in line:
        if player.hasBall:
          print('#', end=' ')
        else:
          print('*', end=' ')
      print()
  
  '''
  Divides the players as evenly as possible into 
  numLines # of lines.
  '''
  def buildLines(self):
    for i in range(self.numPlayers):
      self.lines[i % self.numLines].append(Player())
    self.lines[self.startingLine][0].hasBall = True
  
  '''
  Passes the ball from one line to the other in the direction 
  specified by the self.direction
  '''
  def passBall(self):
    pass
  
  def flipDirection(self):
    if self.direction == 'left':
      self.direction = 'right'
    else:  
      self.direction = 'left'
