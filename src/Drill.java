import java.util.*;
public class Drill {
    private int currLine;
    private boolean goingRight;
    private int numPlayers;
    private int numLines;
    private final ArrayList<LinkedList<Player>> lines = new ArrayList<>();

    /**
     * Constructor
     * @param numLines > 1
     * @param numPlayer >= numLines
     * @param goingRight Direction the ball is going
     * @param startingLine < numLines
     */
    public Drill(int numLines, int numPlayer, boolean goingRight, int startingLine) {
        this.numLines = numLines;
        this.numPlayers = numPlayer;
        this.goingRight = goingRight;
        currLine = startingLine;
        buildLines();
    }

    /**
     * Runs drill where players pass the ball numPlayer
     * number of times. (eventually until every player
     * goes through every line)
     */
    public void runDrill() throws InterruptedException {
        int temp = numPlayers;
        while (temp!=0) {
            try {
                passBall();
            } catch (NoBallException e) {
                e.printStackTrace();
            }
            Thread.sleep(1000);
            printDrill();
            System.out.println("\n\n\n\n\n");
            temp--;
        }
    }

    /**
     * Prints the drill using * for players
     * without the ball and # for the player with the ball.
     */
    public void printDrill() {
        Player[] temp = new Player[lines.size()];
        for (int i = 0 ; i < temp.length ; i++) {
            temp[i] = lines.get(i).getLast();
        }
        int throughCount = 0;
        while (throughCount < numLines) {
            for (int i = 0 ; i < lines.size() ; i++) {
                LinkedList<Player> curr = lines.get(i);
                if (curr.getFirst().equals(temp[i]))
                    throughCount++;
                if (curr.getFirst().hasBall())
                    System.out.print("#\t");
                else
                    System.out.print("*\t");
                curr.add(curr.remove());
            }
            System.out.println();
        }
    }

    /**
     * Adds the appropriate number of lines and players per line
     * to the global variable, lines.
     */
    public void buildLines() {
        for (int i = 0 ; i < numLines ; i++) {
            lines.add(new LinkedList<>());
        }
        int index = 0;
        int x = numPlayers;
        while (x > 0) {
            if (index == numLines)
                index = 0;
            lines.get(index).add(new Player());
            x--;
            index++;
        }
        lines.get(0).getFirst().setHasBall(true);
    }

    /**
     * Passes the ball from the first player of one line to
     * the first player of the adjacent line in the given direction.
     * If there are no more lines in the given direction, switch
     * the direction.
     */
    public void passBall() throws NoBallException{
        if (!lines.get(currLine).getFirst().hasBall())
            throw new NoBallException();
        LinkedList<Player> curr = lines.get(currLine);
        LinkedList<Player> next;
        if (goingRight) {
            if (currLine+1 == lines.size()) {
                flipDirection();
                passBall();
                return;
            }
            next = lines.get(currLine+1);
        } else {
            if (currLine == 0) {
                flipDirection();
                passBall();
                return;
            }
            next = lines.get(currLine-1);
        }
        curr.getFirst().setHasBall(false);
        next.add(curr.remove());
        next.getFirst().setHasBall(true);
        if (goingRight)
            currLine++;
        else
            currLine--;
    }

    public void flipDirection() {
        goingRight = !goingRight;
    }

    public ArrayList<LinkedList<Player>> getLines() {
        return lines;
    }

    public int getNumPlayers() {
        return numPlayers;
    }

    public void setNumPlayers(int numPlayers) {
        this.numPlayers = numPlayers;
    }

    public int getNumLines() {
        return numLines;
    }

    public void setNumLines(int numLines) {
        this.numLines = numLines;
    }
}
