class Player: 
  def __init__(self, currentLine):
    self.hasBall = False
    self.currentLine = currentLine
    self.previousLine = None
    self.oscillation_count = 0

class Drill:
  def __init__(self, numLines: int, numPlayers: int):
    assert(numLines < numPlayers, "Number of lines must be less than number of players")
    assert(numLines > 0, "Number of lines must be greater than 0")
    self.numLines = numLines
    self.numPlayers = numPlayers
    self.direction = 'right'
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
      self.lines[i % self.numLines].append(Player(i))
    self.lines[self.startingLine][0].hasBall = True
  
  '''
  Passes the ball from one line to the other in the direction 
  specified by the self.direction
  '''
  def passBall(self):
    if self.isLastLine():
      self.flipDirection()

    if self.direction == 'left':
      self.movePlayer(self.currentLine, self.currentLine - 1)
    else:
      self.movePlayer(self.currentLine, self.currentLine + 1)

  '''
  Move the first player in the passLine to the end of recieveLine.
  '''
  def movePlayer(self, passLine: int, recieveLine: int):
    if not self.lines[recieveLine]:
      raise Exception(f"Line {recieveLine} is empty! Player in line {passLine + 1} is passing to no one!")
    
    # the current player in the start line no longer has the ball
    self.lines[passLine][0].hasBall = False
    
    # update the number of times the player has oscillated
    if self.lines[passLine][0].previousLine == recieveLine:
      self.lines[passLine][0].oscillation_count += 1

    # update the previous and current line of the player
    self.lines[passLine][0].previousLine = passLine
    self.lines[passLine][0].currentLine = recieveLine

    # move the player to the end of the line they just passed to
    self.lines[recieveLine].append(self.lines[passLine].pop(0))
    # the player in the reciving line now has the ball
    self.lines[recieveLine][0].hasBall = True

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
