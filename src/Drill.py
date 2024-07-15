import utils 
import argparse

class Player: 
  def __init__(self, currentLine: int, id):
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
  def runDrill(self, 
               n: int, 
               color_ball = True, 
               verbose = True):
    self.printDrill()
    for i in range(n):
      self.passBall()
      if verbose:
        self.printDrill(i+1, color_ball)
  
  '''
  Prints the drill using * for players without the ball and 
  # for players with the ball.
  '''
  def printDrill(self, iteration: int = -1, color_ball = True):
    utils.printCyan(utils.boldText(f"Iteration {iteration}:" if iteration != -1 else "Initial State:"))

    for i in range(self.numLines):
        txt = utils.underlineText( f"Line {i + 1}:")
        print(f"{txt:<18}", end=" ")
    print()

    max_len = max(len(line) for line in self.lines)
    # iterate through the length of the longest line
    for i in range(max_len):
      # iterate through the number of lines
      for j in range(self.numLines):
        # print the player id if the line has a player at that index
        if i < len(self.lines[j]):
          player = self.lines[j][i]
          symbol = f"{player.id}"
          if player.hasBall:
            if color_ball:
              utils.printYellow(f"{symbol:<11}", end="")
            else:
              print(f"{symbol:<11}b", end="")
          else:
            print(f"{symbol:<11}", end="")
        # print nothing if the line does not have a player at that index
        else:
          print(" "*11, end="")
      # separate rows
      print()

    # new line for appearance
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

    curr_player = self.lines[passLine][0]

    # the current player in the start line no longer has the ball
    curr_player.hasBall = False
    
    # update the number of times the player has oscillated
    if (not (passLine == 0 or passLine == self.numLines - 1) and
         curr_player.previousLine == recieveLine):
      curr_player.oscillationCount += 1

    # update the previous and current line of the player
    self.lines[passLine].pop(0)
    curr_player.previousLine = passLine
    curr_player.currentLine = recieveLine

    # move the player to the end of the line they just passed to
    self.lines[recieveLine].append(curr_player)
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

  '''
  Prints the number of times each player oscillated.
  '''
  def printOsicllations(self):
    players = self.getAndSortPlayers()
    for player in players:
      if player.oscillationCount > 0:
        utils.printRed(f"Player {player.id} oscillated {player.oscillationCount} times.")
      else:
        utils.printGreen(f"Player {player.id} did not oscillate.")

  '''
  Gets all the players in the drill and sorts them by id.
  '''
  def getAndSortPlayers(self):
    players = []
    for line in self.lines:
      for player in line:
        players.append(player)
    players.sort(key=lambda x: x.id)
    return players

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a drill.')
    parser.add_argument(
      "lines", 
      type=int, 
      help='Number of lines', 
      default=3)
    
    parser.add_argument("players", 
                        type=int, 
                        help='Number of players', 
                        default=9)
    
    parser.add_argument("-p", type=int, help='Number of passes', default=40)
    args = parser.parse_args()

    drill = Drill(args.lines, args.players)
    drill.runDrill(args.p)
    drill.printOsicllations()