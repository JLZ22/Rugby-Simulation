class Player: 
  def __init__(self):
    self.hasBall = False
    self.running = False

class Drill:
  
  def __init__(self, numLines: int, numPlayers: int, direction: str, startingLine: int):
    if (startingLine >= numLines):
      raise Exception('Your starting line is larger than the number of lines in this drill.')
    self.numLines = numLines
    self.numPlayers = numPlayers
    self.direction = -1 if direction == 'left' else 1
    self.startingLine = startingLine
    self.currentLine = startingLine
    self.lines = [[None] for i in range(numLines)]
    
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
    pass
  
  '''
  Divides the players as evenly as possible into 
  numLines # of lines.
  '''
  def buildLines(self):
    pass
  
  '''
  Passes the ball from one line to the other in the direction 
  specified by the self.direction
  '''
  def passBall(self):
    pass
  
  def flipDirection(self):
    self.direction = -1 * self.direction
