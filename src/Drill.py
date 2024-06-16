import utils 

class Player: 
  def __init__(self, currentLine, id):
    self.id = id
    self.hasBall = False
    self.currentLine = currentLine
    self.previousLine = None
    self.oscillationCount = 0

class Drill:
  def __init__(self, numLines: int, numPlayers: int):
    assert numLines < numPlayers, "Number of lines must be less than number of players"
    assert numLines > 0, "Number of lines must be greater than 0"
    self.numLines = numLines
    self.numPlayers = numPlayers
    self.direction = 'right'
    self.startingLine = 0 # The line that starts with the ball
    self.lineWithBall = 0 # The line that has the ball
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
  def printDrill(self, iteration: int = -1):
    utils.printBlue(utils.boldText(f"Iteration {iteration}:" if iteration != -1 else "Initial State:"))

    for i in range(self.numLines):
        txt = utils.underlineText( f"Line {i + 1}:")
        print(f"{txt:<18}", end=" ")
    print()

    max_len = max(len(line) for line in self.lines)
    for i in range(max_len):
      for j in range(self.numLines):
        symbol = ""
        if i < len(self.lines[j]):
          player = self.lines[j][i]
          symbol = f"{player.id}b" if player.hasBall else player.id
        print(f"{symbol:<11}", end="")
      print()
    print()
  
  '''
  Divides the players as evenly as possible into 
  numLines # of lines.
  '''
  def buildLines(self):
    id = 1
    for i in range(self.numPlayers):
      self.lines[i % self.numLines].append(Player(i, id))
      id += 1
    self.lines[self.startingLine][0].hasBall = True
  
  '''
  Passes the ball from one line to the other in the direction 
  specified by the self.direction
  '''
  def passBall(self):
    if self.isLastLine():
      self.flipDirection()

    if self.direction == 'left':
      self.movePlayer(self.lineWithBall, self.lineWithBall - 1)
    else:
      self.movePlayer(self.lineWithBall, self.lineWithBall + 1)

  '''
  Move the first player in the passLine to the end of recieveLine.
  '''
  def movePlayer(self, passLine: int, recieveLine: int):
    if not self.lines[recieveLine]:
      raise Exception(f"Line {recieveLine + 1} is empty! Player in line {passLine + 1} is passing to no one!")
    
    if not self.lines[passLine]:
      raise Exception(f"Line {passLine + 1} is empty! Player in line {recieveLine + 1} is recieving from no one!")

    # the current player in the start line no longer has the ball
    self.lines[passLine][0].hasBall = False
    
    # update the number of times the player has oscillated
    if (not (passLine == 0 or passLine == self.numLines - 1) and
         self.lines[passLine][0].previousLine == recieveLine):
      self.lines[passLine][0].oscillationCount += 1

    # update the previous and current line of the player
    self.lines[passLine][0].previousLine = passLine
    self.lines[passLine][0].currentLine = recieveLine

    # move the player to the end of the line they just passed to
    self.lines[recieveLine].append(self.lines[passLine].pop(0))
    # the player in the reciving line now has the ball
    self.lines[recieveLine][0].hasBall = True

    self.lineWithBall = recieveLine

  '''
  checks if the line with the ball is the last line
  '''
  def isLastLine(self):
    if self.direction == 'left':
      return self.lineWithBall == 0
    else:
      return self.lineWithBall == self.numLines - 1
  
  '''
  flips the direction of the drill
  '''
  def flipDirection(self):
    if self.direction == 'left':
      self.direction = 'right'
    else:  
      self.direction = 'left'

  def printOsicllations(self):
    players = self.getAndSortPlayers()
    for player in players:
      if player.oscillationCount > 0:
        utils.printRed(f"Player {player.id} oscillated {player.oscillationCount} times.")
      else:
        utils.printGreen(f"Player {player.id} did not oscillate.")

  def getAndSortPlayers(self):
    players = []
    for line in self.lines:
      for player in line:
        players.append(player)
    players.sort(key=lambda x: x.id)
    return players