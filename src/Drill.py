class Player: 
  def __init__(self):
    self.hasBall = False

class Drill:
  def __init__(self, numLines: int, numPlayers: int):
    assert(numLines < numPlayers, "Number of lines must be less than number of players")
    assert(numLines > 0, "Number of lines must be greater than 0")
    self.numLines = numLines
    self.numPlayers = numPlayers
    self.direction = 'left'
    self.startingLine = 0 # The line that starts with the ball
    self.currentLine = 0 # The line that has the ball
    self.lines = [[] for i in range(numLines)] # array of lines
    self.buildLines() # Distribute players into lines
    
  '''
  Runs drill where players pass the ball n times.
  '''
  def runDrill(self, n: int):
    self.printDrill()
    for i in range(n):
      self.passBall()
      self.printDrill(i+1)
  
  '''
  Prints the drill using * for players without the ball and 
  # for players with the ball.
  '''
  def printDrill(self, n: int = -1):
    if n != -1:
      print(f"Iteration {n}:")
    else:
      print("Drill:")
    
    for i in range(self.numLines):
      print(i+1, end=" ")
    print()
    lens = [len(line) for line in self.lines]
    maxLen = max(lens)
    for i in range(maxLen):
      for j in range(self.numLines):
        if i < lens[j]:
          if self.lines[j][i].hasBall:
            print("#", end=" ")
          else:
            print("*", end=" ")
        else:
          print(" ", end=" ")
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
    if self.isLastLine():
      self.flipDirection()
    if self.direction == 'left':
      self.lines[self.currentLine][0].hasBall = False
      self.currentLine -= 1
      if not self.lines[self.currentLine]:
        raise Exception(f"Line {self.currentLine} is empty! Player in line {self.currentLine + 1} are passing to no one!")
      self.lines[self.currentLine][0].hasBall = True
      self.lines[self.currentLine].append(self.lines[self.currentLine + 1].pop(0))
    else:
      self.lines[self.currentLine][0].hasBall = False
      self.currentLine += 1
      if not self.lines[self.currentLine]:
        raise Exception(f"Line {self.currentLine} is empty! Player in line {self.currentLine - 1} are passing to no one!")
      self.lines[self.currentLine][0].hasBall = True
      self.lines[self.currentLine].append(self.lines[self.currentLine - 1].pop())

  def isLastLine(self):
    if self.direction == 'left':
      return self.currentLine == 0
    else:
      return self.currentLine == self.numLines - 1
  
  def flipDirection(self):
    if self.direction == 'left':
      self.direction = 'right'
    else:  
      self.direction = 'left'
